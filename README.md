# Monitoring App

This Python application provides a simple monitoring solution for CPU and Memory usage. The app is designed to be deployed on Amazon EKS (Elastic Kubernetes Service) using Docker containers stored in Amazon ECR (Elastic Container Registry). It is a hands-on project aimed at gaining experience in DevOps practices.

## Technologies Used

- **Amazon EKS**: The application is deployed on a Kubernetes cluster managed by Amazon EKS.

- **Amazon ECR**: Docker images for the application are stored in Amazon ECR for containerized deployments.

- **Python**: The core of the monitoring application is developed in Python.

- **Docker**: The application is containerized using Docker for consistent and scalable deployments.

## Prerequisites

Before deploying the application, ensure you have the following set up:

- Amazon EKS cluster configured and accessible.

- Docker installed locally for building and testing containers.

- AWS CLI configured with the necessary permissions for ECR and EKS.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nawam727/monitoringApp.git
    cd monitoringApp
    ```
2. Run the web app

    ```bash
    python3 app.py
    ```

## Usage

The application automatically monitors CPU and Memory usage within the Kubernetes cluster. You can view logs and metrics through Kubernetes dashboards or use tools like Prometheus and Grafana for more advanced monitoring.

## Contributing

Feel free to contribute to the development of this application by submitting issues or pull requests.
