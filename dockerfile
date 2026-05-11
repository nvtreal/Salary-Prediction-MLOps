# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose port 5002 for the Monitoring Dashboard
EXPOSE 5002

# Set the default command to run the Dashboard
CMD ["python", "app.py"]