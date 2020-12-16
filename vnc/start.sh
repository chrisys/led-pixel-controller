#!/bin/bash
# Rename the files to allow for default connection html page
ln -s /noVNC/vnc.html /noVNC/index.html

# Change the default quality and compression (this is available in UI but not on startup it seems)
sed -i 's/this._qualityLevel = 6;/this._qualityLevel = 2;/g' /noVNC/core/rfb.js
sed -i 's/this._compressionLevel = 2;/this._compressionLevel = 0;/g' /noVNC/core/rfb.js

# Start noVNC
exec /noVNC/utils/launch.sh --vnc 172.20.0.4:5900 --listen 80
