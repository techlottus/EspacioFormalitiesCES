FROM python:3.10.1-alpine3.15
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
# Bind to all network interfaces so that it can be mapped to the host OS
ENV HOST=0.0.0.0 PORT=80
CMD ["python", "app.py"]