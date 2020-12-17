#!/bin/sh

#set -ev # failsafe

path="$(
    for pid in $(pidof mplayer); do
        ls -l /proc/$pid/fd | awk -v pid=$pid -v dst="$1" '
            BEGIN{
                FS="-> "
            }

            !/\/dev\// && !/\/proc\// && !/socket:\[/ && !/pipe:\[/ && $2 && !/tick.mp3$/ && /\.m..$/{
                print $2
                print "\n-------------------- " dst "\n" > "/proc/" pid "/fd/1"
            }
        '

        [ "$3-" = "kill-" ] && kill $pid > /dev/null
        kill $pid > /dev/null #TODO: Remove after intense selection

    done

    )"

touch "$path"
dirname="$(dirname "$path")"
dest="$dirname/$1"
[ -d "$dest" ] || exit
mv "$path" "$dest"

up_count="$(ls $dirname/ascender/*.m* | wc -l)"
this_count="$(ls $dirname/*.m* | wc -l)"
down_count="$(ls $dirname/descender/*.m* | wc -l)"

notify-send -t 1000 -i $2 "$2" "Down $down_count - $this_count - $up_count Up"
