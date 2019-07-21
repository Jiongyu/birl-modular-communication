#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rospkg import RosPack
rp = RosPack()
import sys
sys.path.append(rp.get_path('canopen_communication') + "/modular/")

import pdb

from modular_I100 import I100
from modular_T100 import T100
from modular_T85 import T85
from modular_I85 import I85 

class Arm5d(object):

    def __init__(self,eds_file):
        self.eds_file = eds_file
        self.I1 = I100(1,self.eds_file)
        self.T2 = T100(2,self.eds_file)
        self.T3 = T100(3,self.eds_file)
        self.i4 = I85(4,self.eds_file)
        self.t5 = T85(5,self.eds_file)

    def start(self):

        self.I1.start()
        self.T2.start()
        self.T3.start()
        self.i4.start()
        self.t5.start()

    def set_mode(self,mode):

        self.mode = mode
        self.I1.set_mode(self.mode)
        self.T2.set_mode(self.mode)
        self.T3.set_mode(self.mode)
        self.i4.set_mode(self.mode)
        self.t5.set_mode(self.mode)


    def sent_joint_position(self,position,velocity = [0.02,0.02,0.02,0.02,0.02]):

        if self.mode == 1:
            self.I1.sent_position(position[0], velocity[0])
            self.T2.sent_position(position[1], velocity[1])
            self.T3.sent_position(position[2], velocity[2])
            self.i4.sent_position(position[3], velocity[3])
            self.t5.sent_position(position[4], velocity[4])


    def sent_joint_velocity(self,velocity):
        """
        transfer velocity to control climb robot.
        :param velocity: control message
        """
        if self.mode == 3:
            self.I1.sent_velocity(velocity[0])
            self.T2.sent_velocity(velocity[1])
            self.T3.sent_velocity(velocity[2])
            self.i4.sent_velocity(velocity[3])
            self.t5.sent_velocity(velocity[4])

    def sent_joint_torque(self,torque):
        """
        transfer torque to control climb robot
        :param torque: control message
        """
        if self.mode == 4:
            self.I1.sent_torque(torque[0])
            self.T2.sent_torque(torque[1])
            self.T3.sent_torque(torque[2])
            self.i4.sent_torque(torque[3])
            self.t5.sent_torque(torque[4])

    def get_position(self):
        """
        get the every joint position (rad)
        :return turtle(position joint1 ,.....)
        """
        return (self.I1.get_position(),self.T2.get_position(),self.T3.get_position(),self.i4.get_position(),self.t5.get_position())


    def get_velocity(self):
        """
        get the every joint velocity (rad/s)
        :return (velocity joint1 ,.....)
        """
        return (self.I1.get_velocity(),self.T2.get_velocity(),self.T3.get_velocity(),self.i4.get_velocity(),self.t5.get_velocity())

    def get_torque(self):
        """
        get the every joint torque (# rate torque(mN.m) /1000)
        :return (torque joint1 ,.....)
        """
        return (self.I1.get_torque(),self.T2.get_torque(),self.T3.get_torque(),self.i4.get_torque(),self.t5.get_torque)


    def get_current(self):
        """
        get the every joint current (mA)
        :return (current joint1 ,.....)
        """
        return (self.I1.get_current(),self.T2.get_current(),self.T3.get_current(),self.i4.get_current(),self.t5.get_current())

    def stop(self):
        """
        stop the communication between climbot and canopen
        """
        self.I1.stop()
        self.T2.stop()
        self.T3.stop()
        self.i4.stop()
        self.t5.stop()
        print "stop the communication!"


    def quick_stop():
        self.I1.quick_stop()
        self.T2.quick_stop()
        self.T3.quick_stop()
        self.i4.quick_stop()
        self.t5.quick_stop()
