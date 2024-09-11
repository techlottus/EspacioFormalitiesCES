FROM python:3.10-slim-buster

COPY . /app

WORKDIR /app

RUN apt update && apt upgrade -y && apt-get install -y cmake
RUN apt install python3-dev build-essential -y
RUN apt-get install zbar-tools pkg-config -y
RUN apt-get install sox ffmpeg libcairo2 libcairo2-dev -y

RUN pip install -r requirements.txt

# DATADOG
COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init
RUN pip install --target /dd_tracer/python/ ddtrace
# DATADOG

# DATADOG
ENV DD_SERVICE=Espacio-ExtractBanner
ENV DD_ENV=develop
ENV DD_VERSION=1
ENV DD_DBM_PROPAGATION_MODE=full
ENV DD_LOGS_INJECTION=true
ENV DD_LOGS_ENABLED=true
ENV DD_TRACE_128_BIT_TRACEID_GENERATION_ENABLED=true
# DATADOG

# Bind to all network interfaces so that it can be mapped to the host OS
# ENV HOST=0.0.0.0 PORT=80
# CMD ["python", "app.py"]
CMD ["/dd_tracer/python/bin/ddtrace-run", "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
