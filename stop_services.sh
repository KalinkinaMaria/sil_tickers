#!/bin/bash

if (! docker stats --no-stream &> /dev/null); then
    echo "Docker is not running on your computer. You don't need to stop services."
    exit
fi

docker-compose down