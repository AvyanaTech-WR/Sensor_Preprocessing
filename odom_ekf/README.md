# ODOM_EKF

A Sensor Fusion packge to fuse `Odom Data` and `IMU Data`, to output a more clean `Odom Data`.

| Input | Type | Description |
|-------|------|-------------|
| `~/odometry/raw` | nav_msgs/msg/Odometry | Raw Odometry Data from the robot |
| `~/IMU/raw` | sensor_msgs/msg/Imu | Raw IMU data | 

|Output | Type | Description |
|-------|------|-------------|
| `~/odometry/filtered` | nav_msgs/msg/Odometry | Processed Odometry Data |