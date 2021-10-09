#!/bin/bash
docker build -t sparta-v1:latest -f Dockerfile .
docker run -it -p 5000:5000 sparta-v1