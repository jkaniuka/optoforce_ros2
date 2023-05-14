# ROS 2 wrapper for Optoforce 3-axis force sensor (OMD-20-FE-200N)

## Requirements: 
```
pip3 install optoforce
```

## TODO:

- [ ] rqt_plot
- [ ] add Wrench visualization in RViz
- [ ] test both launch files
- [ ] how to determine serial ports?
- [] check if publish rate is appropriate

[OptoForce custom DAQ specification - SPI](http://www.cs.cmu.edu/~cga/optoforce/optoforce-spi.pdf)
[optoforce Python library](https://pypi.org/project/optoforce/)

1. Change parameters values in `config/optoforce_params.yaml`
2. Sensor specification you will find in `docs` directory.
3. Test sensor and visualize force in Rviz -> `ros2 launch optoforce_wrapper optoforce_test.launch.py`
4. Read data from sensor(-s) -> `ros2 launch optoforce_wrapper optoforce_read.launch.py`
5. In 2018, Optoforce was acquired by OnRobot. 
6. Calibration data to convert the sensor's readings into force expressed in Newtons can be found on the flash drive included with the sensor.  