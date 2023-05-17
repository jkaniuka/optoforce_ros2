# ROS 2 wrapper for Optoforce 3-axis force sensor 

<h2 align="center">:warning: Tested on OMD-20-FE-200N 3-axis force sensor :warning:</h2> 
<p align="center">
<img src="https://github.com/jkaniuka/optoforce_ros2/assets/80155305/cc192693-7ba9-4b0f-b7db-6b59ea8c70b8" width="350" height="300"/>        <img src="https://github.com/jkaniuka/optoforce_ros2/assets/80155305/fc0aaf77-cd6f-47e9-9d28-0a5eab07a767" width="400" height="300"/>
</p> 



## Requirements :arrow_down:
```
pip3 install optoforce
```

## Setup :arrow_forward:
1. Check the name of the serial port into which your Optoforce sensor is plugged by using `python3 list_ports.py`.
2. Change the parameters values in **config/optoforce_params.yaml** file. Calibration data (_scale_ parameter) to convert the sensor's readings into force expressed in Newtons can be found on the flash drive that comes with the sensor.
3. Verify that the sensor is working properly by running `ros2 launch optoforce_wrapper optoforce_test.launch.py`. In RViz, the sensor model and force readings (as _geometry_msgs/msg/WrenchStamped_ messages) will be visualized.
4. To read the measurements from the sensor(-s) you need to run _optoforce_node_ node and load the parameters from the YAML file. Use the following command:
```
ros2 launch optoforce_wrapper optoforce_read.launch.py
```

## Documentation :spiral_notepad:
- [**OptoForce custom DAQ specification - SPI**](http://www.cs.cmu.edu/~cga/optoforce/optoforce-spi.pdf)  
- [**_optoforce_ Python library**](https://pypi.org/project/optoforce/)

## Good to know :detective:
In 2018, Optoforce was acquired by [**OnRobot**](https://onrobot.com/pl). The links to Optoforce's website redirect to Onrobot's website, where the **Page not found (404)** error appears, so don't be surprised :wink:

## TODO:

- [ ] RViz visualization

