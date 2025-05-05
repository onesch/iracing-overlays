# iRacing Overlays

**iRacing Overlays** is a Python + PyQt6 graphical application that displays real-time data from iRacing as customizable overlay windows on top of your screen.

---

## 📦 Features

- Real-time telemetry display (speed, throttle, brake, etc.).
- Automatically connects to iRacing when running.
- Startup overlay menu with the option to hide.
- Transparent always-on-screen overlay.
- Clean MVC structure: View / Controller / Model.

---

## 🖼️ Screenshot

<img width="425" alt="image" src="https://github.com/user-attachments/assets/8366cc71-5333-4b6e-86b9-a2a62e5f5443" />

---

## 🛠️ Installation

> Requires Python 3.10+

```bash
git clone https://github.com/onesch/iracing-overlays.git
cd iracing-overlay
pip install -r requirements.txt
```
or install in [releases](https://github.com/onesch/iracing-overlays/releases/tag/publish)

## 🚀 Usage
```bash
.\make.bat run
```

## 🗂️ Project Structure
```
.
├───.gitignore
├───main.py
├───make.bat
├───README.md
├─── window_position.json      
│
├───services
│   └───telemetry_updater.py
│
├───settings
│   └───constants.py
│
├───ui
│   ├───styles.py
│   │
│   ├───startup
│   │   ├───controller.py
│   │   └───view.py
│   │
│   └───telemetry
│       └───controller.py
│       └───view.py
│       │
│       └───widgets
│           └───bars.py
│
└───utils
    └───utils.py

```

## 📌 TODO
- ✅ Startup overlay with iRacing detection.
- ✅ Telemetry overlay view with graph widgets.
- 🔲 Configurable UI settings.
- 🔲 Basic testing suite.
- 🔲 Parameter selection via GUI.
- 🔲 Support for multi-monitor setups.

## 🧑‍💻 Contributing
Pull requests are welcome. Feel free to open issues with suggestions or bug reports.

# 📄 License
[MIT](https://github.com/onesch/iracing-overlays/blob/master/LICENSE) License.
