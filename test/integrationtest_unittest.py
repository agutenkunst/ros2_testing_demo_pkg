#!/usr/bin/python

"""
This test can be executed directly using
python3 integrationtest_unittest.py
"""

import sys

import unittest
import rclpy
import time

class TestSum(unittest.TestCase):
    def test_demo(self):
        time.sleep(5)
        self.assertTrue(True)

def main(args=None):
    sys.argv = [sys.argv[0]]
    unittest.main()

if __name__ == "__main__":
    rclpy.init()
    main()
