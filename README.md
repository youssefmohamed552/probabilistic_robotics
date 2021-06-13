# README `Probabilistic Robotics`

## Simulator
run the gazebo simulator

### install 
follow the link https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/
or run
- `sudo apt-get install ros-noetic-dynamixel-sdk`
- `sudo apt-get install ros-noetic-turtlebot3-msgs`
- `sudo apt-get install ros-noetic-turtlebot3`
- `echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc`
- `source ~/.bashrc`

### run turtlebot gazebo 
follow the link https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/
or run
- `cd ~/catkin_ws/src/`
- `git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`
- `cd ~/catkin_ws && catkin_make`
- `roslaunch turtlebot3_gazebo turtlebot3_house.launch`
