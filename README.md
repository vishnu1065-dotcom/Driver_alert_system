# 🚗 Driver Alert System

An AI-powered Driver Alert System designed to improve road safety by monitoring the driver's face and detecting signs of drowsiness or distraction in real time.

The system uses a camera and computer vision techniques to analyze the driver's eye and facial conditions. When drowsiness is detected, the system provides an immediate alert using a buzzer or other warning mechanism.

---

## 📌 Project Overview

Driver fatigue and distraction are major causes of road accidents. This project aims to develop a low-cost embedded AI system capable of continuously monitoring a driver's alertness.

A camera captures the driver's face, and the Raspberry Pi processes the video using computer vision and AI techniques.

The system can identify conditions such as:

- 😴 Driver drowsiness
- 👁️ Prolonged eye closure
- 😵 Loss of attention
- 📱 Driver distraction
- ⚠️ Unsafe driving conditions

When the system detects a potential danger, an alert is generated immediately.

---

## 🎯 Objectives

- Detect driver drowsiness in real time.
- Monitor eye closure and facial conditions.
- Detect driver distraction.
- Generate an immediate warning when unsafe behavior is detected.
- Implement the system using Raspberry Pi and a camera.
- Develop a low-cost and portable driver safety system.
- Explore AI and computer vision for automotive safety applications.

---

## 🧠 Technologies Used

- Python
- Raspberry Pi 4 Model B
- OpenCV
- Computer Vision
- Artificial Intelligence / Machine Learning
- Facial Landmark Detection
- Eye Aspect Ratio (EAR)
- Webcam / Raspberry Pi Camera
- GPIO
- Buzzer
- LED

---

## 🔧 Hardware Requirements

- Raspberry Pi 4 Model B
- USB Webcam / Raspberry Pi Camera
- Buzzer
- LED
- Resistors
- Breadboard
- Jumper wires
- Power supply
- Optional: OLED/LCD display

---

## 💻 Software Requirements

- Raspberry Pi OS
- Python 3
- OpenCV
- NumPy
- MediaPipe or another facial landmark detection library
- GPIO library

---

## ⚙️ Working Principle

The system follows these basic steps:

1. The camera captures the driver's face continuously.
2. OpenCV processes the camera frames.
3. The driver's face is detected.
4. Facial landmarks are identified.
5. The system monitors the driver's eyes and facial orientation.
6. Eye closure is analyzed using computer vision.
7. If the driver's eyes remain closed beyond a predefined time, the system identifies possible drowsiness.
8. The buzzer and LED are activated.
9. The driver receives an immediate warning.
10. The system continuously returns to monitoring mode.

---

## 🔄 System Flow

```text
        Camera
           ↓
     Video Capture
           ↓
     Face Detection
           ↓
   Facial Landmark Detection
           ↓
    Eye / Face Analysis
           ↓
   ┌───────────────────┐
   │ Driver Alertness  │
   │     Analysis      │
   └───────────────────┘
           ↓
     ┌─────┴─────┐
     ↓           ↓
   Alert       Normal
     ↓           ↓
 Buzzer + LED  Continue
