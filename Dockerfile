# Use the official Python image as the base image
FROM python:3.10.10

# Set the working directory in the container
WORKDIR /app
RUN echo "Working directory set to /app"

# Copy all files excluding the venv directory
COPY . /app
RUN echo "Files copied to /app"

# Install the required Python packages using the Aliyun mirror
RUN pip install -r requirements.txt
RUN echo "Python packages installed"

# Change directory to /app/models and clone the git repository
WORKDIR /app/models
RUN echo "Working directory set to /app/models"
RUN git clone https://huggingface.co/moka-ai/m3e-base
RUN echo "Git repository cloned to /app/models/m3e-base"

# Expose the port that the web service will be running on
EXPOSE 8000
RUN echo "Port 8000 exposed"

# Start the web service using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
