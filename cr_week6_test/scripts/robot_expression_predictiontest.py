#!/usr/bin/env python

import rospy
import numpy as np
import random as ra
import imp; imp.find_module('bayesian_belief_networks')

from cr_week6_test.srv import predict_robot_expression,predict_robot_expressionResponse
from cr_week6_test.msg import perceived_info


p_happy=None
p_sad=None
p_neutral=None
re_happyprob=None
re_sadprob=None
re_neutralprob=None
o_size=None
h_action=None
h_expression = None
info = perceived_info()

def callback1(perceivedinfo):
	global info
	
	info = perceivedinfo

def re_sad(o_size,h_action,h_expression):
	global re_happyprob,re_sadprob,re_neutralprob

	if h_expression ==1 and h_action==1 and o_size ==1:
		re_sadprob = 0.2
	elif h_expression ==1 and h_action==1 and o_size ==2: 
                re_sadprob = 0.0
	elif h_expression ==1 and h_action==2 and o_size ==1: 
                re_sadprob = 0.2  
 	elif h_expression ==1 and h_action==2 and o_size ==2: 
                re_sadprob = 0.0
	elif h_expression ==1 and h_action==3 and o_size ==1: 
                re_sadprob = 0.2
	elif h_expression ==1 and h_action==3 and o_size ==2: 
                re_sadprob = 0.2
	elif h_expression ==2 and h_action==1 and o_size ==1: 
                re_sadprob = 0.0
	elif h_expression ==2 and h_action==1 and o_size ==2: 
                re_sadprob = 0.0
	elif h_expression ==2 and h_action==2 and o_size ==1: 
                re_sadprob = 0.1
	elif h_expression ==2 and h_action==2 and o_size ==2: 
                re_sadprob = 0.1
	elif h_expression ==2 and h_action==3 and o_size ==1: 
                re_sadprob = 0.2
	elif h_expression ==2 and h_action==3 and o_size ==2: 
                re_sadprob = 0.2
	elif h_expression ==3 and h_action==1 and o_size ==1: 
                re_sadprob = 0.3
	elif h_expression ==3 and h_action==1 and o_size ==2: 
                re_sadprob = 0.2
	elif h_expression ==3 and h_action==2 and o_size ==1: 
                re_sadprob = 0.2
	elif h_expression ==3 and h_action==2 and o_size ==2: 
                re_sadprob = 0.1
	elif h_expression ==3 and h_action==3 and o_size ==1: 
                re_sadprob = 0.2
	elif h_expression ==3 and h_action==3 and o_size ==2: 
                re_sadprob = 0.2
	elif h_expression == 0 or h_action ==0 or o_size ==0:
		re_sadprob =1.0/3
	else:
		re_sadprob = 1.0/3
	return re_sadprob
	
def re_happy(o_size,h_action,h_expression):
	global re_happyprob,re_sadprob,re_neutralprob


	if h_expression ==1 and h_action==1 and o_size ==1:
                re_happyprob = 0.8
        elif h_expression ==1 and h_action==1 and o_size ==2: 
                re_happyprob = 1
        elif h_expression ==1 and h_action==2 and o_size ==1: 
                re_happyprob = 0.8  
        elif h_expression ==1 and h_action==2 and o_size ==2: 
                re_happyprob = 1
        elif h_expression ==1 and h_action==3 and o_size ==1: 
                re_happyprob = 0.6
        elif h_expression ==1 and h_action==3 and o_size ==2: 
                re_happyprob = 0.8
        elif h_expression ==2 and h_action==1 and o_size ==1: 
                re_happyprob = 0.0
        elif h_expression ==2 and h_action==1 and o_size ==2: 
                re_happyprob = 0.0
        elif h_expression ==2 and h_action==2 and o_size ==1: 
                re_happyprob = 0.0
        elif h_expression ==2 and h_action==2 and o_size ==2: 
                re_happyprob = 0.1
        elif h_expression ==2 and h_action==3 and o_size ==1: 
                re_happyprob = 0.0
        elif h_expression ==2 and h_action==3 and o_size ==2: 
                re_happyprob = 0.2
        elif h_expression ==3 and h_action==1 and o_size ==1: 
                re_happyprob = 0.7
        elif h_expression ==3 and h_action==1 and o_size ==2: 
                re_happyprob = 0.8
        elif h_expression ==3 and h_action==2 and o_size ==1: 
                re_happyprob = 0.8
        elif h_expression ==3 and h_action==2 and o_size ==2: 
                re_happyprob = 0.9
        elif h_expression ==3 and h_action==3 and o_size ==1: 
                re_happyprob = 0.6
        elif h_expression ==3 and h_action==3 and o_size ==2: 
                re_happyprob = 0.7
	elif h_expression == 0 or h_action ==0 or o_size ==0:
                re_happyprob =1.0/3

	else:
		re_happyprob = 1.0/3
	return re_happyprob
	
