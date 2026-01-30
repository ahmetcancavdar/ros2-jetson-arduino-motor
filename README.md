# ROS 2 – Jetson – Arduino Motor Control

Motor control via serial communication to an Arduino UNO using a distributed ROS 2 Humble setup.
A ROS 2 node running on a PC publishes keyboard commands, which are received by a ROS 2 node running inside a Docker container on a Jetson device.

## Architecture
PC (Keyboard Input)  
→ ROS 2 Topic (`/motor_cmd`)  
→ Jetson (Docker Container)  
→ Serial Communication (`/dev/ttyUSB0`)  
→ Arduino UNO  
→ L298N Motor Driver  

## Folder Structure
- `pc/` : ROS 2 node that publishes motor commands via keyboard input  
- `jetson/` : ROS 2 subscriber node that bridges commands to the serial interface  
- `arduino/` : Arduino motor control code for the L298N driver  

## Requirements
- ROS 2 Humble
- Docker (on Jetson)
- Arduino UNO
- L298N motor driver

## Running

### PC
```bash
python3 pc/keyboard_pub.py
