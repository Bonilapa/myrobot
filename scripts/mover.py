#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from datetime import datetime

def mover():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('mover', anonymous=True)
    rate = rospy.Rate(30) # 30hz
    move = JointState()
    move.name = ['base_to_1_link', '1_to_2_link', '2_to_3_joint_link']
    jb1pos = 0.0
    j12pos = 0.0
    j23pos = 0.0
    jb1 = True
    j12 = True
    j23 = True
    while not rospy.is_shutdown():
        move.header.stamp = rospy.Time.now()
        rospy.loginfo(str(move))
        move.position = [jb1pos, j12pos, j23pos]
        if jb1:
            jb1pos += 0.1
            if jb1pos >= 5:
                jb1 = False
        else:
            jb1pos -= 0.1
            if jb1pos <= 0.5:
                jb1 = True
        if j12:
            j12pos -= 0.1
            if j12pos <= -4.5:
                j12 = False   
        else:
            j12pos += 0.1
            if j12pos >= 0:
                j12 = True
        if j23:
            j23pos += 0.1
            if j23pos >= 3.14:
                j23 = False
        else:
            j23pos -= 0.1
            if j23pos <= -3.14:
                j23 = True
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
