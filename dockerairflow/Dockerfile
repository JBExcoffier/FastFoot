# Get official Airflow Docker image
FROM apache/airflow:2.9.0

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install all dependencies
RUN pip install apache-airflow==2.9.0 -r requirements.txt