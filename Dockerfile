# Use the official Python image as the base image
FROM ibegyourpardon/llm-basic:latest

# Set the working directory in the container
WORKDIR /app
RUN echo "Working directory set to /app"

# Copy all files excluding the venv directory
COPY . /app
RUN echo "Files copied to /app"

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
    && apt-get install -y git-lfs \
    && git lfs install
RUN echo "Git LFS installed"

# Change directory to /app/models and clone the git repository with LFS
WORKDIR /app/models
RUN echo "Working directory set to /app/models"
RUN git lfs clone https://huggingface.co/moka-ai/m3e-base
RUN echo "Git LFS repository cloned to /app/models/m3e-base"

# Expose the port that the web service will be running on
WORKDIR /app
EXPOSE 8000
RUN echo "Port 8000 exposed"

# Start the web service using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
