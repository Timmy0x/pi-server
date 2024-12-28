#!/bin/bash

# Run Python build script with root privileges
echo "Building..."
sudo python build.py

# Install dependencies from requirements.txt with root privileges
echo "Installing dependencies..."
sudo python -m pip install -r requirements.txt

# Run main script with root privileges
echo "Running main application..."
sudo python main.py
