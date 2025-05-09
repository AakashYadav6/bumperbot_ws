from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():

    # Get path to xacro file
    xacro_file = os.path.join(
        get_package_share_directory("bumperbot_description"),
        "urdf",
        "bumperbot.urdf.xacro"
    )

    # Process xacro file into a URDF XML string
    robot_description_config = xacro.process_file(xacro_file).toxml()

    # Robot State Publisher node
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description_config}]
    )

    # Joint State Publisher GUI
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    # RViz Node
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(
            get_package_share_directory("bumperbot_description"),
            "rviz2",
            "display.rviz"
        )]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz_node
    ])
