#!/usr/bin/python

"""
This test can be executed directly using
python3 integrationtest_unittest.py
"""

import sys

import unittest
import rclpy

class TestSum(unittest.TestCase):
    def test_demo(self):
        self.assertTrue(False)

def main(args=None):
    sys.argv = [sys.argv[0]]
    unittest.main()

if __name__ == "__main__":
    rclpy.init()
    main()
