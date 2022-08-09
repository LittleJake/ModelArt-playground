#!/bin/bash

./ffmpeg/ffmpeg -i ./input/input.mp4 -r 30 -f image2 ./Anime-Super-Resolution/inputs/%08d.png
cp ./Anime-Super-Resolution/inputs/* ./Real-CUGAN/pending/