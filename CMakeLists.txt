cmake_minimum_required(VERSION 3.5)
project(ros2_testing_demo_pkg)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

add_executable(simple_pub_node src/simple_pub_node.cpp)
target_include_directories(simple_pub_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

install(TARGETS simple_pub_node
  DESTINATION lib/${PROJECT_NAME})

# Install Python modules
ament_python_install_package(${PROJECT_NAME})
# Install Python executables
install(PROGRAMS
  scripts/simple_py_pub_node.py
  DESTINATION lib/${PROJECT_NAME}
)


#############
## TESTING ##
#############

if(BUILD_TESTING)

  find_package(ament_cmake_gtest REQUIRED) # Includes the package "ament_cmake_gtest" providing the macros ament_add_gtest, ...
  find_package(ros_testing REQUIRED) #Needs package.xml: <test_depend>ros_testing</test_depend>

  # A basic unittest based on gtest
  ament_add_gtest(unittest_gtest test/unittest_gtest.cpp) #Macro provided by https://github.com/ament/ament_cmake/blob/84719051ef2b26070de484e60b8f060ae7a70b06/ament_cmake_gtest/cmake/ament_add_gtest.cmake#L52
  target_link_libraries(unittest_gtest)

  # Integrationtest using gtest (see https://github.com/ros-planning/moveit2/blob/main/moveit_ros/moveit_servo/CMakeLists.txt)
  ament_add_gtest_executable( #Macro provided by https://github.com/ament/ament_cmake/blob/84719051ef2b26070de484e60b8f060ae7a70b06/ament_cmake_gtest/cmake/ament_add_gtest_executable.cmake#L34
    integrationtest_gtest
    test/integrationtest_gtest.cpp
  )
  target_link_libraries(integrationtest_gtest)
  ament_target_dependencies(integrationtest_gtest)
  add_ros_test(test/integrationtest_gtest.test.py ARGS "test_binary_dir:=${CMAKE_CURRENT_BINARY_DIR}") #TODO arg needed? # macro provided by https://github.com/ros2/ros_testing/blob/4d5cf881e59c93821a439262cdea5ee961593d21/ros_testing/cmake/add_ros_test.cmake#L61

  add_ros_test(test/integrationtest_unittest.test.py)


  # find_package(ament_lint_auto REQUIRED) TODO USAGE
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)



  # ament_lint_auto_find_test_dependencies() TODO usage?
endif()

ament_package()

