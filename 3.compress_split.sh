#!/bin/bash

zip -r compress/output_merged.zip output/output_merged.mp4
zip -s 99m compress/output_merged.zip --out compress/output_split.zip