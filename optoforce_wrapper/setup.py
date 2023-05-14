from setuptools import setup
import os
from glob import glob

package_name = 'optoforce_wrapper'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'model'), glob('model/*.*')),
        (os.path.join('share', package_name, 'rviz') , glob('rviz/*.*')),
        (os.path.join('share', package_name, 'meshes') , glob('meshes/*.*')),
        (os.path.join('share', package_name, 'config') , glob('config/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jan Kaniuka',
    maintainer_email='jasiek491@gmail.com',
    description='ROS 2 wrapper for Optoforce 3-axis force sensor.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "optoforce_node = optoforce_wrapper.optoforce_node:main"
        ],
    },
)
