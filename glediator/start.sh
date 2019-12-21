#!/bin/bash
if [[ -z $PATTERN_PRESET ]]; then
  echo 'No pattern preset specified - using default'
  cp /root/rainbowrain.gled /usr/src/app/autoSave.gled
else
  echo 'Using pattern preset '$PATTERN_PRESET
  cp /root/$PATTERN_PRESET.gled /usr/src/app/autoSave.gled
fi

if [ ! -z ${ENABLE_TIMER+x} ] && [ "$ENABLE_TIMER" -eq "1" ]
then
  (crontab -l; echo "${TIMER_ON:-0 8 * * *} /usr/src/app/scripts/scheduler_on.sh") | crontab -
  (crontab -l; echo "${TIMER_OFF:-0 23 * * *} /usr/src/app/scripts/scheduler_off.sh") | crontab -
fi

exec supervisord -c /etc/supervisor/supervisord.conf