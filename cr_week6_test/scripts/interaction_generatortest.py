#!/usr/bin/env python

import rospy
import numpy as np
import random as ra
from cr_week6_test.msg import object_info
from cr_week6_test.msg import human_info

objectinfo = None
humaninfo = None

def node_1():
        
	global objectinfo
	global humaninfo
	objectinfo = object_info()
	humaninfo = human_info()	
	id = objectinfo.id
	
	rospy.init_node('interaction_generator', anonymous=True) 
 	pub = rospy.Publisher('object_info', object_info, queue_size=10)
	pub1 = rospy.Publisher('human_info', human_info, queue_size=10)

	try:
			
		while not rospy.is_shutdown():
	
			objectinfo.object_size= ra.randint(1,2)
			humaninfo.human_action = ra.randint(1,3)
			humaninfo.human_expression = ra.randint(1,3)
			for id in range(1, 10, 1):
                		print(id)
			
				humaninfo.id = id
				objectinfo.id = id	
				pub.publish(objectinfo)
				pub1.publish(humaninfo)
				rate = rospy.Rate(0.1) # Publish every 10s
				rospy.loginfo(humaninfo)
				rospy.loginfo(objectinfo)
				rate.sleep()

	except KeyboardInterrupt:
		pass

if __name__ == "__main__" :
	try:
		node = node_1()
	except rospy.ROSInterruptException: pass

