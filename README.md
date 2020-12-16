# Fadecandy RGB LED Pixel Controller

This project provides a VNC or web-client VNC interface to Glediator, which ultimately allows you to control an array of WS2811 or compatible RGB LED pixels/neopixels via an Adafruit Fadecandy board.

The project is set up and configured to run with a 25x10 matrix based on 5 folded strings of 50 LEDs each. This is entirely configurable, and there's more information in [this blog post](https://www.balena.io/blog/build-festive-lighting-for-the-holidays-with-balena/) that explains how.

**Note:** this project includes freely available software (Glediator) from [solderlab.de](https://solderlab.de). At the time of writing the site is currently down and so we have mirrored the download within this project. This will be removed upon request by the author or when the site comes back online.

## Customization

### Scheduler

What good is a light controller if you can’t schedule a simple on and off time?! Set the device service variables below for the `glediator` service within the balenaCloud dashboard to enable automated switching of the lighting. This works by toggling the output of Glediator on and off, so although the device itself will stay powered on and online, the LEDs themselves will turn on and off.

The timer uses cron format to specify times. I recommend using [crontab.guru](https://crontab.guru/) to figure out what you need.

Set the `TIMER_ON` variable to set the on time for your lighting. For example: `0 9 * * *` to turn on at 9AM.

Set the `TIMER_OFF` variable to set the off time for your lighting. For example: `0 2 * * *` to turn off at 2AM.

After you've set your on and off time, set `ENABLE_TIMER` to `1` to enable the timer function, and be sure to set your timezone as below to ensure the times you're setting are in your local time. The default is UTC.

### Timezone

In order for the scheduler to work correctly, you'll of course have to tell the device what timezone you'd like to use. Set the `TZ` environment variable to any [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g. `Europe/London`, `America/Los_Angeles`, `Asia/Taipei` etc.