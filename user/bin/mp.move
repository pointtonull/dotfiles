#!/bin/sh

set -e # failsafe
path="$(for pid in $(pidof mplayer); do ls -l /proc/$pid/fd|awk 'BEGIN{FS="-> "}!/\/dev\//&&!/\/proc\//&&!/socket:\[/&&!/pipe:\[/&&$2{print $2}'; done)"
touch "$path"
dirname="$(dirname "$path")"
dest="$dirname/$1"
[ -d "$dest" ] || mkdir "$dest"
mv "$path" "$dest"
