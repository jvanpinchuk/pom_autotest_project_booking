#!/bin/bash

# Get the current script directory
SCRIPT_DIR=$(dirname "$0")

# Run allure using relative path to reports file in tests directory
allure serve "$SCRIPT_DIR/../tests/reports"
