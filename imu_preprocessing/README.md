# IMU_PREPROCESSING

A Sensor Fusion packge to fuse 2 `IMU Sensors` to output a more clean `IMUData`.

| Input | Type | Description |
|-------|------|-------------|
| `~/IMU/raw_0`| sensor_msgs/msg/Imu | Raw IMU data 0 | 
| `~/IMU/raw_1`| sensor_msgs/msg/Imu | Raw IMU data 1 | 

|Output | Type | Description |
|-------|------|-------------|
| `~/IMU/processed`| sensor_msgs/msg/Imu | Processed IMU data | 