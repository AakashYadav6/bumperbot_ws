#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class SimpleTurtlesimKinematics(Node):
    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")

        self.turtlesim1_pose_sub_ = self.create_subscription(
            Pose, "/turtle1/pose", self.turtle1PoseCallback, 10)
        self.turtlesim2_pose_sub_ = self.create_subscription(
            Pose, "/turtle2/pose", self.turtle2PoseCallback, 10)

        self.last_turtle1_pose_ = None
        self.last_turtle2_pose_ = None

    def turtle1PoseCallback(self, msg):
        self.last_turtle1_pose_ = msg

    def turtle2PoseCallback(self, msg):
        self.last_turtle2_pose_ = msg

        # Only compute if we have both poses
        if self.last_turtle1_pose_ is not None:
            Tx = self.last_turtle2_pose_.x - self.last_turtle1_pose_.x
            Ty = self.last_turtle2_pose_.y - self.last_turtle1_pose_.y

            self.get_logger().info(
                f"\nTranslation vector turtle1 -> turtle2\nTx: {Tx:.2f}, Ty: {Ty:.2f}"
            )


def main():
    rclpy.init()
    simple_turtlesim_kinematics = SimpleTurtlesimKinematics()
    rclpy.spin(simple_turtlesim_kinematics)
    simple_turtlesim_kinematics.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
