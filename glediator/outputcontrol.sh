#!/bin/bash
while [[ -z $windowid ]]
do
    windowid=$(xdotool search --name "GLEDIATOR - Graphical LED Installation AnimaTOR")
done

echo 'Window ID found: '$windowid
sleep 0.5

# the window header (to make sure it's active)
xdotool mousemove --window $windowid 80 10
xdotool click 1
# the options menu
xdotool mousemove --window $windowid 80 35
xdotool click 1
# the output option
xdotool mousemove --window $windowid 100 76
xdotool click 1

while [[ -z $outputwindowid ]]
do
    outputwindowid=$(xdotool search --name "Output Options")
done

echo 'Output Window ID found: '$outputwindowid
sleep 0.5

if [[ $1 == "start" ]]; then
    echo 'Starting output'
    # the open socket button
    xdotool mousemove --window $outputwindowid 315 224
elif [[ $1 == "stop" ]]; then
    echo 'Stopping output'
    # the close socket button
    xdotool mousemove --window $outputwindowid 455 224
fi

xdotool click 1
sleep 0.5
# the done button
xdotool mousemove --window $outputwindowid 445 305
xdotool click 1