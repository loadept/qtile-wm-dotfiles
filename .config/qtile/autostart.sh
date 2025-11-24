#!/bin/sh

#[Battery Icon]
cbatticon &

#[Volume Icon]
pasystray &

#[Networking Applet]
nm-applet &

#[Mounted Disks]
# udiskie -t &

#[Bluetooth Applet]
blueman-applet &
