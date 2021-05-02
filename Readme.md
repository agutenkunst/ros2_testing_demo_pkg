# ROS2 testing demo

## Usage
Run unittest and integrationtest
```
colcon build && colcon test && colcon test-result
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

## Relevant issues
https://github.com/ros2/rcutils/issues/204
