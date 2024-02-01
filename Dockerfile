# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY ./api /usr/src/app/api

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "api.FBScrapperApi:app", "--host", "0.0.0.0", "--port", "80"]
