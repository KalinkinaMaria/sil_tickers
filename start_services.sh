#!/bin/bash

if (! docker stats --no-stream &> /dev/null); then
    echo "Docker is not running on your computer. Start docker application and run script again."
    exit
fi

docker-compose up -d