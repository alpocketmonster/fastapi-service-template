# Fast API Service

## Launch

### Set up
```bash
pip install -r requirements.txt -c constraints.txt
```

### Run app

```bash
python -m app
```

или 

запустить __main__.py

### Run tests

```bash
pytest
```

или с покрытием

```bash
pytest --cov=./ --cov-branch
```

## Settings 
```bash
LOG_LEVEL = "INFO"
PORT = 8080

ECS_LOGGING_USE = false

SENTRY_USE = false
SENTRY_DSN = ""

METRICS_USE = true

HEALTHCHECK_USE = true
```
