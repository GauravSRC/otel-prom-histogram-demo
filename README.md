# otel-prom-histogram-demo

Demo: scrape Prometheus-native histograms from `/metrics` and convert them into OTLP via OpenTelemetry Collector.

## Quick start (PowerShell)
1. `docker compose up --build`  
2. Confirm app metrics: `curl http://localhost:8000/metrics`  
3. Watch collector logs: `docker compose logs -f collector`

This repo contains:
- `server_histogram.py` - example app
- `collector-config.yaml` - otelcol config with native histogram scraping
- `docker-compose.yml` - runs app + collector
- `friction-log.md` - my notes on friction points
