# Use the official Python image as the base image
FROM python:3.10.10

# Set the working directory in the container
WORKDIR /app

# Copy all files excluding the venv directory
COPY . /app

# Install the required Python packages using the Aliyun mirror
RUN pip install --no-cache-dir -r requirements.txt --index-url=https://mirrors.aliyun.com/pypi/simple/

# Expose the port that the web service will be running on
EXPOSE 8000

# Start the web service using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
