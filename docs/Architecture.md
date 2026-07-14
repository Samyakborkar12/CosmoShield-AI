# System Architecture

## Project

CosmoShield AI v2

Artificial Intelligence Powered Space Weather Forecasting System

---

# Bharatiya Antariksha Hackathon 2026

## Problem Statement 14

Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites

---

# Architecture Overview

CosmoShield AI follows a modular architecture where every component is independent but connected through well-defined interfaces.

The system consists of five primary layers:

1. Data Layer
2. Machine Learning Layer
3. Backend Layer
4. Database Layer
5. Frontend Layer

Each layer performs a specific responsibility within the forecasting pipeline.

---

# High Level Architecture

```

┌──────────────────────────────┐
│ NASA OMNI Dataset │
│ NOAA GOES Dataset │
└─────────────┬────────────────┘
│
▼
┌──────────────────────────────┐
│ Data Preprocessing │
│ • Cleaning │
│ • Feature Selection │
│ • Normalization │
│ • Sequence Builder │
└─────────────┬────────────────┘
│
▼
┌──────────────────────────────┐
│ Machine Learning │
│ LSTM Forecasting Model │
└─────────────┬────────────────┘
│
▼
┌──────────────────────────────┐
│ Flask Backend │
│ REST API │
└─────────────┬────────────────┘
│
▼
┌──────────────────────────────┐
│ SQLite Database │
│ Prediction History │
└─────────────┬────────────────┘
│
▼
┌──────────────────────────────┐
│ Mission Dashboard │
│ HTML │ CSS │ JS │
│ Chart.js │ Three.js │
└──────────────────────────────┘

```

---

# Layer 1 — Data Layer

The Data Layer is responsible for acquiring and organizing scientific datasets.

Primary sources include:

- NASA OMNIWeb
- NOAA GOES Satellite

The datasets contain measurements of:

- IMF
- Bx
- By
- Bz
- Solar Wind Speed
- Proton Density
- Solar Wind Temperature
- Electron Flux (>2 MeV)

The datasets are stored inside:

```

datasets/

raw/

processed/

final/

```

---

# Layer 2 — Data Processing Layer

This layer prepares raw scientific observations for machine learning.

Processing steps include:

- Missing Value Handling
- Timestamp Alignment
- Feature Selection
- Feature Scaling
- Sequence Generation
- Dataset Splitting

The output of this layer becomes the direct input for model training.

---

# Layer 3 — Machine Learning Layer

The Machine Learning Layer performs time-series forecasting.

Current Model

- Long Short-Term Memory (LSTM)

Responsibilities

- Sequence Learning
- Pattern Recognition
- Forecast Generation
- Multi-step Prediction

Future versions may additionally support:

- GRU
- Transformer
- Temporal Fusion Transformer
- N-BEATS

---

# Why LSTM?

LSTM is selected because:

- Suitable for sequential data.
- Captures temporal dependencies.
- Performs well for scientific time-series.
- Proven effectiveness in forecasting applications.
---

# Layer 4 — Backend Architecture

The backend is developed using the Flask framework and follows a modular service-oriented architecture.

Rather than placing all logic in a single file, responsibilities are divided into independent modules to improve maintainability, scalability, and testing.

## Backend Responsibilities

- Receive prediction requests
- Validate user input
- Preprocess incoming parameters
- Execute the trained AI model
- Generate radiation forecasts
- Perform risk classification
- Store prediction history
- Return structured JSON responses

---

# Backend Directory Structure

```
backend/

├── database/
│   ├── init_db.py
│   ├── prediction_db.py
│
├── routes/
│   ├── home.py
│   ├── predict.py
│   ├── history.py
│   ├── health.py
│
├── services/
│   └── prediction_service.py
│
├── utils/
│   └── validation.py
```

Each module has a single responsibility, making the backend easier to maintain and extend.

---

# Prediction Request Flow

The prediction workflow follows a structured pipeline.

```
Dashboard

↓

POST /api/predict

↓

Input Validation

↓

Prediction Service

↓

Feature Scaling

↓

LSTM Model

↓

Radiation Prediction

↓

Risk Classification

↓

SQLite Storage

↓

JSON Response

↓

Dashboard Update
```

---

# Layer 5 — Database Architecture

CosmoShield AI currently uses SQLite for lightweight local storage.

The database stores prediction history generated by the forecasting engine.

## Current Table

### prediction_history

| Field | Description |
|--------|-------------|
| id | Primary Key |
| satellite | Satellite Name |
| energy | Electron Energy |
| radiation | Predicted Electron Flux |
| risk | Risk Category |
| timestamp | Prediction Time |

The database design is intentionally simple to ensure rapid deployment during the hackathon while allowing future migration to PostgreSQL or MySQL.

---

# API Architecture

The backend exposes RESTful APIs for communication between the dashboard and the AI engine.

## Available Endpoints

| Method | Endpoint | Purpose |
|----------|------------------|------------------------------|
| GET | / | Landing Page |
| GET | /dashboard | Dashboard |
| GET | /api/health | Health Status |
| POST | /api/predict | Generate Prediction |
| GET | /api/history | Retrieve Prediction History |