def re_neutral(o_size,h_action,h_expression):
        global re_happyprob,re_sadprob,re_neutralprob

	if h_expression ==1 and h_action==1 and o_size ==1:
                re_neutralprob = 0.0
        elif h_expression ==1 and h_action==1 and o_size ==2: 
                re_neutralprob = 0.0
        elif h_expression ==1 and h_action==2 and o_size ==1: 
                re_neutralprob = 0.0  
        elif h_expression ==1 and h_action==2 and o_size ==2: 
                re_neutralprob = 0.0
        elif h_expression ==1 and h_action==3 and o_size ==1: 
                re_neutralprob = 0.2
        elif h_expression ==1 and h_action==3 and o_size ==2: 
                re_neutralrob = 0.0
        elif h_expression ==2 and h_action==1 and o_size ==1: 
                re_neutralrob = 1
        elif h_expression ==2 and h_action==1 and o_size ==2: 
                re_neutralprob = 1  
        elif h_expression ==2 and h_action==2 and o_size ==1: 
                re_neitralprob = 0.9
        elif h_expression ==2 and h_action==2 and o_size ==2: 
                re_neutralprob = 0.8
        elif h_expression ==2 and h_action==3 and o_size ==1: 
                re_neutralprob = 0.8
        elif h_expression ==2 and h_action==3 and o_size ==2: 
                re_neutralprob = 0.6
        elif h_expression ==3 and h_action==1 and o_size ==1: 
                re_neutralprob = 0.0
        elif h_expression ==3 and h_action==1 and o_size ==2: 
                re_neutralprob = 0.0
        elif h_expression ==3 and h_action==2 and o_size ==1: 
                re_neutralprob = 0.0
        elif h_expression ==3 and h_action==2 and o_size ==2: 
                re_neutralprob = 0.0
        elif h_expression ==3 and h_action==3 and o_size ==1: 
		 re_neutralprob = 0.2
        elif h_expression ==3 and h_action==3 and o_size ==2: 
                re_neutralprob = 0.1
	elif h_expression == 0 or h_action ==0 or o_size ==0:
                re_neutralprob =(1.0/3)

	else:
		re_neutralprob = 1.0/3
        return re_neutralprob


def f_prob(info):
	global o_size, h_action, h_expression
	o_size = info.object_size
        h_action = info.human_action 
        h_expression = info.human_expression 

	re_happy(o_size,h_action,h_expression)
        re_sad(o_size,h_action,h_expression)
        re_neutral(o_size,h_action,h_expression) 

	

	return re_happyprob,re_sadprob, re_neutralprob
def f_predict_robot_expression(perceivedinfo):
	
	global p_happy,p_sad,p_neutral,info, re_happyprob,re_sadprob,re_neutralprob, o_size, h_action, h_expression
	f_prob(info)
	
	return predict_robot_expressionResponse(	
		p_happy = re_happyprob,
		p_sad = re_sadprob,
		p_neutral = re_neutralprob
	)
	
	
	

if __name__ == "__main__":

	rospy.init_node('Robot_expression_prediction')
	
	

        sub = rospy.Subscriber("perceived_info", perceived_info, callback1, queue_size =10)
	s = rospy.Service('Robot_expression_prediction', predict_robot_expression, f_predict_robot_expression)

	rospy.spin()

