import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from picarx import Picarx



class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_to_pwm_callback, 10)
        self.px = Picarx()
        self.px.motor_direction_calibrate(1,1)
        self.px.motor_direction_calibrate(2,1)




    def cmd_to_pwm_callback (self, msg):
        right_wheel_vel = ( msg.linear.x + msg.angular.z) / 2
        left_wheel_vel = ( msg.linear.x - msg.angular.z ) / 2

        
        print(right_wheel_vel , "/" , left_wheel_vel)


        if(right_wheel_vel > 0 and left_wheel_vel > 0): # forward
            self.px.set_dir_servo_angle(0)
            self.px.forward(80)

        elif(right_wheel_vel > 0 and left_wheel_vel < 0):#left
            self.px.set_dir_servo_angle(-30)
            self.px.forward(80)

        elif(right_wheel_vel < 0 and left_wheel_vel > 0): #right
            self.px.set_dir_servo_angle(30)
            self.px.forward(80)

        elif(right_wheel_vel < 0 and left_wheel_vel < 0): #reverse
            self.px.set_dir_servo_angle(0)
            self.px.backward(80)

        elif(right_wheel_vel == 0 and left_wheel_vel == 0): #stop
            self.px.set_dir_servo_angle(0)
            self.px.forward(0)
            self.px.backward(0)



def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()