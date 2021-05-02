import unittest

import launch
import launch_ros
import launch_testing
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

import pytest

@pytest.mark.rostest
def generate_test_description():
    test_node = launch_ros.actions.Node(
        executable=PathJoinSubstitution([LaunchConfiguration('test_binary_dir'), 'integrationtest_gtest']),
        parameters=[],
        output='screen',
    )


    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='test_binary_dir', # From https://github.com/ros-planning/moveit2/blob/1e1337b46daed0aaa1252b87367c1824f46c9b1a/moveit_ros/moveit_servo/test/launch/servo_launch_test_common.py#L92
                                             description='Binary directory of package containing test executables'),
        # other fixture actions
        test_node,
        launch_testing.actions.ReadyToTest(),
    ])

@launch_testing.post_shutdown_test()
class TestOutcome(unittest.TestCase):

    def test_exit_codes(self, proc_info):
        launch_testing.asserts.assertExitCodes(proc_info)