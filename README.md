# ASV_ROS


|Reference|
|---------|
|[Dukciepond Website](https://robotx-nctu.github.io/duckiepond)|
|[David Chen's Website](https://championway.github.io)|

## Requirements Environment

- ROS kinetic
- Ubuntu 16.04
- OpenCV 3.3.1

## Sensors

|Name | Type |
|-------		|--------					|
|IMU		|???						|
|GPS			|???					|
|Depth sensors	|???						|

## How to Build
1. For ROS part
```
$ cd ~/
$ git clone https://github.com/championway/asv_ros.git
$ cd ~/asv_ros/catkin_ws
$ source ../environment.sh
$ catkin_make
```

Do the following everytime as you open new terminals
```
$ cd ~/asv_ros/
$ source environment.sh
```

## Multi-point Navigation
- cycle:=False --> The ASV will stop at the end point.
- cycle:=True --> The ASV will keep doing the cyle navigation.
- You can skip typing "veh:=[Your vehicle name]", your default name will be "ASV"

### Run Sensor
Open the sensor on the ASV, and make sure all the sensor ROS topics are publishing.
```
TODO
```

### Run Navigation
```
$ roslaunch asv navigation.launch cycle:=[True/False]
```

### Run Joystick
```
$ roslaunch asv joy.launch veh:=[Your vehicle name]
press "Start"
```
