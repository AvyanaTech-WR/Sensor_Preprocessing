import os, sys
import math

import numpy as np

import threading, argparse
import time

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

class Odom_EKF(Node):
    def __init__(self):
        super().__init__('odom_ekf')

        # Odometry Subscription
        self.subscribe_raw_odom = self.create_subscription(Odometry, '~/raw_odom', self.odom_callback, 10)
        # IMU Subscription
        self.subscribe_processed_imu = self.create_subscription(Imu, '~/processed_imu', self.imu_callback, 10)

        # Processed Odometry Publish
        self.processed_odom_publisher = self.create_publisher(Odometry, '~/processed_odom', 10)

    def process_odom_EKF():
    
    def odom_callback(self, msg):

    def imu_callback(self, msg):


def main(args = None):
    rclpy.init(args=args)
    node = Odom_EKF()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
