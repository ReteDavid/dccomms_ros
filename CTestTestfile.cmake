# CMake generated Testfile for 
# Source directory: /home/david/catkin_ws/src/underwater_simulation/uwsim
# Build directory: /home/david/catkin_ws/build_isolated/uwsim
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_uwsim_roslaunch-check_data_scenes_launch "/home/david/catkin_ws/build_isolated/uwsim/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/david/catkin_ws/build_isolated/uwsim/test_results/uwsim/roslaunch-check_data_scenes_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/david/catkin_ws/build_isolated/uwsim/test_results/uwsim" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/david/catkin_ws/build_isolated/uwsim/test_results/uwsim/roslaunch-check_data_scenes_launch.xml\" \"/home/david/catkin_ws/src/underwater_simulation/uwsim/data/scenes/launch\" ")
subdirs("gtest")
