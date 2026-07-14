# Dataset Documentation

## Project

CosmoShield AI v2

Artificial Intelligence Powered Space Weather Forecasting System

---

# Bharatiya Antariksha Hackathon 2026

## Problem Statement 14

Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites

---

# Introduction

The accuracy of any forecasting model depends heavily on the quality, consistency, and scientific relevance of the training dataset.

For this project, only publicly available and scientifically validated datasets are used. These datasets are widely adopted by the international space weather research community.

The selected datasets provide both the input parameters (solar wind conditions) and the target variable (energetic electron flux) required for supervised machine learning.

---

# Dataset Overview

CosmoShield AI uses two primary scientific datasets.

| Dataset | Organization | Purpose |
|---------|--------------|---------|
| OMNI Dataset | NASA OMNIWeb | Solar Wind Parameters |
| GOES Electron Flux | NOAA | Target Electron Flux |

These datasets are synchronized on the basis of timestamp before model training.

---

# Dataset 1 — NASA OMNI

## Source

NASA OMNIWeb Data Center

The OMNI dataset combines measurements from multiple spacecraft positioned upstream of Earth.

These measurements provide near-Earth solar wind conditions and interplanetary magnetic field parameters.

---

## Parameters Used

The following parameters are selected as model input features:

| Parameter | Description | Unit |
|-----------|-------------|------|
| IMF | Interplanetary Magnetic Field Magnitude | nT |
| BX_GSE | Magnetic Field X Component | nT |
| BY_GSE | Magnetic Field Y Component | nT |
| BZ_GSE | Magnetic Field Z Component | nT |
| Speed | Solar Wind Speed | km/s |
| Proton Density | Solar Wind Density | particles/cm³ |
| Temperature | Solar Wind Temperature | Kelvin |

---

# Why OMNI?

The OMNI dataset provides the physical conditions responsible for changes in Earth's radiation belts.

Energetic electrons at geostationary orbit are strongly influenced by solar wind dynamics, making these parameters ideal predictors for time-series forecasting.

---

# Dataset 2 — NOAA GOES Electron Flux

## Source

National Oceanic and Atmospheric Administration (NOAA)

GOES satellites continuously monitor energetic particles around geostationary orbit.

For this project, the energetic electron flux greater than **2 MeV** is used as the prediction target.

---

## Target Variable

| Variable | Description |
|----------|-------------|
| Electron Flux (>2 MeV) | Number of energetic electrons detected at geostationary orbit |

The forecasting model learns to estimate future values of this variable using historical solar wind observations.
---

# Data Collection Strategy

The dataset preparation process consists of combining independent scientific observations into a unified time-series suitable for machine learning.

The workflow is as follows:

```
NASA OMNI Dataset
        │
        │
        ▼
Solar Wind Parameters

        +

NOAA GOES Dataset
        │
        ▼
Electron Flux

        │
        ▼
Timestamp Alignment

        │
        ▼
Merged Dataset

        │
        ▼
Machine Learning Pipeline
```

---

# Data Preprocessing

Raw scientific observations cannot be used directly for training because they often contain missing values, inconsistent timestamps, measurement gaps, and noise.

To prepare the data for machine learning, the following preprocessing pipeline is applied.

---

## Step 1 — Timestamp Synchronization

The OMNI and GOES datasets are first aligned using their timestamps.

Since both datasets originate from different missions, synchronization ensures that every input observation corresponds to the correct electron flux measurement.

This step is essential for supervised learning.

---

## Step 2 — Missing Value Handling

Scientific datasets frequently contain missing measurements caused by telemetry interruptions, communication loss, or instrument maintenance.

Missing observations are handled using appropriate preprocessing techniques such as:

- Removal of invalid rows
- Forward filling (where appropriate)
- Linear interpolation (if scientifically justified)

Rows containing excessive missing information are discarded to maintain data quality.

---

## Step 3 — Feature Selection

Only scientifically relevant parameters are selected as model inputs.

Selected Features:

- IMF
- Bx
- By
- Bz
- Solar Wind Speed
- Proton Density
- Solar Wind Temperature

Target Variable:

- Electron Flux (>2 MeV)

Reducing unnecessary variables improves training efficiency and minimizes model complexity.

---

## Step 4 — Feature Scaling

The selected parameters have significantly different numerical ranges.

For example:

- IMF ≈ 5 nT
- Speed ≈ 450 km/s
- Temperature ≈ 250,000 K

Without scaling, larger values dominate the optimization process.

Therefore, numerical features are normalized using **StandardScaler**, ensuring that each feature contributes proportionally during training.

---

