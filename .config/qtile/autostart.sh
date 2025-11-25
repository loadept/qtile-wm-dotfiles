#!/bin/sh

#[Volume Icon]
pasystray -a &

#[Battery Icon]
cbatticon &

#[Networking Applet]
nm-applet &

#[Mounted Disks]
# udiskie -t &

#[Bluetooth Applet]
blueman-applet &
