#!/bin/sh

set -e # failsafe
path="$(
    for pid in $(pidof mplayer); do
        ls -l /proc/$pid/fd | awk -v pid=$pid -v dst="$1" '
            BEGIN{
                FS="-> "
            }
            
            !/\/dev\// && !/\/proc\// && !/socket:\[/ && !/pipe:\[/ && $2 && !/tick.mp3$/ && /\.mp3$/{
                print $2
                print "\n" dst > "/proc/" pid "/fd/1"
            }
        '
    done)"

touch "$path"
dirname="$(dirname "$path")"
dest="$dirname/$1"
[ -d "$dest" ] || exit
mv "$path" "$dest"
