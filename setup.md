## Setup Instructions

### 1. Prerequisites

* A Google Cloud Project with billing enabled.
* `gcloud` CLI installed and authenticated.
* `kubectl` installed and configured.
* `helm` installed for deploying Prometheus.
* Git and Docker installed.

### 2. Create Cloud Spanner Instance

```bash
gcloud spanner instances create spanner-instance \
  --config=regional-us-central1 \
  --description="Spanner instance" \
  --nodes=1

gcloud spanner databases create products-db \
  --instance=spanner-instance \
  --ddl='CREATE TABLE products (
    product_id STRING(36) NOT NULL,
    name STRING(1024),
    price FLOAT64,
    quantity INT64
  ) PRIMARY KEY(product_id)'
```

### 3. Deploy FastAPI App to GKE

* Build Docker image:

```bash
docker build -t gcr.io/<your-project-id>/fastapi-app .
docker push gcr.io/<your-project-id>/fastapi-app
```

* Apply Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Set Up Monitoring with Prometheus

* Add Prometheus community Helm repo:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

* Install Prometheus Stack:

```bash
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
```

### 5. Access Prometheus UI

* Port forward from Cloud Shell:

```bash
kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090
```

* Open browser and visit: `http://localhost:9090`

If using Cloud Shell and the browser doesn’t open, use the Web Preview feature.
