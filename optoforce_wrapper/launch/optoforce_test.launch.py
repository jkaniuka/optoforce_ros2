import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

    display_model = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(
                                    Command(['xacro ', PathJoinSubstitution([get_package_share_directory('optoforce_wrapper'), "model", "optoforce_sensor.urdf"])]),
                                      value_type=str)
        }]
        )

    run_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(get_package_share_directory('optoforce_wrapper'), 'rviz', 'optoforce_rviz_config.rviz')]
        )
    

    static_tf_publisher = ExecuteProcess(
        cmd=[[
            'ros2 run tf2_ros static_transform_publisher ',
            '--z 0.017 --yaw 3.14159265359 ',
            '--frame-id sensor_link --child-frame-id frame_IFE048',
            ]],
        shell=True,
        )


    return LaunchDescription([
        display_model,
        run_rviz,
        static_tf_publisher
    ])