# Friction log

Date: 2026-02-10

What I tried:
I followed the demo instructions and ran docker compose up --build -d from the project root to start the Python app, the OpenTelemetry Collector (collector), and the backend collector. After starting the compose stack I tried to verify the setup by curling the app metrics at http://localhost:8000/metrics from PowerShell and by inspecting the collector and backend logs with docker logs otel_collector and docker logs otel_backend.

What happened:
The collector container repeatedly failed to load the configuration and logged the same decoding error: the logging exporter is deprecated and must be replaced (the exact message was: 'exporters' the logging exporter has been deprecated, use the debug exporter instead). Because the collector could not parse its config it did not run properly. A subsequent curl http://localhost:8000/metrics from the host returned “Unable to connect to the remote server”, indicating the application was not reachable (the app container either did not start or was not accessible on localhost from the host). Finally, docker logs otel_backend returned “Error response from daemon: No such container: otel_backend”, so the backend container was not running or had been removed by Docker after the compose failure.

Why it's confusing:
At first glance this looked like a networking issue (the curl failure suggested the app was not reachable), but the collector logs clearly show a configuration parsing error that prevents the collector from starting. Because the collector fails on startup, the whole pipeline cannot progress and dependent containers may not be healthy or started as expected. The deprecation message about the logging exporter is not obvious if you are following older examples or online guides that still use logging. It is also confusing that the host curl fails while the app is defined in compose; this can be caused by the app container not being created due to compose failing earlier, or by the app failing to start during build/run. The absence of the backend container confirms the compose stack did not end up in the desired running state.

How I fixed/mitigated:
I diagnosed the root cause from the collector logs and prepared the following corrective actions to resolve the immediate failures and re-run the demo:
