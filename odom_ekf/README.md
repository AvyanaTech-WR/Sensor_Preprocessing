# ODOM_EKF

A Sensor Fusion packge to fuse `Odom Data` and `IMU Data`, to output a more clean `Odom Data`.

| Input | Type | Description |
|-------|------|-------------|
| `~/odom/raw` | nav_msgs/msg/Odometry | Raw Odometry Data from the robot |
| `/IMU/processed` | sensor_msgs/msg/Imu | Raw IMU data | 

|Output | Type | Description |
|-------|------|-------------|
| `~/odom/processed` | nav_msgs/msg/Odometry | Processed Odometry Data |