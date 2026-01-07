# Hand-Tracking Pong Game

A computer vision-powered Pong game that supports both single-player and two-player modes, where players control paddles using hand gestures detected through a webcam and MediaPipe. The game features real-time ball physics, collision detection, lives tracking, and dynamic victory screens—all controlled entirely through hand movements.

## Features

- **Dual Game Modes**: Single-player mode with accelerating difficulty and two-player competitive mode
- **Hand Gesture Controls**: Real-time hand tracking using MediaPipe for intuitive paddle control
- **Dynamic Gameplay**: Physics-based ball movement with collision detection and velocity changes
- **Lives System**: Track remaining lives with on-screen display and game-over detection
- **Victory/Defeat Screens**: Player-specific messaging based on game outcome
- **Instant Restart**: Quick restart functionality without relaunching the application

## Demo

### Single-Player Mode
Control a paddle at the top of the screen using your hand's horizontal position. The ball accelerates over time, creating an increasingly challenging experience.

### Two-Player Mode
Competitive gameplay where your left hand controls the blue left paddle and your red hand controls the blue right paddle. Each player has independent life counters, and the game announces a winner when one player loses all lives.

## Technical Details

**Languages & Libraries:**
- Python
- OpenCV (computer vision operations and game rendering)
- MediaPipe (hand tracking and handedness classification)

**Lines of Code:** 273

**Date Completed:** June 2024

## How It Works

1. **Initialization**: MediaPipe's hand tracking module and OpenCV's video capture initialize at startup
2. **Mode Selection**: Choose single-player (press '1') or two-player (press '2') mode
3. **Hand Detection**: MediaPipe processes webcam frames in real-time, detecting hand landmarks and extracting 21 coordinate points per hand
4. **Coordinate Mapping**: Normalized coordinates (0-1) are scaled to pixel positions for paddle control
5. **Handedness Classification**: In two-player mode, MediaPipe identifies left vs. right hand to control respective paddles
6. **Game Loop**: Continuous loop captures video, updates ball position, checks collisions, manages lives, and renders graphics
7. **Collision Detection**: Mode-aware system handles both horizontal (single-player) and vertical (two-player) paddle orientations
8. **State Management**: Tracks game mode, lives, and transitions between gameplay, victory/defeat screens, and restart flows

## Controls

- **1**: Select single-player mode
- **2**: Select two-player mode
- **Hand Movement**: Control paddle position
- **R**: Restart game
- **Q**: Quit application

## Challenges Overcome

- Implementing mode selection and seamless transitions between gameplay types
- Managing independent life counters and game states for two competing players
- Differentiating left vs. right hand using MediaPipe's handedness API
- Designing collision detection for both horizontal and vertical paddle orientations
- Ensuring smooth physics across both modes while maintaining real-time performance
- Creating victory/defeat screens with player-specific messaging

## Skills Demonstrated

- Multi-mode game architecture with state management
- Advanced hand tracking and handedness classification
- Real-time collision detection and physics simulation
- Dynamic UI rendering with OpenCV
- Event-driven programming for user input
- Object-oriented Python design
- Performance optimization for computer vision applications
- Gesture-based control system implementation
- Real-time computer vision game loop
- Integration of MediaPipe's API into OpenCV workflows

## Installation

```bash
pip install opencv-python numpy mediapipe
```

## Usage

```bash
python pong_game.py
```

## Project Context

This project represents the culmination of my computer vision journey, integrating foundational OpenCV skills with real-time processing techniques into a fully interactive gaming experience. The gesture-based control systems and multi-mode architecture developed here form a crucial foundation for future robotics applications where machines need to interpret human gestures and respond dynamically.