## Step 5 — Sequence Generation

Electron flux forecasting is a sequential prediction problem.

Instead of predicting from a single observation, the model receives a window of previous observations.

Example:

```
Time 1

Time 2

Time 3

...

Time N

↓

Predict Future Electron Flux
```

This allows the LSTM model to learn temporal relationships within the data.

---

# Dataset Splitting

After preprocessing, the dataset is divided into three subsets.

| Dataset | Purpose |
|----------|---------|
| Training Set | Model Learning |
| Validation Set | Hyperparameter Tuning |
| Test Set | Final Performance Evaluation |

Typical ratio:

- Training : 70%
- Validation : 15%
- Testing : 15%

This separation prevents overfitting and provides an unbiased estimate of model performance.

---

# Data Quality Assurance

Before model training, several validation checks are performed.

These include:

- Duplicate record removal
- Missing value verification
- Timestamp consistency
- Numerical range validation
- Feature distribution analysis
- Sequence integrity verification

Only validated data is passed to the machine learning pipeline.

---
---

# Dataset Statistics

The final training dataset consists of synchronized observations from the NASA OMNI dataset and NOAA GOES electron flux measurements.

After preprocessing, the dataset is organized into multivariate time-series sequences suitable for deep learning.

Each training sample contains:

- Historical solar wind observations
- Corresponding energetic electron flux
- Sequential time window
- Future forecasting target

The dataset is structured to support supervised learning for multi-horizon forecasting.

---

# Scientific Feature Justification

The selected input parameters are not arbitrary; they are chosen based on established space weather research demonstrating their influence on Earth's radiation belts.

| Feature | Scientific Importance |
|----------|-----------------------|
| IMF | Represents the strength of the interplanetary magnetic field influencing geomagnetic activity. |
| Bx | Indicates the X-component of the magnetic field in Geocentric Solar Ecliptic coordinates. |
| By | Represents east-west magnetic field variations affecting solar wind interactions. |
| Bz | One of the most critical parameters governing magnetic reconnection between the solar wind and Earth's magnetosphere. |
| Solar Wind Speed | Controls the arrival and impact of solar disturbances at Earth. |
| Proton Density | Reflects solar wind particle concentration and dynamic pressure. |
| Temperature | Indicates plasma energy and helps characterize solar wind conditions. |

These parameters collectively describe the near-Earth space environment and are widely used in operational space weather forecasting.

---

# Feature Importance

The forecasting model learns nonlinear relationships between the selected input features and future energetic electron flux.

Although feature importance is learned automatically by the neural network, scientific literature suggests that the following variables often have the greatest influence:

- Southward Bz
- Solar Wind Speed
- IMF Magnitude
- Proton Density

These variables are known to correlate with geomagnetic disturbances and energetic electron enhancements.

---

# Challenges

Several challenges arise when working with scientific space weather datasets:

- Missing observations
- Instrument downtime
- Different temporal resolutions
- Measurement noise
- Extreme solar events
- Time synchronization between multiple missions

The preprocessing pipeline is designed to minimize the impact of these challenges before model training.

---

# Future Dataset Improvements

Future versions of CosmoShield AI may incorporate additional scientific datasets to improve forecasting performance.

Potential additions include:

- ISRO GRASP payload observations
- ACE spacecraft measurements
- DSCOVR solar wind observations
- Solar flare event catalogs
- Coronal Mass Ejection (CME) databases
- Geomagnetic indices (Kp, Dst, AE)
- Solar X-ray flux measurements
- Sunspot number records

The inclusion of these datasets may enhance model robustness during extreme space weather events.

---

# Dataset Validation

Before model training, the dataset undergoes several validation checks.

These include:

- Verification of timestamp consistency
- Numerical range validation
- Missing value inspection
- Duplicate record detection
- Feature normalization verification
- Sequence generation validation

Only validated samples are included in the final training dataset.

---

# Dataset Summary

The datasets selected for CosmoShield AI provide a scientifically reliable foundation for forecasting energetic electron radiation at geostationary orbit.

By combining NASA OMNI solar wind observations with NOAA GOES electron flux measurements, the project establishes a complete supervised learning dataset aligned with the objectives of **Problem Statement 14**.

The preprocessing pipeline ensures that the resulting data is clean, synchronized, and suitable for deep learning–based time-series forecasting.

---

**Document Version:** 1.0

**Project:** CosmoShield AI v2

**Team:** Team Pulse X

**Hackathon:** Bharatiya Antariksha Hackathon (BAH) 2026

**Problem Statement:** 14 — Forecasting Energetic Particle Radiation Environment for ISRO's Geostationary Satellites