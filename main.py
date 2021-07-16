#!/usr/bin/env python3

import subprocess
import random
import os

scripts_folder = os.path.expanduser("~/color-scripts")
files = os.listdir(scripts_folder)
script_file_path = os.path.join(scripts_folder, random.choice(random.choices(files, k=5)))

subprocess.run(script_file_path)
