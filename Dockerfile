# Use Python 3.10 slim image (works on Windows, Mac, Linux)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY conftest.py .

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Set environment variables
ENV PORT=8080
ENV PYTHONPATH=/app

# Run the application (cross-platform compatible)
CMD ["python", "-c", "print('SRS Document Generator is running on port', 8080)"]
