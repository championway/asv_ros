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
g on...]()

## Installation

## How to Build (Software)
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

## How to Run


### Run Sensor
```
TODO
```

### Run Joystick
```
$ roslaunch asv joy.launch veh:=[Your vehicle name]
```

### Run Localization
```
$ roslaunch asv localizatin.launch
```

### Run Single Ponit Navigation
```
(TX2)
$ roslaunch duckiepond moos.launch sim:=false veh:=BRIAN moos_folder:=single_waypt
(TX2)
$ cd ~/duckiepond-nctu/moos/missions/single_waypt
$ ./launch_vehicle.sh -b
(LAPTOP)
$ cd ~/duckiepond-nctu/moos/missions/single_waypt
$ ./launch_shoreside.sh
```
