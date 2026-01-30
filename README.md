# ROS 2 – Jetson – Arduino Motor Control

PC üzerinde çalışan ROS 2 Humble node’u ile,
Jetson üzerindeki Docker container içinde çalışan ROS 2 node’u
aracılığıyla Arduino UNO’ya seri haberleşme ile motor kontrolü.

## Mimari
PC (Keyboard Input)
→ ROS 2 Topic (/motor_cmd)
→ Jetson (Docker)
→ Serial (/dev/ttyUSB0)
→ Arduino UNO
→ L298N Motor Driver

## Klasör Yapısı
- pc/ : Klavye ile motor komutu gönderen ROS node
- jetson/ : ROS subscriber + serial bridge
- arduino/ : Arduino motor kontrol kodu

## Gereksinimler
- ROS 2 Humble
- Docker (Jetson)
- Arduino UNO
- L298N motor sürücü

## Çalıştırma
PC:
```bash
python3 pc/keyboard_pub.py
