# File: Dockerfile

# --- Stage 1: Base Image ---
# Start from an official, lightweight Python image. 'slim' is a good choice for production.
FROM python:3.9-slim

# --- Stage 2: Set Working Directory ---
# Set a directory inside the container where our code will live.
WORKDIR /app

# --- Stage 3: Install Dependencies ---
# Copy ONLY the requirements file first. This leverages Docker's layer caching.
# If this file doesn't change, Docker will reuse this layer, making future builds faster.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 4: Copy Application Code ---
# Now, copy the rest of the application files into the working directory.
COPY . .

# --- Stage 5: Expose Port ---
# Inform Docker that the application inside the container will listen on port 5000.
EXPOSE 5000

# --- Stage 6: Define Runtime Command ---
# Specify the command to run when a container is started from this image.
CMD ["python", "app.py"]