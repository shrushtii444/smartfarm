#use official python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
