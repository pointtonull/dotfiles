#!/bin/sh
./update.py
git add user
git commit -m "updated user files"
git add system
git commit -m "updated systeam files"
git commit -am "updated dotfiles repo"
git push
