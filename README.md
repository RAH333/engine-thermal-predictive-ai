# engine-thermal-predictive-ai

# AeroTherm-AI

A Python-based end-to-end framework that takes internal combustion engine parameters (RPM, fuel-air ratio, coolant flow) and uses a Machine Learning model to predict cylinder head temperature and thermal stress, featuring an automated data pipeline.

# AeroTherm-AI: Engine Thermal Predictive AI Framework

AeroTherm-AI is a data-driven engineering framework designed to predict internal combustion engine (ICE) steady-state cylinder head temperatures based on transient dynamic operational conditions. 

By leveraging **Python** automation architectures and **Machine Learning models**, this framework bridges traditional 1D/3D CFD solvers and real-time physical testbeds, offering rapid thermal evaluation feedback loops during the early R&D phases.

## Target Relevance (EDD Division)
* **Automation-Driven Simulation:** Provides structural script setups built for high-throughput parametric optimization sweeps.
* **Thermal Analysis Insight:** Focuses directly on predicting critical thermal metrics (Cylinder Head Heat Accumulation) corresponding to variations in Engine RPM, Fuel-Air ratio (AFR), and coolant circulation dynamics.
* **Production-Grade Engineering:** Features automated data engineering validation loops, decoupled inference logic, and integrated GitHub Action CI tracking workflows.

## Tech Stack & Dependencies
* **Core Language:** Python 3.10+
* **Data Processing & Analytics:** NumPy, Pandas
* **AI & Predictive Modeling:** Scikit-Learn (Random Forest Ensemble Regression Architectures)
* **Serialization & Pipelines:** Joblib, Unittest framework

## Repository Structural Mapping
* `data/`: House raw and structural feature parameters derived from testbeds/solvers.
* `src/data_pipeline.py`: Robust ETL class modules managing cleanups, physical scale normalization, and structural array divisions.
* `src/train_model.py`: Model training runtime parameters, regression evaluator functions, and binary serialization loops.
* `src/inference_engine.py`: Encapsulated calculation model execution environment mapping dynamic runtime profiles directly to expected temperatures.
* `main.py`: Main gateway orchestrating the lifecycle sequence pipeline.

## Installation & Local Execution

1. Clone this repository structure:
```bash
git clone https://github.com
cd engine-thermal-predictive-ai
```

2. Provision environment requirements:
```bash
pip install -r requirements.txt
```

3. Execute the full end-to-end processing script sequence:
```bash
python main.py
```

4. Verify data processing pipeline functionality locally using regression tests:
```bash
python -m unittest discover -s tests
```



```
engine-thermal-predictive-ai/
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── data/
│   ├── raw_simulation_data.csv
│   └── processed_features.csv
│
├── models/
│   └── thermal_predictor_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py
│   ├── train_model.py
│   └── inference_engine.py
│
├── tests/
│   └── test_pipeline.py
│
├── README.md
├── requirements.txt
└── main.py
```
