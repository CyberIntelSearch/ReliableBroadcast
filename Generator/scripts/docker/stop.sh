#!/bin/bash

echo ""
echo "Stopping Generator docker container..."
echo ""

cd scripts/docker/
docker-compose down -v

echo ""
echo "Done!"
echo ""