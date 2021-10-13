#!/usr/bin/env python

import rospy
import numpy as np
import random as ra
import imp; imp.find_module('bayesian_belief_networks')
from cr_week6_test.srv import predict_robot_expression, predict_robot_expressionRequest
from cr_week6_test.msg import perceived_info
from cr_week6_test.msg import robot_info

probs = robot_info()

def node_3(perceivedinfo):
	global probs
	rospy.wait_for_service('Robot_expression_prediction')
	try:
		predict_expression = rospy.ServiceProxy('Robot_expression_prediction', predict_robot_expression)
		print perceivedinfo
		robotinfo = predict_robot_expressionRequest(perceivedinfo.object_size,perceivedinfo.human_action,perceivedinfo.human_expression)
		
		prob = predict_expression(robotinfo)
		probs.id = perceivedinfo.id
		probs.p_happy = prob.p_happy
		probs.p_sad = prob.p_sad
		probs.p_neutral = prob.p_neutral
		return probs

	except rospy.ServiceException as e:
		print("Service call failed")






if __name__ == '__main__':
        try:

                rospy.init_node('robot_controller', anonymous=True)
		
		pub = rospy.Publisher("robot_info", robot_info, queue_size=10)
                sub = rospy.Subscriber("perceived_info", perceived_info, node_3, queue_size =10)

		while not rospy.is_shutdown():

                        rate=rospy.Rate(0.1) #0.05Hz
                        pub.publish(probs)
			rospy.loginfo(probs)
                        rate.sleep()
	except rospy.ROSInterruptException:
                pass



