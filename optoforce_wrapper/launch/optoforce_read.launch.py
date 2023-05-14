import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    optoforce_params = os.path.join(
        get_package_share_directory('optoforce_wrapper'),
        'config',
        'optoforce_params.yaml'
        )
        
    optoforce_node = Node(
        package = 'optoforce_wrapper',
        executable = 'optoforce_node',
        parameters = [optoforce_params]
    )

    return LaunchDescription([
        optoforce_node
    ])