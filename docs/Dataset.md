# 📊 Dataset Documentation

## Dataset Overview

CosmoShield AI uses historical and real-time space weather datasets to predict radiation conditions around geostationary satellites.

The datasets contain measurements related to energetic particles, solar activity, and solar wind conditions that influence the radiation environment in space.

---

# Data Sources

## 1. GOES Electron Flux Data

**Provider:** NOAA

GOES (Geostationary Operational Environmental Satellites) continuously monitor Earth's space environment and provide measurements of energetic electron flux.

### Parameters Used

- Electron Flux
- Timestamp
- Energy Channels

### Purpose

Electron flux is the primary target variable used for predicting hazardous radiation conditions.

---

## 2. WIND Spacecraft Data

**Provider:** NASA

The WIND spacecraft measures the properties of the solar wind before it reaches Earth's magnetosphere.

### Parameters Used

- Solar Wind Speed
- Solar Wind Density
- Plasma Temperature
- Magnetic Field Parameters

### Purpose

These measurements help identify incoming solar disturbances that may increase radiation levels.

---

## 3. NOAA Space Weather API

Provides near real-time space weather information.

### Data Includes

- Geomagnetic Activity
- Solar Alerts
- Radiation Storm Information
- Space Weather Notifications

### Purpose

Used to enhance real-time monitoring and improve operational awareness.

---

## 4. NASA DONKI API

NASA's DONKI (Space Weather Database of Notifications, Knowledge, Information) provides information about significant solar events.

### Events Used

- Solar Flares
- Coronal Mass Ejections (CMEs)
- Solar Energetic Particle (SEP) Events

### Purpose

These events provide context for sudden increases in radiation levels.

---

# Dataset Features

The prediction model uses a combination of environmental and radiation-related parameters.

| Feature | Description |
|----------|-------------|
| Timestamp | Time of observation |
| Electron Flux | Radiation intensity measured by GOES |
| Solar Wind Speed | Speed of incoming solar wind |
| Solar Wind Density | Density of solar particles |
| Magnetic Field | Interplanetary magnetic field parameters |
| Solar Event Information | Data from DONKI and NOAA |

---

# Data Preprocessing Pipeline

Before training the LSTM model, the raw datasets undergo several preprocessing steps.

## Step 1 — Data Cleaning

- Remove duplicate records
- Handle missing values
- Remove corrupted entries

---

## Step 2 — Timestamp Alignment

All datasets are synchronized using their timestamps so that observations from different sources represent the same time period.

---

## Step 3 — Feature Selection

Only the most relevant variables required for prediction are retained.

This reduces noise and improves model performance.

---

## Step 4 — Normalization

Numerical features are scaled to a common range before training.

Normalization helps the LSTM model converge faster and improves prediction stability.

---

## Step 5 — Sequence Generation

Because LSTM models learn from sequential data, the processed dataset is converted into fixed-length time windows.

Example:

Previous 24 observations → Predict the next observation.

---

# Training Dataset

The processed historical data is used to train the LSTM model.

The model learns patterns in radiation levels and their relationship with space weather parameters.

---

# Validation Dataset

A separate validation dataset is used to monitor model performance during training and reduce overfitting.

---

# Test Dataset

The final trained model is evaluated on unseen data to measure its prediction capability.

Evaluation metrics may include:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

# Dataset Folder Structure

```text
datasets/
│
├── raw/
│   ├── goes/
│   ├── wind/
│   ├── noaa/
│   └── donki/
│
├── processed/
│
├── sample/
│
└── README.md
```

---

# Future Dataset Expansion

Future versions of CosmoShield AI may include additional datasets such as:

- ACE Spacecraft Data
- DSCOVR Space Weather Data
- GOES Proton Flux Data
- Geomagnetic Indices (Kp, Dst)
- Additional ISRO mission-specific datasets (if publicly available)

---

# Summary

The quality of any AI prediction system depends heavily on the quality of its data.

By combining multiple trusted space weather sources and applying a structured preprocessing pipeline, CosmoShield AI creates a reliable dataset for forecasting radiation conditions around geostationary satellites.
