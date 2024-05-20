
## Introduction

- In this course, we will learn how to put Machine Learning to production.
- Best practice for ML project:
  - Design
  - Train
  - Operate

## Environment preparation

### Github codespace

## MLOps maturity model

> [MLOps maturity model](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model)

0. No MLOps
  
    - No automation
    - All codes in Jupyter
    - ***Highlights***
      - Difficult to manage full machine learning model lifecycle.
      - The teams are disparate and releases are painful.
      - Most systems exist as "black boxes" little feedback during/post deployment.
    - ***Technology***
      - Manual builds and deployments
      - Manual testing of model and application.
      - No centrailized tracking of model performance.
      - Training of model is manual.

1. DevOps, No MLOps

    - ***Highlights***
      - Releases are less painful than **No MLOps**, but rely on Data Team for every new model.
      - Still limited feedbacks on how well a model performs in production.
      - Difficult to trace/reproduce results.
    - ***Technology***
      - Automated builds.
      - Automated tests for application code.

2. Automated Training

    - ***Highlights***
      - Training environment is fully managed and traceable.
      - Easy to reproduce model.
      - Releases are manual but low friction.
    - ***Technology***
      - Automated model training.
      - Centralized tracking of model training performance.
      - Model management.

3. Automated Model Deployment

    - ***Highlights***
      - Releases are low friction but automatic.
      - Full traceability from deployment back to original data.
      - Entire environment managed: train > test > production
    - ***Technology***
      - Integrated A/B testing of model performance for deployment.
      - Automated tests for all code.
      - Centralized tracking of model training performance.

4. Full MLOps Automated Operations

    - ***Highlights***
      - Full system automated and easily monitored.
      - Production systems are providing information on how to improve and in some cases automatically improve with new model.
      - Approaching a zero downtime system.
    - ***Technology***
      - Automated model training and testing.
      - Verbose centralized metrics from deployed model.