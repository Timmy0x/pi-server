#!/bin/bash

# Run Python build script with root privileges
echo "Building..."
sudo python3 build.py

# Install dependencies from requirements.txt with root privileges
echo "Installing dependencies..."
sudo python3 -m pip install -r requirements.txt

# Run main script with root privileges
echo "Running main application..."
sudo python3 main.py
