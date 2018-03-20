This a a Bipedal test environment Usage:

first cd into this folder and do pip install -e . to install this environment

in your Python code, do

import gym 
import gym_bipedal

env = gym.make('Bipedal-v0')

Now, this re-creates the original Bipedal-v2 environment parameters.

To change the parameters do:

env.env.my_init(f=YOUR_FRICTION_VALUE) #these are the default params of the environment

where f=FRICTION 

This will change the corresponding values. 

You can choose to call my_init even every episode to change these parameters
