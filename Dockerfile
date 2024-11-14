# # Use an official Python image
# FROM ubuntu:latest

# # Update apt package list and install python3 and pip3
# RUN apt-get update && \
#     apt-get install -y python3 python3-pip git && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file to install dependencies
# COPY requirements.txt .

# # Install dependencies
# RUN pip3 install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose the port that Gradio will run on (usually 7860)
# EXPOSE 7860

# # Command to run the Gradio application
# CMD ["python3", "agency.py"]
# # CMD ["entrypoint.sh"]


# Use an official Ubuntu image
FROM ubuntu:latest

# Update apt package list and install Python3, pip3, and venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Create a virtual environment and install dependencies within it
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Gradio will run on (usually 7860)
EXPOSE 7860

# Activate the virtual environment and start the Gradio application
CMD ["/app/venv/bin/python", "agency.py"]
