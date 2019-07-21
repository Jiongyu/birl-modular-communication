#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from os import getcwd
# print getcwd()

from rospkg import RosPack
rp = RosPack()
import sys
sys.path.append(rp.get_path('canopen_communication') + "/robot/")

from arm5d import Arm5d
import time
import pdb

def main():
    eds_file = 'Copley.eds'
    manipulater = Arm5d(eds_file)
    #pdb.set_trace()
    manipulater.start()

    print 'position mode'
    manipulater.set_mode(1)
    position = [0,0,0,0.2,0.2]

    manipulater.sent_joint_position(position)
    while manipulater.get_position()[3] < 0.2 or manipulater.get_position()[4] < 0.2:

        print 'actual motor_i4 position: %f rad' % manipulater.get_position()[3]
        print 'actual motor_t5 position: %f rad' % manipulater.get_position()[4]
        print "<---------------------------------------------------->"   
        manipulater.sent_joint_position(position)

    position = [0,0,0,0,0]
    manipulater.sent_joint_position(position)
    while manipulater.get_position()[3] > 0 or manipulater.get_position()[4] > 0:

        print 'actual motor_i4 position: %f rad' % manipulater.get_position()[3]
        print 'actual motor_t5 position: %f rad' % manipulater.get_position()[4] 
        print "<---------------------------------------------------->"    
        manipulater.sent_joint_position(position)
    time.sleep(5)

    print 'velocity mode'
    manipulater.set_mode(3)
    velocity = [0,0,0,0.02,0.02]
    manipulater.sent_joint_velocity(velocity)
    while(manipulater.get_position()[3] < 0.5 and manipulater.get_position()[4]<0.5):

        print 'actual motor_i4 velocity: %f rad/s' % manipulater.get_velocity()[3]
        print 'actual motor_t5 velocity: %f rad/s' % manipulater.get_velocity()[4]
        manipulater.sent_joint_velocity(velocity)

    velocity = [0,0,0,-0.03,-0.03]
    manipulater.sent_joint_velocity(velocity)

    while(manipulater.get_position()[3] > 0 and manipulater.get_position()[4] > 0):

        print 'actual motor_i4 velocity: %f rad/s' % manipulater.get_velocity()[3]
        print 'actual motor_t5 velocity: %f rad/s' % manipulater.get_velocity()[4]
        manipulater.sent_joint_velocity(velocity)
        
    velocity = [0,0,0,0,0]
    manipulater.sent_joint_velocity(velocity)
    time.sleep(5)
    
    manipulater.stop()


if __name__ == "__main__":
    main()