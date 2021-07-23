#!/bin/bash
# Rename the files to allow for default connection html page
ln -s /noVNC/vnc.html /noVNC/index.html

# Set hostname
curl -X PATCH --header "Content-Type:application/json" \
    --data '{"network": {"hostname": "led-pixel-controller"}}' \
    "$BALENA_SUPERVISOR_ADDRESS/v1/device/host-config?apikey=$BALENA_SUPERVISOR_API_KEY"

# Start noVNC
exec /noVNC/utils/launch.sh --vnc 172.20.0.4:5900 --listen 80
