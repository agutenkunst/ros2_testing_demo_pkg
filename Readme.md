# ROS2 testing demo

This packages is create while learning how to write tests for ROS2.

So far it contains the following types of tests

- A unittest based on gtest (unittest_gtest.cpp)
- An integrationtest (launch based) using gtest (integrationtest_gtest.*)

## Usage
Run unittest and integrationtest
```
colcon build && colcon test && colcon test-result
```
to have more verbose output
```
colcon build && colcon test --event-handlers console_direct+ && colcon test-result
```

### Run single integrationtest
```
ros2 test src/ros2_testing_demo_pkg/test/integrationtest_gtest.test.py test_binary_dir:=build/ros2_testing_demo_pkg
```


## TODO
- [ ] Run single test

## Sources
https://github.com/ros2/launch/issues/466#issuecomment-715372369
https://roscon.ros.org/2019/talks/roscon2019_launch_testing_presentation.pdf
https://github.com/ros2/launch_ros/blob/master/launch_testing_ros/test/examples/talker_listener_launch_test.py
https://roboticsbackend.com/ros2-package-for-both-python-and-cpp-nodes/#Compile_and_run_your_ROS2_Cpp_and_Python_nodes

Writing Integrationtests
https://github.com/ros-planning/moveit2/blob/main/moveit_ros/moveit_servo/CMakeLists.txt

## Relevant issues
https://github.com/ros2/rcutils/issues/204
