# 🚀 CosmoShield AI v2

> **AI-Powered Space Weather Forecasting System for ISRO's Geostationary Satellites**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-red)
![Three.js](https://img.shields.io/badge/Three.js-3D-green)

---

# 📌 Project Overview

CosmoShield AI is an Artificial Intelligence powered Space Weather Forecasting System developed for the **Bharatiya Antariksha Hackathon (BAH) 2026**.

The project addresses **Problem Statement 14**, which focuses on forecasting energetic electron flux at geostationary orbit to improve the protection of ISRO's communication satellites against hazardous space weather conditions.

The system processes historical solar wind observations and electron flux measurements, applies advanced Machine Learning models, and predicts future energetic electron radiation levels for multiple forecasting horizons.

---

# 🎯 Problem Statement

## Problem Statement 14

**Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites**

The objective is to develop an Artificial Intelligence model capable of forecasting energetic electron fluxes (>2 MeV) at geostationary orbit.

The model should predict radiation conditions for:

- 45 Minutes Ahead
- 6 Hours Ahead
- 12 Hours Ahead

using historical solar wind observations and space weather parameters.

---

# 🌍 Why This Project?

Space weather significantly impacts satellites operating in geostationary orbit.

Solar storms and energetic particle events may cause:

- Satellite charging
- Communication disruption
- Navigation errors
- Instrument degradation
- Electronic failures

By forecasting radiation conditions before they occur, satellite operators can perform preventive actions and reduce mission risks.

---

# 🎯 Objectives

The primary objectives of CosmoShield AI are:

- Read and process space weather datasets.
- Forecast energetic electron flux.
- Classify mission risk.
- Visualize historical and predicted radiation.
- Provide an interactive Mission Control Dashboard.
- Assist satellite operators in decision making.

---

# ✨ Key Features

✅ Space Weather Forecasting

✅ Multi-Horizon Prediction

- 45 Minutes
- 6 Hours
- 12 Hours

✅ AI-Based Electron Flux Prediction

✅ Mission Risk Classification

✅ Historical Data Visualization

✅ Live Dashboard

✅ Interactive Charts

✅ 3D Earth Visualization

✅ Prediction History

✅ Scientific Data Processing

---

# 🛰 Application Areas

- Satellite Mission Planning
- Space Weather Monitoring
- Communication Satellites
- Navigation Satellites
- Space Research
- Aerospace Education
- AI for Space Science

---

# 🧠 Machine Learning Pipeline

Raw Space Weather Data

↓

Data Cleaning

↓

Feature Engineering

↓

Sequence Generation

↓

Deep Learning Model

↓

Electron Flux Forecast

↓

Risk Classification

↓

Visualization

---

# 🛠 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap
- Chart.js
- Three.js

## Backend

- Python
- Flask

## Machine Learning

- TensorFlow
- Keras
- Scikit-Learn
- NumPy
- Pandas

## Database

- SQLite

## Visualization

- Matplotlib
- Plotly

---

# 📂 Project Structure

```
CosmoShield-AI/

backend/

frontend/

ml/

datasets/

docs/

models/

notebooks/

tests/

README.md

requirements.txt
```
---

# 📊 Dataset

The forecasting model is trained using publicly available scientific datasets from internationally recognized space agencies.

## Primary Datasets

### 1. NASA OMNI Dataset

The OMNI dataset provides near-Earth solar wind and interplanetary magnetic field measurements.

Important Parameters:

- Interplanetary Magnetic Field (IMF)
- Bx
- By
- Bz
- Solar Wind Speed
- Proton Density
- Solar Wind Temperature

Purpose:

These parameters are used as the primary input features for the forecasting model.

---

### 2. NOAA GOES Electron Flux Dataset

The GOES satellite provides energetic electron flux observations at geostationary orbit.

Target Variable:

> Electron Flux (>2 MeV)

The trained model learns the relationship between solar wind conditions and future energetic electron flux.

---

# 📈 Forecast Horizons

CosmoShield AI provides predictions for multiple operational horizons.

| Forecast | Purpose |
|----------|----------|
| 45 Minutes | Early Warning |
| 6 Hours | Mission Planning |
| 12 Hours | Long-Term Forecast |

---

# ⚙ System Workflow

```
Solar Wind Data

↓

Preprocessing

↓

Feature Engineering

↓

Sequence Generation

↓

Deep Learning Model

↓

Electron Flux Prediction

↓

Risk Classification

↓

Mission Dashboard

↓

Operator Decision Support
```

---

# 🖥 Dashboard Modules

The Mission Control Dashboard consists of several independent modules.

## Mission Status

Displays

- Active Satellite
- Current Mission
- System Status

---

## Solar Wind Monitor

Displays current solar wind parameters including

- IMF
- Bx
- By
- Bz
- Speed
- Density
- Temperature

---

## AI Forecast Panel

Displays

- Predicted Electron Flux
- Risk Level
- Prediction Time
- Forecast Horizon

---

## Radiation Timeline

Displays predictions for

- 45 Minutes
- 6 Hours
- 12 Hours

---

## Interactive Charts

The dashboard visualizes

- Historical Electron Flux
- Forecast Trend
- Solar Wind Parameters

---

## Prediction History

Stores previous AI predictions using SQLite.

---

# 👨‍💻 Team Pulse X

| Member | Role |
|---------|------|
| Samyak Amardeep Borkar | Team Lead • Backend Developer |
| Aaryan Nitin Chavan | Frontend Developer |
| Shravani Sagar Dhulup | Research & Documentation Lead |
| Shreya Ganesh Birari | UI/UX Designer & Quality Assurance (QA) |

---

# 👥 Responsibilities

## Samyak Amardeep Borkar

- Project Architecture
- Backend Development
- Machine Learning Integration
- API Development
- GitHub Repository Management

---

## Aaryan Nitin Chavan

- Frontend Development
- Dashboard Implementation
- JavaScript Integration
- User Interface Development

---

## Shravani Sagar Dhulup

- Scientific Research
- Dataset Validation
- Documentation
- Presentation Content

---

## Shreya Ganesh Birari

- UI/UX Design
- User Experience
- Quality Assurance
- Testing
- Bug Reporting

---

# 📌 Project Goals

Our project aims to

- Forecast hazardous space weather
- Protect communication satellites
- Assist mission operators
- Improve decision making
- Demonstrate AI for Space Applications

---

# 🌟 Future Scope

Future improvements may include

- Live NOAA API Integration
- ISRO GRASP Dataset Integration
- Transformer-Based Forecasting
- Cloud Deployment
- Mobile Dashboard
- Real-Time Alert System
- Explainable AI (XAI)
- Multi-Satellite Forecasting

---
# 🚀 Installation

## Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.12+
- Git
- Visual Studio Code
- pip
- Virtual Environment (recommended)

---

## Clone Repository

```bash
git clone https://github.com/<your-username>/CosmoShield-AI.git

cd CosmoShield-AI
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Server starts on

```
http://127.0.0.1:5000
```

---

# 📂 Detailed Folder Structure

```
CosmoShield-AI/

backend/
│
├── database/
│
├── routes/
│
├── services/
│
├── utils/

frontend/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│
└── templates/

ml/
│
├── training/
├── preprocessing/
├── models/
├── predictor.py
├── risk.py

datasets/
│
├── raw/
├── processed/
└── final/

docs/

models/

notebooks/

tests/

requirements.txt

README.md

app.py
```

---

# 🔄 Development Workflow

The development lifecycle of CosmoShield AI follows a structured pipeline.

```
Research

↓

Dataset Collection

↓

Data Cleaning

↓

Feature Engineering

↓

Model Training

↓

Model Evaluation

↓

Backend Development

↓

Frontend Development

↓

System Integration

↓

Testing

↓

Documentation

↓

Deployment
```

---

# 🌐 API Overview

The backend exposes REST APIs that connect the Machine Learning model with the Mission Control Dashboard.

Available APIs

| Method | Endpoint | Description |
|----------|----------------|------------------------------|
| GET | / | Landing Page |
| GET | /dashboard | Dashboard |
| POST | /api/predict | Generate AI Prediction |
| GET | /api/history | Prediction History |
| GET | /api/health | Health Status |

Detailed API documentation is available inside

```
docs/05_API_Documentation.md
```

---

# 🖥 Dashboard Overview

The Mission Control Dashboard includes the following modules.

### Mission Control

Displays current satellite mission.

---

### Solar Wind Panel

Displays

- IMF
- Bx
- By
- Bz
- Speed
- Density
- Temperature

---

### AI Prediction Engine

Displays

- Predicted Electron Flux
- Risk Category
- Forecast Time

---

### Forecast Timeline

Displays predictions for

- 45 Minutes
- 6 Hours
- 12 Hours

---

### Interactive Earth

A real-time animated Earth developed using Three.js.

---

### Radiation Trend

Interactive graphs generated using Chart.js.

---

### Prediction History

Stores previous forecasts inside SQLite.

---

# 🧪 Testing

Testing includes

- Backend API Testing
- Frontend Validation
- Machine Learning Validation
- Database Testing
- Integration Testing

Future automated testing will be implemented using PyTest.

---

# 🤝 Contribution Guidelines

To contribute:

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📷 Project Screenshots

Screenshots will be added after completing the final dashboard.

```
docs/screenshots/

landing_page.png

dashboard.png

prediction.png

charts.png

history.png
```

---
# 📜 License

This project has been developed exclusively for academic and research purposes as part of the **Bharatiya Antariksha Hackathon (BAH) 2026**.

The source code is intended for educational use, scientific learning, and space weather research.

Future licensing may be updated after the completion of the hackathon.

---

# 🙏 Acknowledgements

We sincerely acknowledge the organizations and communities whose datasets, documentation, and research have supported the development of this project.

- Indian Space Research Organisation (ISRO)
- Bharatiya Antariksha Hackathon (BAH)
- National Aeronautics and Space Administration (NASA)
- National Oceanic and Atmospheric Administration (NOAA)
- OMNIWeb Data Center
- GOES Mission Team
- TensorFlow Team
- Scikit-learn Developers
- Flask Community
- Chart.js Contributors
- Three.js Community

---

# 📚 References

### Scientific Resources

- NASA OMNIWeb
- NOAA Space Weather Prediction Center
- GOES Satellite Mission Documentation
- TensorFlow Official Documentation
- Scikit-learn Documentation
- Flask Documentation
- Three.js Documentation
- Chart.js Documentation

Additional scientific references are available in:

```
docs/07_Resources.md
```

---

# 🏆 Why CosmoShield AI?

Unlike conventional monitoring systems, CosmoShield AI focuses on **forecasting** rather than simply visualizing historical observations.

Our system combines:

- Scientific space weather datasets
- Artificial Intelligence
- Time-Series Forecasting
- Interactive Mission Dashboard
- Risk Classification
- Decision Support

to provide an end-to-end intelligent forecasting platform for satellite mission support.

---

# 🚀 Project Highlights

✔ AI Powered Forecasting

✔ Multi-Horizon Prediction

✔ Space Weather Analytics

✔ Scientific Data Processing

✔ Interactive Dashboard

✔ Mission Control Interface

✔ Electron Flux Prediction

✔ Risk Assessment

✔ Modern UI/UX

✔ Modular Backend

✔ REST API Architecture

✔ SQLite Database

✔ Three.js Earth Visualization

✔ Chart.js Analytics

✔ Production-Oriented Project Structure

---

# 📈 Development Status

| Module | Status |
|----------|--------|
| Research | ✅ Completed |
| Project Planning | ✅ Completed |
| Documentation | 🟡 In Progress |
| Dataset Collection | 🟡 In Progress |
| Data Preprocessing | ⏳ Pending |
| Feature Engineering | ⏳ Pending |
| Model Training | ⏳ Pending |
| Backend Development | ⏳ Pending |
| Frontend Development | ⏳ Pending |
| Integration | ⏳ Pending |
| Testing | ⏳ Pending |
| Final Submission | ⏳ Pending |

---

# 📞 Contact

## Team Pulse X

**Project**

CosmoShield AI v2

**Hackathon**

Bharatiya Antariksha Hackathon (BAH) 2026

**Problem Statement**

Problem Statement 14

Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites

---

# 🌌 Vision

Our vision is to build an intelligent and reliable AI-driven space weather forecasting platform capable of assisting future satellite missions through scientific data analysis, machine learning, and intuitive visualization.

We believe that intelligent forecasting can contribute toward safer and more resilient space operations.

---

<div align="center">

# 🛰️ CosmoShield AI v2

### Artificial Intelligence for Space Weather Forecasting

**Built with ❤️ by Team Pulse X**

**Bharatiya Antariksha Hackathon (BAH) 2026**

*"Predict Today. Protect Tomorrow."*

</div>