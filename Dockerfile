# Base image
FROM python:3.9-slim

# Install build dependencies required for building tgcrypto and other extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev \
    libssl-dev \
    liblzma-dev \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "bot.py"]
