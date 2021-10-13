#!/usr/bin/env python

import rospy
import numpy as np
import random as ra
from cr_week6_test.msg import object_info
from cr_week6_test.msg import human_info
from cr_week6_test.msg import perceived_info

perceivedinfo = perceived_info()
def callback1(objectinfo):
	global perceivedinfo
	perceivedinfo.id = objectinfo.id
	perceivedinfo.object_size = objectinfo.object_size
	

def callback2(humaninfo):
	global perceivedinfo
	perceivedinfo.human_action = humaninfo.human_action 
	perceivedinfo.human_expression = humaninfo.human_expression


def node_2():
	global perceivedinfo
	
	modvar = ra.randint(1,8)
	print(modvar)
	if modvar == 1:
		perceivedinfo.object_size = 0
		print("Object size not perceived")
	elif modvar ==2:
		perceivedinfo.human_action=0
		print("Human action not perceived")
	elif modvar ==3:
		perceivedinfo.human_expression=0
		print("Human expression not perceived")
	elif modvar ==4:
		perceivedinfo.object_size=0
		perceivedinfo.human_action =0
		print("Object size and human action not perceived")
	elif modvar ==5:
		perceivedinfo.object_size=0
		perceivedinfo.human_expression =0
		print("Object size and human expression not perceived")

	elif modvar ==6:
		perceivedinfo.human_expression=0
		perceivedinfo.human_action =0
		print("Human expression and human action not perceived")

	elif modvar ==7:
		perceivedinfo.object_size=0
		perceivedinfo.human_action=0
		perceivedinfo.human_expression =0
		print("Object size, human expression and human action not perceived")

	elif modvar ==8:
		print ("No Modifications")

	rospy.loginfo(perceivedinfo)



if __name__ == '__main__':
	try:

		rospy.init_node('perception_filter', anonymous=True)

                pub = rospy.Publisher("perceived_info", perceived_info, queue_size=10)
		sub = rospy.Subscriber("object_info", object_info, callback1, queue_size =10)
		sub2 = rospy.Subscriber("human_info", human_info, callback2, queue_size=10)
		while not rospy.is_shutdown():

			node_2()
			rate=rospy.Rate(0.1) #0.05Hz
			pub.publish(perceivedinfo)
			rate.sleep()
				
		


	except rospy.ROSInterruptException:
		pass