All APIs exchange data in JSON format.

---

# Prediction API Lifecycle

```
Client Request

↓

JSON Validation

↓

Data Cleaning

↓

Scaling

↓

LSTM Prediction

↓

Risk Calculation

↓

Database Logging

↓

JSON Response
```

---

# Frontend Architecture

The frontend follows a component-based structure where each visual section performs an independent task.

## Components

- Landing Page
- Mission Dashboard
- Mission Input Panel
- Live Prediction Panel
- Radiation Trend Chart
- Prediction History
- Interactive Earth Visualization

This modular design improves maintainability and allows future expansion without affecting existing components.

---

# Frontend Directory Structure

```
frontend/

templates/

│
├── index.html
└── dashboard.html

static/

├── css/
│   ├── style.css
│   └── dashboard.css
│
├── js/
│   ├── main.js
│   ├── dashboard.js
│   └── earth.js
│
└── images/
```

---

# Frontend Workflow

```
User Input

↓

Dashboard Form

↓

REST API

↓

Prediction Response

↓

DOM Update

↓

Charts Refresh

↓

Prediction History Refresh

↓

Mission Status Update
```

---
---

# Machine Learning Architecture

The forecasting engine is designed as a supervised multivariate time-series prediction pipeline.

Historical solar wind observations are converted into sequential input windows before being supplied to the neural network.

## Input Features

The forecasting model uses the following scientific parameters:

| Feature | Description |
|---------|-------------|
| IMF | Interplanetary Magnetic Field Magnitude |
| Bx | Magnetic Field X Component |
| By | Magnetic Field Y Component |
| Bz | Magnetic Field Z Component |
| Speed | Solar Wind Speed |
| Density | Solar Wind Proton Density |
| Temperature | Solar Wind Temperature |

These parameters represent the current state of the heliospheric environment and strongly influence energetic particle dynamics.

---

# Target Variable

The model predicts:

**Energetic Electron Flux (>2 MeV)**

Forecast Horizons:

- 45 Minutes
- 6 Hours
- 12 Hours

---

# Machine Learning Pipeline

```
Raw Scientific Data

↓

Cleaning

↓

Interpolation

↓

Feature Selection

↓

Normalization

↓

Sequence Generation

↓

Training Dataset

↓

LSTM Model

↓

Prediction

↓

Risk Classification
```

---

# Model Training Workflow

```
Historical Dataset

↓

Train / Validation / Test Split

↓

Model Training

↓

Loss Evaluation

↓

Model Optimization

↓

Best Model Saved

↓

Production Inference
```

---

# Deployment Architecture

```
                Browser

                   │

                   ▼

        HTML / CSS / JavaScript

                   │

                   ▼

             Flask REST API

                   │

         ┌─────────┴─────────┐

         ▼                   ▼

SQLite Database        LSTM Model

         │                   │

         └─────────┬─────────┘

                   ▼

           JSON Response

                   ▼

        Mission Dashboard
```

---

# Security Considerations

The current implementation incorporates the following security measures:

- Server-side input validation
- Numeric parameter verification
- JSON request validation
- Backend exception handling
- Modular API structure

Future improvements may include:

- Authentication
- API Keys
- HTTPS Deployment
- Rate Limiting
- Logging & Monitoring

---

# Scalability

The architecture has been intentionally designed to support future expansion.

Possible future enhancements include:

- Real-time NOAA data ingestion
- NASA API integration
- ISRO GRASP payload integration
- Multi-satellite forecasting
- Cloud deployment
- Containerization using Docker
- Kubernetes orchestration
- GPU inference
- Distributed model serving

---

# Design Decisions

## Why Flask?

Flask was selected because:

- Lightweight framework
- Easy REST API development
- Rapid prototyping
- Excellent Python ecosystem
- Simple ML integration

---

## Why LSTM?

LSTM is used because:

- Designed for sequential data
- Learns temporal dependencies
- Performs well for scientific forecasting
- Widely adopted in time-series prediction

---

## Why SQLite?

SQLite was selected because:

- Zero configuration
- Lightweight
- Reliable
- Perfect for local deployment and hackathon demonstrations

Future production deployments may migrate to PostgreSQL.

---

## Why Chart.js?

Chart.js provides:

- Interactive visualization
- Lightweight rendering
- Responsive charts
- Easy JavaScript integration

---

## Why Three.js?

Three.js enables:

- Interactive 3D Earth visualization
- Modern user interface
- Better user engagement
- Scientific presentation quality

---

# Architecture Summary

CosmoShield AI adopts a modular, scalable, and research-oriented architecture specifically designed for space weather forecasting.

The separation of data processing, machine learning, backend services, database management, and visualization ensures that each subsystem can evolve independently while remaining fully integrated into the overall forecasting pipeline.

This architecture not only satisfies the objectives of **Problem Statement 14** but also provides a strong foundation for future operational deployment and scientific research.

---

**Document Version:** 1.0

**Project:** CosmoShield AI v2

**Team:** Team Pulse X

**Hackathon:** Bharatiya Antariksha Hackathon (BAH) 2026

**Problem Statement:** 14 — Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites