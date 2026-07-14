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

| File | Type | Purpose |
|------|------|---------|
| `server.py` | 🐍 Backend | Python server with hacker theme |
| `weather.html` | 🌤️ Frontend | Weather app disguise |
| `delivery.html` | 🍔 Frontend | Food delivery app disguise |
| `map.html` | 🗺️ Frontend | Live movement map |
| `index.html` | 📍 Frontend | Original tracker (reference) |
| `.gitignore` | 📄 Config | Excludes log files |
| `README.md` | 📄 Docs | Project documentation |
| `locations.log` | 📊 Data | Location logs (auto-generated) |
| `locations.csv` | 📈 Data | CSV data (auto-generated) |


## 🚀 Quick Start Guide

### Prerequisites

- **Kali Linux** (or any Linux distro)
- **Python 3.8+**
- **ngrok** account (free)
- **Browser** with Geolocation support

### Installation

```
# Clone the repository
git clone https://github.com/hacker-604/location-tracker.git
cd location-tracker

# Install ngrok (if not installed)
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin/
rm ngrok-stable-linux-amd64.zip

# Authenticate ngrok (get token from dashboard.ngrok.com)
ngrok config add-authtoken YOUR_AUTH_TOKEN
```
Running the Tracker

1️⃣ Start the Python Server
```
python3 server.py
```
2️⃣ Start ngrok Tunnel (in new terminal)
```
ngrok http 8080
Copy the ngrok URL (e.g., https://xxxx.ngrok-free.dev)
```
3️⃣ Update HTML Files
```
Edit weather.html and delivery.html:

javascript
const SERVER_URL = 'https://YOUR_NGROK_URL.ngrok-free.dev';
```
4️⃣ Share the Link
```
Share your ngrok URL with test subjects:

text
https://YOUR_NGROK_URL.ngrok-free.dev        # Weather disguise
https://YOUR_NGROK_URL.ngrok-free.dev/delivery  # Delivery disguise
```
## 📱 How It Works

### 🔄 User Flow

| Step | Action |
|------|--------|
| 1️⃣ | 🔗 User opens link |
| 2️⃣ | 🚫 Sees "Location Required" blocker |
| 3️⃣ | 👆 Clicks "Enable Location" |
| 4️⃣ | 🌐 Browser asks for permission |
| 5️⃣ | ✅ User allows → Page loads with disguised content |
| 6️⃣ | 📡 Location sent to your server |
| 7️⃣ | 💻 You see coordinates in terminal |
| 8️⃣ | 🏃 User moves → Continuous updates |
| 9️⃣ | 🔴 User closes tab → Disconnect notification |

## 🏗️ Technical Architecture

| Layer | Component | Description |
|-------|-----------|-------------|
| **Client** | 🌐 Target Device (Browser) | Captures location via HTML5 Geolocation API |
| **Tunnel** | 🔗 ngrok URL (public) | Provides secure HTTPS access from anywhere |
| **Server** | 🐧 Kali VM (localhost:8080) | Hosts the Python HTTP server |
| **Backend** | 🐍 Python Server (server.py) | Processes and logs incoming location data |
| **Storage** | 📊 locations.log & locations.csv | Saves data for analysis and forensics |

## 🎓 For Your Project Report

### 📚 Key Learning Outcomes

#### 💻 Technical Skills
- 🏗️ Built a complete client-server application
- 📡 Used HTML5 Geolocation API
- 🔄 Implemented real-time data transmission
- 🌐 Configured network tunneling with ngrok

#### 🔒 Security Awareness
- 🎭 Understood social engineering techniques
- 🔍 Recognized privacy implications
- 🛡️ Learned about browser security models
- ⚠️ Understood ethical hacking boundaries

#### 📋 Project Management
- 📝 Version control with Git/GitHub
- 📄 Documentation best practices
- 🧪 Testing and debugging methodologies
- 🤝 Collaboration and code sharing

## ⚖️ Ethical Considerations

