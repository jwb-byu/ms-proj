#!/bin/bash

# Adapted from a ChatGPT-generated script from February 2025

# Function to ensure the user confirms the cleanup
confirm() {
    read -p "This will remove all Docker containers, images, volumes, and networks. Are you sure? (y/n): " choice
    case "$choice" in
        y|Y ) echo "Proceeding with cleanup...";;
        n|N ) echo "Aborting."; exit 0;;
        * ) echo "Invalid input. Please enter y or n."; confirm;;
    esac
}

# Confirm before running
confirm

# Stop all running containers
echo "Stopping all running containers..."
docker ps -q | xargs -r docker stop

# Remove all containers
echo "Removing all containers..."
docker ps -aq | xargs -r docker rm

# Remove all images
echo "Removing all images..."
docker images -q | xargs -r docker rmi -f

# Remove all volumes
echo "Removing all volumes..."
docker volume ls -q | xargs -r docker volume rm

# Remove all networks
echo "Removing all networks..."
docker network ls -q | xargs -r docker network rm

# Prune unused objects (optional but ensures everything is clean)
echo "Pruning unused objects..."
docker system prune -af --volumes

echo "Docker cleanup complete."
