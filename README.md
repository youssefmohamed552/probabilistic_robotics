# README `Probabilistic Robotics`

## Simulator
run the gazebo simulator

### install 
follow the link https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/
or run
- `sudo apt-get install ros-noetic-dynamixel-sdk`
- `sudo apt-get install ros-noetic-turtlebot3-msgs`
- `sudo apt-get install ros-noetic-turtlebot3`
- for the `burger` model `echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc`
- for the `waffle_pi` model `echo "export TURTLEBOT3_MODEL=waffle_pi" >> ~/.bashrc`
- `source ~/.bashrc`

### run turtlebot gazebo 
follow the link https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/
or run
- `cd ~/catkin_ws/src/`
- `git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`
- `cd ~/catkin_ws && catkin_make`
- `roslaunch turtlebot3_gazebo turtlebot3_house.launch`

## Visualization
to visualize on gazebo and get all the rostopics visualized properly `roslaunch turtlebot3_gazebo turtlebot3_gazebo_rvis.launch`

## Debugging tools
### rosbag
- `rosbag record <topic> ..`
- `rosbag play <recording-file>`
- `rosbag info <recording-file>`
