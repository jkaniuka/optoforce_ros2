# ROS 2 wrapper for Optoforce 3-axis force sensor 

<h2 align="center">:warning: Tested with OMD-20-FE-200N 3-axis force sensor </h2> 
<p align="center">
<img src="https://github.com/jkaniuka/optoforce_ros2/assets/80155305/b73e3afe-6a09-474e-b10f-f6044036163a" width="300" height="250"/><img src="https://github.com/jkaniuka/optoforce_ros2/assets/80155305/0613ee25-c7dd-4a0b-a397-db26d23fccf3" width="350" height="250"/>
</p> 

## Requirements: 
```
pip3 install optoforce
```

## Setup:
1. Check the name of the serial port into which your Optoforce sensor is plugged by using `python3 list_ports.py`.
2. Change the parameter values in `config/optoforce_params.yaml` file. Calibration data (_scale_ parameter) to convert the sensor's readings into force expressed in Newtons can be found on the flash drive included with the sensor.

3. Test sensor and visualize force in Rviz -> `ros2 launch optoforce_wrapper optoforce_test.launch.py`
4. Read data from sensor(-s) -> `ros2 launch optoforce_wrapper optoforce_read.launch.py`


6. In 2018, Optoforce was acquired by OnRobot. 

## Documentation:
- [**OptoForce custom DAQ specification - SPI**](http://www.cs.cmu.edu/~cga/optoforce/optoforce-spi.pdf)  
- [**_optoforce_ Python library**](https://pypi.org/project/optoforce/)


## TODO:

- [ ] rqt_plot
- [ ] RViz visualization
- [ ] test both sensors

