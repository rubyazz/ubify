# Use the official Python image as the base image
FROM python:3.10.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip3 install --no-cache-dir -r requirements/base.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend_pr.wsgi:application"]
