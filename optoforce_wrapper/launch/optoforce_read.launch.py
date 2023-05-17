import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

    num_of_sensors_in_use = DeclareLaunchArgument(name = 'num_of_sensors_in_use', default_value = '1', choices = ['1', '2'],
                                     description = 'If 1 use IFE048 sensor, if 2 use both IFE048 and IFE049 sensors.') 


    optoforce_params = os.path.join(
        get_package_share_directory('optoforce_wrapper'),
        'config',
        'optoforce_params.yaml'
        )
        
    optoforce_node = Node(
        package = 'optoforce_wrapper',
        executable = 'optoforce_node',
        parameters = [{"num_of_sensors_in_use" : LaunchConfiguration('num_of_sensors_in_use')}, optoforce_params]
    )

    return LaunchDescription([
        num_of_sensors_in_use,
        optoforce_node
    ])