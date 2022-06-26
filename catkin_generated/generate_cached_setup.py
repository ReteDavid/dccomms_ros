# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/david/catkin_ws/install_isolated;/home/david/catkin_ws/devel_isolated/gscam;/home/david/catkin_ws/devel_isolated/uwsim;/home/david/catkin_ws/devel_isolated/uuv_world_ros_plugins;/home/david/catkin_ws/devel_isolated/uuv_world_ros_plugins_msgs;/home/david/catkin_ws/devel_isolated/uuv_world_plugins;/home/david/catkin_ws/devel_isolated/uuv_tutorials;/home/david/catkin_ws/devel_isolated/uuv_tutorial_seabed_world;/home/david/catkin_ws/devel_isolated/uuv_tutorial_dp_controller;/home/david/catkin_ws/devel_isolated/uuv_tutorial_disturbances;/home/david/catkin_ws/devel_isolated/uuv_trajectory_control;/home/david/catkin_ws/devel_isolated/uuv_thruster_manager;/home/david/catkin_ws/devel_isolated/uuv_teleop;/home/david/catkin_ws/devel_isolated/uuv_simulator;/home/david/catkin_ws/devel_isolated/uuv_sensor_ros_plugins;/home/david/catkin_ws/devel_isolated/uuv_sensor_ros_plugins_msgs;/home/david/catkin_ws/devel_isolated/uuv_gazebo_worlds;/home/david/catkin_ws/devel_isolated/uuv_gazebo_ros_plugins;/home/david/catkin_ws/devel_isolated/uuv_gazebo_ros_plugins_msgs;/home/david/catkin_ws/devel_isolated/uuv_gazebo_plugins;/home/david/catkin_ws/devel_isolated/uuv_gazebo;/home/david/catkin_ws/devel_isolated/uuv_descriptions;/home/david/catkin_ws/devel_isolated/uuv_control_utils;/home/david/catkin_ws/devel_isolated/uuv_control_msgs;/home/david/catkin_ws/devel_isolated/uuv_control_cascaded_pid;/home/david/catkin_ws/devel_isolated/uuv_auv_control_allocator;/home/david/catkin_ws/devel_isolated/uuv_assistants;/home/david/catkin_ws/devel_isolated/underwater_vehicle_dynamics;/home/david/catkin_ws/devel_isolated/underwater_sensor_msgs;/home/david/catkin_ws/devel_isolated/test_mavros;/home/david/catkin_ws/devel_isolated/slider_publisher;/home/david/catkin_ws/devel_isolated/mavros_extras;/home/david/catkin_ws/devel_isolated/bluerov_ros_playground;/home/david/catkin_ws/devel_isolated/bluerov2_control;/home/david/catkin_ws/devel_isolated/mavros;/home/david/catkin_ws/devel_isolated/mavros_msgs;/home/david/catkin_ws/devel_isolated/libmavconn;/home/david/catkin_ws/devel_isolated/freefloating_gazebo_demo;/home/david/catkin_ws/devel_isolated/freefloating_gazebo;/home/david/catkin_ws/devel_isolated/bluerov_ffg;/home/david/catkin_ws/devel_isolated/bluerov2_gazebo;/home/david/catkin_ws/devel_isolated/bluerov2_description;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/david/catkin_ws/devel_isolated/uwsim/env.sh')

output_filename = '/home/david/catkin_ws/build_isolated/uwsim/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
