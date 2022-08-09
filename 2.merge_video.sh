#!/bin/bash

./ffmpeg/ffmpeg -r 30 -f image2 -i ./Anime-Super-Resolution/outputs/sr_%08d.png ./output/output.mp4
./ffmpeg/ffmpeg -i ./output/output.mp4 -i ./input/input.mp4 -c:v copy -c:a aac -strict experimental ./output/output_merged.mp4


./ffmpeg/ffmpeg -r 30 -f image2 -i ./Real-CUGAN/finish/%08d.png ./output/output.mp4
./ffmpeg/ffmpeg -i ./output/output.mp4 -i ./input/input.mp4 -c:v copy -c:a aac -strict experimental ./output/output_merged.mp4