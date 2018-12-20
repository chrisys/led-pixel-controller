FROM resin/raspberrypi3-debian:stretch

RUN apt-get update && apt-get install -yq \
    x11vnc x11-utils xvfb wmctrl default-jre \
    supervisor python && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . .
ADD supervisor /etc/supervisor

RUN python gled_patch_generator.py > patch.gled

ENTRYPOINT supervisord -c /etc/supervisor/supervisord.conf
