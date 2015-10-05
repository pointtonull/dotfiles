#!/bin/sh

#set -ev # failsafe

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
        [ "$3-" = "kill-" ] && kill $pid > /dev/null
    done

    )"

touch "$path"
dirname="$(dirname "$path")"
dest="$dirname/$1"
[ -d "$dest" ] || exit
mv "$path" "$dest"
up_count="$(ls $dirname/ascender/*.mp3 | wc -l)"
this_count="$(ls $dirname/*.mp3 | wc -l)"
down_count="$(ls $dirname/descender/*.mp3 | wc -l)"
notify-send -t 1000 -i $2 "$2" "Down $down_count - $this_count - $up_count Up"
