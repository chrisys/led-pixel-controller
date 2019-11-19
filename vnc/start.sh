#!/bin/bash
# Rename the files to allow for default connection html page
ln -s /noVNC/vnc.html /noVNC/index.html

# Start noVNC
exec /noVNC/utils/launch.sh --vnc 172.20.0.4:5900 --listen 80
