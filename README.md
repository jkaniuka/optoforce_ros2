# ROS 2 wrapper for Optoforce 3-axis force sensor 
## Sensor type: OMD-20-FE-200N
<img src="https://img.shields.io/badge/ros--version-humble-green"/>  <img src="https://img.shields.io/badge/platform%20-Ubuntu%2022.04-orange"/>

## Requirements: 
```
pip3 install optoforce
```

## TODO:

- [ ] rqt_plot
- [x] add Wrench visualization in RViz
- [x] test both launch files
- [x] how to determine serial ports?
- [x] check if publish rate is appropriate
- [ ] test both sensors

[OptoForce custom DAQ specification - SPI](http://www.cs.cmu.edu/~cga/optoforce/optoforce-spi.pdf)  
[optoforce Python library](https://pypi.org/project/optoforce/)

0. `python3 list_ports.py`
1. Change parameters values in `config/optoforce_params.yaml`
2. Sensor specification you will find in `docs` directory.
3. Test sensor and visualize force in Rviz -> `ros2 launch optoforce_wrapper optoforce_test.launch.py`
4. Read data from sensor(-s) -> `ros2 launch optoforce_wrapper optoforce_read.launch.py`
5. In 2018, Optoforce was acquired by OnRobot. 
6. Calibration data to convert the sensor's readings into force expressed in Newtons can be found on the flash drive included with the sensor.  
