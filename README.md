# LED Pixel Controller

This project provides a VNC or web-client VNC interface to Glediator, which ultimately allows you to control an array of WS2811 or compatible RGB LED pixels/neopixels via an Adafruit Fadecandy board.

---
## Hardware needed
The project has been built to run on Raspberry Pi 3 or 4 and balenaFin.

* 250 5-volt WS2811 LEDs in the form of 5x 50 LED strings - I got mine [from AliExpress](https://www.aliexpress.com/item/32791781404.html) of course, but Amazon and others carry them too.
* A Raspberry Pi 3B/3B+, 4 or balenaFin (others will likely work too, but probably not the Pi Zero for this project)
* SD Card - 8GB is plenty, but go for the Sandisk Extreme Pro
* A 5V power supply - get the [Mean Well LRS-100-5](https://www.digikey.co.uk/product-detail/en/mean-well-usa-inc/LRS-100-5/1866-3318-ND/7705010)
* An [Adafruit Fadecandy board](https://www.amazon.co.uk/Adafruit-FadeCandy-Dithering-Controlled-Neopixel/dp/B00K9M3VLE)
* [LED string connectors](https://www.amazon.co.uk/MENGCORE%C2%AE-20Pair-20sets-Connector-WS2812B/dp/B01DF0UL8C/ref=pd_bxgy_147_2/258-7672630-7267061) - you can just solder the wires but the connectors are nice for modularity
* Optionally, if you want to print your own case, a 3D printer or 3D printing service to print [the case](https://www.thingiverse.com/thing:3297031) - recommended!


---
## Assembly and building

A full [blog post is published here](https://www.balena.io/blog/control-your-christmas-tree-a-raspberry-pi-powered-rgb-led-matrix-v2/) with a complete tutorial on assembly and setup.

---

## Deployment

This project has been built to be deployed to balenaCloud in order to enable remote access from anywhere and management of multiple devices and updates.

Get started deploying all the software you need by clicking the button below.

[![](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-io-playground/internetspeedtest)

The deployment process will ask you to sign up or sign in to balenaCloud, and then add a device to the application. This will automatically set up your device with all the software required.

---
## Customization

### Different matrix sizes
The project is set up and configured to run with a 25x10 matrix based on 5 folded strings of 50 LEDs each. This is entirely configurable, and there's more information in [this blog post](https://www.balena.io/blog/build-festive-lighting-for-the-holidays-with-balena/) that explains how.

### Scheduler

What good is a light controller if you can’t schedule a simple on and off time?! Set the device service variables below for the `glediator` service within the balenaCloud dashboard to enable automated switching of the lighting. This works by toggling the output of Glediator on and off, so although the device itself will stay powered on and online, the LEDs themselves will turn on and off.

The timer uses cron format to specify times. I recommend using [crontab.guru](https://crontab.guru/) to figure out what you need.

Set the `TIMER_ON` variable to set the on time for your lighting. For example: `0 9 * * *` to turn on at 9AM.

Set the `TIMER_OFF` variable to set the off time for your lighting. For example: `0 2 * * *` to turn off at 2AM.

After you've set your on and off time, set `ENABLE_TIMER` to `1` to enable the timer function, and be sure to set your timezone as below to ensure the times you're setting are in your local time. The default is UTC.

### Timezone

In order for the scheduler to work correctly, you'll of course have to tell the device what timezone you'd like to use. Set the `TZ` environment variable to any [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g. `Europe/London`, `America/Los_Angeles`, `Asia/Taipei` etc.

---

## Credits

This project is made possible by some great free software, both in terms of usage and inspiration:
* [Fadecandy](https://github.com/scanlime/fadecandy)
* [Glediator](https://solderlab.de)
* [noVNC](https://github.com/novnc/noVNC)
* [openpixelcontrol](https://github.com/zestyping/openpixelcontrol)
* [Fadecandy with Glediator](https://github.com/chunk100/Glediator-with-Fadecandy)

Amongst a lot of other supporting software, too!

**Note:** this project includes freely available software (Glediator) from [solderlab.de](https://solderlab.de). At the time of writing the site is currently down and so we have mirrored the download within this project. This will be removed upon request by the author or when the site comes back online.