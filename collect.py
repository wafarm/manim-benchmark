#!/usr/bin/env python3

import shutil
import sys
import os

if len(sys.argv) != 2:
    print("Error: Please provide the data type.")

data_type = sys.argv[1]
os.makedirs(f"result/{data_type}", exist_ok=True)

testcases = os.listdir("output")
for testcase in testcases:
    shutil.copy(f"output/{testcase}", f"result/{data_type}/{testcase}")

os.mkdir("videos")
os.mkdir(f"videos/{data_type}")

videos = os.listdir("media/videos/720p30")
for video in videos:
    if video.endswith(".mp4"):
        shutil.copy(f"media/videos/720p30/{video}", f"videos/{data_type}/{video}")