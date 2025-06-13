# This file (and the associated ../.devcontainer/devcontainer.json file) is adapted from
# similar files used in my prior academic and industry work. Those files and this file may
# have been developed with the help of LLM's like ChatGPT

# Use a base image with Python 3.13 (or another compatible version)
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off

# Install necessary system dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    curl \
    git \
    qtbase5-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --upgrade pip setuptools
