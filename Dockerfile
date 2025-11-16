# --- Stage 1: Use an official Python runtime as a parent image ---
# Using a 'slim' image is a good practice to keep the final image size smaller.
FROM python:3.9-slim

# --- Stage 2: Set the working directory inside the container ---
# This is where our application code will live.
WORKDIR /app

# --- Stage 3: Copy dependency file and install dependencies ---
# We copy only the requirements file first to take advantage of Docker's layer caching.
# If requirements.txt doesn't change, Docker won't re-run this step on subsequent builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 4: Copy the rest of the application code ---
# Now copy the application source code into the container's working directory.
COPY . .

# --- Stage 5: Expose a port ---
# Inform Docker that the container listens on port 5000 at runtime.
EXPOSE 5000

# --- Stage 6: Define the command to run the application ---
# This is the command that will be executed when the container starts.
CMD ["python", "app.py"]