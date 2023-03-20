#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
from pynput import keyboard
from rclpy.node import Node

class Publicador(Node):

    def __init__(self):
        super().__init__('publicador')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = Twist()

        def press(key):
            movimiento = [0,0,0,0]
            linealspd = 2.0
            angularspd = 2.0
            if key.char == "s":
                movimiento[0] = -linealspd
            if key.char == "w":
                movimiento[0] = linealspd
            if key.char == "a":
                movimiento[1] = linealspd
            if key.char == "d":
                movimiento[1] = -linealspd
            if key.char == "c":
                movimiento[2] = linealspd
            if key.char == "z":
                movimiento[2] = -linealspd
            if key.char == "q":
                movimiento[3] = angularspd
            if key.char == "e":
                movimiento[3] = -angularspd
            
            msg.linear.x = float(movimiento[0])
            msg.linear.y = float(movimiento[1])
            msg.linear.z = float(movimiento[2])
            msg.angular.z = float(movimiento[3])
            print(movimiento)
            #msg.linear.y = movimiento["y"]
            #msg.angular.z = movimiento["z"]
        
            self.publisher_.publish(msg)

        def on_release(key):
            msg = Twist()
            self.publisher_.publish(msg)


        with keyboard.Listener(
            on_press=press, on_release=on_release) as listener:
                listener.join()



def main(args=None):
    rclpy.init(args=args)
    node = Publicador()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "_main_":
    main()