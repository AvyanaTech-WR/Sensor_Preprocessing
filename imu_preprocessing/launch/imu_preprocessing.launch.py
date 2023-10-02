import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = FindPackageShare(package='imu_preprocessing').find('imu_preprocessing')
    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("imu_preprocessing"), 'config', 'ekf.yaml')],
            remappings=[('/odometry/filtered', '/IMU/processed')],
            arguments=['--ros-args', '--log-level', 'debug']
        )
    ])

if __name__ == '__main__':
    generate_launch_description()