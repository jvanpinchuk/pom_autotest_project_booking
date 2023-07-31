#!/bin/bash

# Get the current script directory
SCRIPT_DIR=$(dirname "$0")

# Determine the path to the test file relative to the directory with the script
TEST_FILE="$SCRIPT_DIR/../tests/test_ui_booking.py/"

# Determine the path to the directory with reports relative to the directory with the script
REPORT_DIR="$SCRIPT_DIR/../tests/reports"

# Run pytest using relative path to test_my_project.py file and reports directory
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"
