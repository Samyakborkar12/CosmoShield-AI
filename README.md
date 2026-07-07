<div align="center">

# 🛰️ CosmoShield AI

### AI-Powered Space Radiation Prediction System for ISRO's Geostationary Satellites

Predicting hazardous space radiation using **Deep Learning**, **Time-Series Forecasting**, and **Real-Time Space Weather Data**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-LSTM-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

# 📖 Overview

CosmoShield AI is an AI-powered predictive space weather monitoring system developed for protecting **ISRO's Geostationary Satellites** from harmful space radiation.

The project combines **Machine Learning**, **Time-Series Forecasting**, and **Space Weather Data** to predict energetic particle radiation before it damages satellite electronics.

Instead of reacting after failures occur, CosmoShield AI enables proactive decision-making through intelligent forecasting and early warning alerts.

---

# 🚀 Features

- 🤖 LSTM-based Radiation Prediction
- 📡 Space Weather Monitoring
- 📈 Historical Radiation Analysis
- 🚨 Radiation Risk Alerts
- 🌍 NOAA & NASA Data Integration
- 📊 Interactive Dashboard
- ⚡ REST API using Flask
- 💾 SQLite Database
- 📉 Radiation Trend Visualization

---

# 🧠 Problem Statement

Geostationary satellites continuously operate in a harsh radiation environment where energetic particles from the Sun and Earth's radiation belts can damage onboard electronics.

These radiation events may cause:

- Deep Dielectric Charging
- Electrostatic Discharge
- Single Event Effects (SEEs)
- Memory Bit Flips
- Component Degradation
- Reduced Satellite Lifespan

Early prediction helps operators take preventive actions before hazardous radiation conditions occur.

---

# 💡 Solution

CosmoShield AI predicts future radiation conditions using an LSTM-based deep learning model trained on historical space weather observations.

The prediction pipeline:

```
Space Weather Data
        │
        ▼
Data Processing
        │
        ▼
LSTM Prediction Model
        │
        ▼
Radiation Risk Assessment
        │
        ▼
Dashboard & Alerts
```

---

# 🏗️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask |
| AI/ML | TensorFlow, Keras, LSTM |
| Data Processing | Pandas, NumPy, SciPy |
| Scientific Data | cdflib |
| Database | SQLite |
| Visualization | Plotly, Matplotlib |
| Version Control | Git & GitHub |
| Deployment | Render |

---

# 📂 Project Structure

```text
CosmoShield-AI/
│
├── backend/
├── frontend/
├── ml/
├── datasets/
├── docs/
├── assets/
├── tests/
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 📚 Documentation

Detailed documentation is available inside the **docs/** directory.

| Document | Description |
|----------|-------------|
| Project_Overview.md | Project overview and objectives |
| Research.md | Space radiation research |
| Architecture.md | System architecture |
| Dataset.md | Dataset documentation |
| Model_Explanation.md | LSTM model explanation |
| API_Documentation.md | Backend APIs |
| Installation.md | Setup guide |
| Future_Work.md | Future roadmap |
| Resources.md | References and resources |

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/Samyakborkar12/CosmoShield-AI.git
```

Move into the project directory.

```bash
cd CosmoShield-AI
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the backend.

```bash
python backend/app.py
```

---

# 📊 Dataset Sources

- GOES Electron Flux Data
- WIND Spacecraft Data
- NOAA Space Weather API
- NASA DONKI API

---

# 🎯 Future Roadmap

- Real-Time Prediction
- Multi-Satellite Support
- Explainable AI (XAI)
- Physics-Informed AI
- Transformer Models
- Cloud Deployment
- Live Alert System

---

# 👨‍💻 Team

**Team Name:** CosmoShield AI

Contributors:

- Samyak Amardeep Borkar *(Team Lead & Backend Developer)*
- Add remaining team members here.

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgements

Special thanks to:

- ISRO
- NASA
- NOAA
- TensorFlow
- Keras
- Open Source Community

---

<div align="center">

### ⭐ If you like this project, consider giving it a Star!

Made with ❤️ for innovation in Space Technology.

</div>
