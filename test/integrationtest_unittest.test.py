import unittest
import rclpy

import launch
import launch_ros
import launch_testing
import launch_testing.asserts
import std_msgs.msg
import time


import pytest

from launch_testing.asserts.assert_exit_codes import EXIT_OK

@pytest.mark.rostest
def generate_test_description():

    test_node = launch_ros.actions.Node(# see https://github.com/ros2/launch_ros/blob/999b208a05998a83378f7ba273b8146ea3eb09d9/launch_testing_ros/test/examples/talker_listener_launch_test.py
        package='ros2_testing_demo_pkg',
        executable='simple_py_pub_node.py',
        additional_env={'PYTHONUNBUFFERED': '1'},
        parameters=[],
        output='screen',
    )


    return launch.LaunchDescription([
        test_node,
        launch_testing.actions.ReadyToTest(),
    ]), locals()

class TestReceive(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = rclpy.create_node('test_receiver')

    def tearDown(self):
        self.node.destroy_node()

    def test_receive(self):
        msgs = []

        sub = self.node.create_subscription(
            std_msgs.msg.String,
            'topic',
            lambda msg: msgs.append(msg),
            10
        )
        try:
            end_time = time.time() + 10
            while time.time() < end_time:
                rclpy.spin_once(self.node, timeout_sec=0.1)
                if len(msgs) > 2:
                    break

            self.assertGreater(len(msgs), 2)

        finally:
            self.node.destroy_subscription(sub)