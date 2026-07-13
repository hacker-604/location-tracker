markdown
# 📍 Real-Time Location Tracker

<div align="center">

**A Cybersecurity Student Project - Educational Purpose Only**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

</div>

## 📋 Overview

This project demonstrates **real-time location tracking** using HTML5 Geolocation API, Python backend, and ngrok tunneling. It's designed as a **cybersecurity student project** to showcase:

- How location data can be captured through legitimate-looking interfaces
- Client-server communication in real-time
- Network tunneling concepts
- Social engineering techniques
- Privacy and security considerations

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **🔍 Hidden Tracking** | Disguised as Weather App & Food Delivery App |
| **🔄 Real-Time Updates** | Tracks user movement continuously |
| **🌐 Cross-Network** | Works anywhere via ngrok tunnel |
| **🗺️ Live Map** | Visualizes tracked locations in real-time |
| **🔴 Disconnect Detection** | Notifies when user closes the page |
| **🚫 Blocker Overlay** | Forces location permission before showing content |
| **📊 Data Export** | Logs to CSV for analysis |
| **🎨 Hacker Theme** | Matrix-style terminal output |

## 🛠️ Technologies

<div align="center">

| Technology | Purpose |
|------------|---------|
| **Python 3** | Backend server |
| **HTML5 + CSS3** | Frontend UI |
| **JavaScript** | Geolocation API, client logic |
| **ngrok** | Public URL tunneling |
| **HTML5 Geolocation API** | GPS/WiFi location capture |
| **Leaflet.js** | Live map visualization |

</div>

## 📁 Project Structure
location-tracker/
├── 📄 server.py # Python backend with hacker theme
├── 🌤️ weather.html # Weather app disguise
├── 🍔 delivery.html # Food delivery app disguise
├── 🗺️ map.html # Live movement map
├── 📍 index.html # Original tracker (reference)
├── 📄 .gitignore # Excludes log files
├── 📄 README.md # This file
├── 📊 locations.log # Location logs (auto-generated)
└── 📈 locations.csv # CSV data (auto-generated)

text

## 🚀 Quick Start Guide

### Prerequisites

- **Kali Linux** (or any Linux distro)
- **Python 3.8+**
- **ngrok** account (free)
- **Browser** with Geolocation support

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/location-tracker.git
cd location-tracker

# Install ngrok (if not installed)
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin/
rm ngrok-stable-linux-amd64.zip

# Authenticate ngrok (get token from dashboard.ngrok.com)
ngrok config add-authtoken YOUR_AUTH_TOKEN
Running the Tracker
1️⃣ Start the Python Server
bash
python3 server.py
2️⃣ Start ngrok Tunnel (in new terminal)
bash
ngrok http 8080
Copy the ngrok URL (e.g., https://xxxx.ngrok-free.dev)

3️⃣ Update HTML Files
Edit weather.html and delivery.html:

javascript
const SERVER_URL = 'https://YOUR_NGROK_URL.ngrok-free.dev';
4️⃣ Share the Link
Share your ngrok URL with test subjects:

text
https://YOUR_NGROK_URL.ngrok-free.dev        # Weather disguise
https://YOUR_NGROK_URL.ngrok-free.dev/delivery  # Delivery disguise
📱 How It Works
User Flow
text
1. User opens link
   ↓
2. Sees "Location Required" blocker
   ↓
3. Clicks "Enable Location"
   ↓
4. Browser asks for permission
   ↓
5. User allows → Page loads with disguised content
   ↓
6. Location sent to your server
   ↓
7. You see coordinates in terminal
   ↓
8. User moves → Continuous updates
   ↓
9. User closes tab → Disconnect notification
Technical Architecture
text
Target Device (Browser)
    ↓ (HTTPS POST via Geolocation API)
ngrok URL (public)
    ↓ (Secure Tunnel)
Kali VM (http://localhost:8080)
    ↓ (Processing)
Python Server (server.py)
    ↓ (Logging)
locations.log & locations.csv
🎓 For Your Project Report
Key Learning Outcomes
Technical Skills

Built a complete client-server application

Used HTML5 Geolocation API

Implemented real-time data transmission

Configured network tunneling

Security Awareness

Understood social engineering techniques

Recognized privacy implications

Learned about browser security models

Project Management

Version control with Git/GitHub

Documentation best practices

Testing and debugging

Ethical Considerations
⚠️ Important: This tool is for educational purposes only.

Never use without explicit consent

Only test in controlled lab environments

Respect user privacy and legal boundaries

Understand the potential for misuse

🔧 Troubleshooting
Issue	Solution
ngrok authentication error	ngrok config add-authtoken YOUR_TOKEN
Location not sending	Check SERVER_URL in HTML files
404 Not Found	Ensure weather.html and delivery.html exist
Permission denied	Enable location in browser settings
Port in use	Change PORT in server.py (line 20)
📊 Sample Output
Terminal (Location Received)
text
┌─────────────────────────────────────────────────────────────────────┐
│ 📍 INCOMING LOCATION PACKET DETECTED                    │
├─────────────────────────────────────────────────────────────────────┤
│ ⏱  TIMESTAMP    2026-07-13 14:30:25
│ 🌐  CLIENT IP    192.168.1.100
│ 📱  DEVICE       Chrome on Android
│ 📦  SOURCE       weather_app
├─────────────────────────────────────────────────────────────────────┤
│ 📍 COORDINATES                                      │
│   LATITUDE   23.03380450929368
│   LONGITUDE  72.52424173977695
│   ACCURACY   15 meters
├─────────────────────────────────────────────────────────────────────┤
│ 🗺  GOOGLE MAPS LINK                                  │
│   https://www.google.com/maps?q=23.0338,72.5242
└─────────────────────────────────────────────────────────────────────┘
▸ Packet #1 logged successfully.
Terminal (User Disconnected)
text
┌─────────────────────────────────────────────────────────────────────┐
│ 🔴 USER DISCONNECTED                                       │
├─────────────────────────────────────────────────────────────────────┤
│ ⏱  TIME        2026-07-13 15:30:45
│ 🌐  CLIENT IP    192.168.1.100
│ 📱  DEVICE      Chrome on Android
│ 📦  SOURCE      weather_app
│ 💬  STATUS      User closed the page
└─────────────────────────────────────────────────────────────────────┘
📚 Resources
HTML5 Geolocation API

ngrok Documentation

Python HTTP Server

Leaflet.js Map Library

🔒 Security Notice
This project demonstrates techniques for educational purposes. Understanding these methods helps:

Security professionals defend against location-based attacks

Users recognize social engineering attempts

Developers implement better privacy protections

📝 License
This project is for educational purposes only. Use responsibly.

👨‍🎓 Author
Cybersecurity Student Project

Course: Cybersecurity Fundamentals

Date: July 2026

Purpose: Educational Demonstration

⭐ Acknowledgments
Kali Linux for the environment

ngrok for tunneling

OpenStreetMap for map tiles

HTML5 Geolocation API

<div align="center">
Made with ❤️ for Educational Purposes

⬆ Back to Top

</div> ```
