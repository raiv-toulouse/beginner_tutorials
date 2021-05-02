#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        service_add = rospy.ServiceProxy('add_two_ints', AddTwoInts)  # Call the service
        resp = service_add(x, y)  # Receive the response message
        return resp.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
