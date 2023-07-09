#!/usr/bin/env python3

import shutil
import subprocess
import os

shutil.rmtree("output", ignore_errors=True)
shutil.rmtree("media", ignore_errors=True)

# get files in testcases folder
testcases = os.listdir("testcases")
os.mkdir("output")
for file in testcases:
    filename_without_extension = file.split(".")[0]
    file = "testcases/" + file
    output = "output/" + filename_without_extension + ".txt"
    subprocess.run(["python", "-m", "cProfile", "-o", output, file])
