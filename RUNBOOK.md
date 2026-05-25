# Runbook

## Kubernetes defaults
- Release: `insiderone-api`
- Example namespace: `default`

## Check app health
- Local:
  ```bash
  curl http://localhost:8000/healthz
  curl http://localhost:8000/ping
  ```
- Kubernetes:
  ```bash
  kubectl -n default get pods
  kubectl -n default port-forward svc/insiderone-api 8000:8000
  curl http://localhost:8000/healthz
  ```

## View logs locally with Docker Compose
```bash
docker compose logs -f app
```

## View Kubernetes pod logs
```bash
kubectl -n default get pods
kubectl -n default logs -f deploy/insiderone-api
```

## Restart the app in Kubernetes
```bash
kubectl -n default rollout restart deploy/insiderone-api
kubectl -n default rollout status deploy/insiderone-api
```

## Roll back with Helm
```bash
helm -n default history insiderone-api
helm -n default rollback insiderone-api <REVISION>
```

## Check Prometheus targets
- Open `http://localhost:9090/targets`
- Confirm job `fastapi` is `UP`

## Access Grafana
- URL: `http://localhost:3000`

## If `/ping` fails
- Check the app is running: `docker compose ps` or `kubectl -n default get pods`
- Check logs: `docker compose logs -f app` or `kubectl -n default logs -f deploy/insiderone-api`
- Verify port access: local `8000`, or re-run Kubernetes port-forward
- If probes keep failing in Kubernetes, restart the deployment and inspect events:
  ```bash
  kubectl -n default describe pod <pod-name>
  ```

## If `/metrics` is not scraped
- Confirm the endpoint responds:
  ```bash
  curl http://localhost:8000/metrics
  ```
- Check Prometheus targets page shows `fastapi` as `UP`
- Verify `monitoring/prometheus.yml` still targets `app:8000`
- Restart the local stack if needed:
  ```bash
  docker compose up --build
  ```
