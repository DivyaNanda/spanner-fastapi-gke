# Spanner FastAPI GKE Demo

This is quick leanring hands On which demonstrates deploying 
a FastAPI backend on Google Kubernetes Engine (GKE) with Cloud Spanner as the backend database. It also includes basic Prometheus monitoring setup.

## Features

- RESTful API built with FastAPI
- Google Cloud Spanner as the scalable backend database
- Containerized using Docker
- Deployed on Google Kubernetes Engine (GKE)
- Integrated with Prometheus for metrics and monitoring

## Architecture

1. FastAPI application connects to Cloud Spanner
2. Deployed to GKE via Kubernetes manifests
3. Prometheus deployed to monitor GKE
