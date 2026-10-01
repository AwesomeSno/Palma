

# Palma

A tiny wristband made with the ESP32-S3 that recognizes hand gestures using a tiny neural network. Use it to send commands and instructions to computers, automation systems, or even robotic arms, all from your wrist.

## How it works

1. The BNO085 IMU measures wrist motion and orientation many times per second.
2. The ESP32-S3 collects short windows of this motion data.
3. A tiny neural network running on the ESP identifies which gesture the motion matches with. All locally on the wristband.
4. A binding table maps each recognized gesture to an action you programmed to it. Like for example, play/pause, toggle a light, or move a robotic arm in a specific manner.
5. The ESP32 sends the command over BLE or ESP-NOW to the target device.
6. A small vibration motor buzzes to confirm the gesture was recognized.

To teach **Palma** a new gesture, you can just record it a few times and assign it an action. That binding is stored on device, so it wokrs the same way every time you wear it.

### Features

- On-device gesture recognition (no phone or cloud required)
- Record any gesture and bind it to an action
- Send commands to computers, home automation systems, and robots
- BLE and ESP-NOW for low-latency control

### Getting started

- Flash the firmware to an ESP32-S3 board
- Use the on-device UI to record gestures and assign actions
- Control devices directly, no phone needed

### Use cases

- Media control
- Smart home toggles
- Robot control
- Accessibility

## Author

Designed and built by **Harinandan J V** for Hack Club's Half Life hardware program.

## Open source

This project is open source. You are free to use, modify, and build on Palma for your own projects. If you do something cool with it, I'd love to hear about it.