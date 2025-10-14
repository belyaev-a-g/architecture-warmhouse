# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --proxy 172.16.0.250:4343 --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 8080
#EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

