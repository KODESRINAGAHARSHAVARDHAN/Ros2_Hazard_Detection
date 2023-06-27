# ROS2 HAZARD DETECTION USING  MOBILE ROBOT 
Ros2 humble project and  gazebo simulation . Detecting  whether the object is hazard 

# Novality 
      Detecting the objects weather it is hazardious or not 

This project aims to develop a mobile robot that can detect hazards in its environment using a camera and take appropriate actions using opencv and detect those hazards.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

In today's world, robots are being increasingly used in various applications, including hazardous environments where human presence may be dangerous or impractical. This project focuses on developing a mobile robot capable of detecting potential hazards, such as obstacles, cliffs, or moving objects, and reacting accordingly.

The robot will be equipped with a combination of sensors, such as LiDAR, cameras, and inertial measurement units (IMUs), to perceive its surroundings. Using advanced algorithms and machine learning techniques, the robot will analyze the sensor data in real-time to identify potential hazards and determine the appropriate course of action.

## Features
- Real-time hazard detection using Camera 
- object clasification using openvc
- Integration with ros2 and simulation in Gazebo 
- Extensibility and modularity for adding new sensors or features

## Installation

To install and set up the project, follow these steps:
Clone the repository:

   git clone https://github.com/your-username/hazard-detection-mobile-robot.git

STEP1:-
At first we need to do colcon build in the workspace. If this is successfull we will proceed furthur.
STEP2:-
Next we need to run the launch file using the command ros2 launch <package_name> <script_name>
STEP3:-
When we are running this code gazebo will run and for movementwe need to run teleop twist keyboard. To run this we need to give the command ros2 run teleop_twist_keyboad teleop_twist_keyboard
STEP4:-
After moving the robot, open the rviz using the command rviz2 in new terminal. Add the Image(by_topic) in bottom left.
STEP5:-
In the image the object detection using the opencv. we need to open new terminal and see all the topics by using the command ros2 topic list
STEP6:-
At last we need echo the topic /weapon_alert using the command ros2 topic echo <topic_name>. when given input object is scaned by camera it gives an alert as weapon detected!. 

## Usage:
For Detecting the Hazard Object in the Environment
Execution of code metioned above as Video
