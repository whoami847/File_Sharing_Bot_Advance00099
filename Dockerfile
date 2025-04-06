# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "bot.py"]
