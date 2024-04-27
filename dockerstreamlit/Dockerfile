# Get official Python Docker image
FROM python:3.10.3

# Set working path inside the container
WORKDIR /fastfoot

# Copy whole directoy into the container
COPY . .

# Install all dependencies
RUN pip install -r requirements.txt

# Command to setup the database (one-shot execution) and the streamlit process with desired URL
CMD ["sh", "-c", "python setup_db.py && streamlit run main.py --server.port=8501 --server.address=0.0.0.0 --server.baseUrlPath=/FastFoot/"]