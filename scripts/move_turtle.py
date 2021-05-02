#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def move():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('move_turtle', anonymous=True)
	tw_msg = Twist()
	tw_msg.linear.x = 2.0
	tw_msg.linear.y = 0.0
	tw_msg.linear.z = 0.0
	tw_msg.angular.x = 0.0
	tw_msg.angular.x = 0.0
	tw_msg.angular.x = 0.0
	rospy.sleep(1)
	pub.publish(tw_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
