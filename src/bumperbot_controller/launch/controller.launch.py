import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.parameter_descriptions import ParameterValue
from launch.conditions import UnlessCondition


def generate_launch_description():

    bumperbot_description = get_package_share_directory("bumperbot_description")
    bumperbot_controller = get_package_share_directory("bumperbot_controller")

    model_arg = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(
            bumperbot_description, "urdf", "bumperbot.urdf.xacro"
        ),
        description="Absolute path to robot URDF file",
    )
    use_python_arg = DeclareLaunchArgument(
        "use_python",
        default_value="False"
    )

    wheel_radius_arg =DeclareLaunchArgument(
        "wheel_radius",
        default_value="0.033"

    )

    wheel_separation_arg = DeclareLaunchArgument(
        "wheel_separation",
        default_value= "0.17"
    )

    use_python = LaunchConfiguration("use_python")
    wheel_radius = LaunchConfiguration("wheel_radius")
    wheel_separation = LaunchConfiguration("wheel_separation")




    robot_description = ParameterValue(
        Command([
            "xacro ",
            LaunchConfiguration("model")
        ]),
        value_type=str,
    )

    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[
            {"robot_description": robot_description},
            os.path.join(bumperbot_controller, "config", "bumperbot_controllers.yaml"),
        ],
        output="screen",
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    simple_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "simple_velocity_controller",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    simple_controller_py =Node(
        package="bumperbot_controller",
        executable="simple_controller.py",
        parameters=[{"wheel_radius":wheel_radius,
                     "wheel_separation":wheel_separation}]
    )
    simple_controller_cpp =Node(
        package="bumperbot_controller",
        executable="simple_controller",
        parameters=[{"wheel_radius":wheel_radius,
                     "wheel_separation":wheel_separation}],
        condition=UnlessCondition(use_python)



    )
    

    return LaunchDescription(
        [
            model_arg,
            use_python_arg,
            wheel_radius_arg,
            wheel_separation_arg,
            controller_manager_node,
            joint_state_broadcaster_spawner,
            simple_controller_spawner,
            simple_controller_py,
            simple_controller_cpp
        ]
    )
