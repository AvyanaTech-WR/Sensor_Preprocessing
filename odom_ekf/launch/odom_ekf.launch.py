from launch import LaunchDescription
form launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'odom_ekf',
            executable='odom_ekf'
        )
    ])