> ⚠️ **Important**: This tool is for **educational purposes only**.

### 🚫 What NOT to Do
- ❌ Never use without explicit consent
- ❌ Never deploy in production environments
- ❌ Never track real users without authorization

### ✅ What TO Do
- ✅ Only test in controlled lab environments
- ✅ Respect user privacy and legal boundaries
- ✅ Understand the potential for misuse
- ✅ Use for educational and research purposes only

### 🎯 Key Principles
- 🔒 **Privacy First**: Always prioritize user privacy
- 📚 **Education Focus**: Use only for learning
- ⚖️ **Legal Compliance**: Follow all applicable laws
- 🛡️ **Responsible Disclosure**: Report vulnerabilities ethically

🔧 Troubleshooting

| ⚠️ Issue | ✅ Solution |
|----------|------------|
| 🔑 ngrok authentication error | 🔐 `ngrok config add-authtoken YOUR_TOKEN` |
| 📡 Location not sending | 🔍 Check `SERVER_URL` in HTML files |
| 🚫 404 Not Found | 📁 Ensure `weather.html` and `delivery.html` exist |
| 🚷 Permission denied | 🌐 Enable location in browser settings |
| 🔌 Port in use | 🔢 Change `PORT` in `server.py` (line 20) |


## 📊 Sample Output

### 📡 Location Received

| Field | Value |
|-------|-------|
| **Event** | 📍 INCOMING LOCATION PACKET DETECTED |
| **Timestamp** | 2026-01-13 15:30:45 |
| **Client IP** | 10.11.0.1 |
| **Device** | Chrome on Android |
| **Source** | weather_app |
| **Latitude** | 23.033804509268 |
| **Longitude** | 72.524241777695 |
| **Accuracy** | 15 meters |
| **Google Maps** | https://www.google.com/maps |
| **Status** | ✅ Packet #1 logged successfully |

### 🔴 User Disconnected

| Field | Value |
|-------|-------|
| **Event** | 🔴 USER DISCONNECTED |
| **Timestamp** | 2026-01-13 15:30:45 |
| **Client IP** | 10.11.0.1 |
| **Device** | Chrome on Android |
| **Source** | weather_app |
| **Status** | ❌ User closed the page |


---

## 📚 Resources

| 📖 Resource | 🔗 Link |
|-------------|---------|
| 🌐 **HTML5 Geolocation API** | [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) |
| 🔗 **ngrok Documentation** | [ngrok Docs](https://ngrok.com/docs) |
| 🐍 **Python HTTP Server** | [Python Docs](https://docs.python.org/3/library/http.server.html) |
| 🗺️ **Leaflet.js Map Library** | [Leaflet Docs](https://leafletjs.com/) |

🔒 Security Notice

> This project demonstrates techniques for **educational purposes only**. Understanding these methods helps:

| 🛡️ Who | 🎯 Benefit |
|---------|------------|
| 👨‍💻 **Security Professionals** | Defend against location-based attacks |
| 👤 **End Users** | Recognize social engineering attempts |
| 👨‍🔧 **Developers** | Implement better privacy protections |

**⚠️ Important:** Never use this tool without explicit consent. Only test in controlled lab environments. Respect user privacy and legal boundaries.

## ⭐ Acknowledgments

| 🙏 Resource | 🎯 Contribution |
|-------------|-----------------|
| 🐧 **Kali Linux** | Penetration testing environment |
| 🔗 **ngrok** | Secure cross-network tunneling |
| 🗺️ **OpenStreetMap** | Free map tiles for visualization |
| 🌐 **HTML5 Geolocation API** | Browser-based location capture |

**Special thanks to all open-source contributors who make security research accessible!**
                                             
<div align="center">

### 🛡️ Stay Safe, Stay Ethical

**Made with ❤️ for Security Education**

---

⭐ **Star this repo** if you find it useful!  
🐛 **Report issues** to help improve the project  
🤝 **Contribute** to make it better for everyone

---

**"Remember: With great power comes great responsibility."**

</div>
