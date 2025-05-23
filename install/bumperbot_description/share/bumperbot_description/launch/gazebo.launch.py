import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    bumperbot_description = get_package_share_directory("bumperbot_description")

    model_arg = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(
            bumperbot_description, "urdf", "bumperbot.urdf.xacro"
        ),
        description="Absolute path to robot URDF file"
    )

    robot_description = ParameterValue(
        Command([
            "xacro ",
            LaunchConfiguration("model")
        ]),
        value_type=str
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "robot_description": robot_description,
            "use_sim_time": True
        }]
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        )
    )

    spawn_entity = Node(
       package="gazebo_ros",
       executable="spawn_entity.py",
       arguments=[
        "-topic", "robot_description",
        "-entity", "bumperbot",
        "-x", "0", "-y", "0", "-z", "1.0"  # Important!
       ],
       output="screen"
    )

    

    return LaunchDescription([
        model_arg,
        robot_state_publisher_node,
        gazebo,
        spawn_entity
    ])
