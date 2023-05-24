# POSE_EKF

A Sensor Fusion packge to fuse `Odom Data` and `IMU Data`, to output a more clean `Odom Data`.

| Input | Type | Description |
|-------|------|-------------|
| `~/raw_odom` | nav_msgs/msg/Odometry | Raw Odometry Data from the robot |
| `~/processed_imu` | sensor_msgs/msg/Imu | Processed IMU data | 

|Output | Type | Description |
|-------|------|-------------|
| `~/processed_odom` | nav_msgs/msg/Odometry | Processed Odometry Data |