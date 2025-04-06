# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Set the environment variable for the bot token
ENV BOT_TOKEN=your_bot_token

# Run the bot
CMD ["python", "bot.py"]
