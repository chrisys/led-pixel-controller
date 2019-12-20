#!/bin/bash
if [[ -z $PATTERN_PRESET ]]; then
  echo 'No pattern preset specified - using default'
  cp /root/rainbowrain.gled /usr/src/app/autoSave.gled
else
  echo 'Using pattern preset '$PATTERN_PRESET
  cp /root/$PATTERN_PRESET.gled /usr/src/app/autoSave.gled
fi

exec supervisord -c /etc/supervisor/supervisord.conf