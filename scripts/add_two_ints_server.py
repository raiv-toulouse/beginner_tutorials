#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):  # When the service is called
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))  # Get the two parameters from the message 
    return AddTwoIntsResponse(req.a + req.b)  # and sends the result message

if __name__ == "__main__":
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints) # Launch the service
    print("Ready to add two ints.")
    rospy.spin()  # Wait indefinitely

