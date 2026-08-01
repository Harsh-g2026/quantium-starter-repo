#!/bin/bash

# Activate virtual environment (Windows Git Bash path)
source venv/Scripts/activate

# Execute test suite
pytest test_app.py

# Capture exit code and return it
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi