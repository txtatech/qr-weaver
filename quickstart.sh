#!/bin/bash

# Stop the script if any command fails
set -e

# Execute the Python scripts in the correct order
echo "Running qr_weaver_vid.py..."
python3 qr_weaver_vid.py

echo "Running qr_weaver_gif.py..."
python3 qr_weaver_gif.py

echo "Running qr_weaver_decode.py..."
python3 qr_weaver_decode.py

echo "All scripts executed successfully."
