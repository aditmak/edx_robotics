#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def callback(data, pub):
    rospy.loginfo("SUM: {}".format(data.a+data.b))
    pub.publish(data.a + data.b)


def listener():
    rospy.init_node('solution')
    pub = rospy.Publisher("sum", Int16, queue_size=10)
    rospy.Subscriber("two_ints", TwoInts, callback, pub)

    rospy.spin()

if __name__=="__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
