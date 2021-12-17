#!/usr/bin/env python3

import subprocess
import random
import os

scripts_folder = os.path.expanduser("~/color-scripts")
random_script = random.choice(random.choices(os.listdir(scripts_folder), k=5))
script_path = os.path.join(scripts_folder, random_script)

subprocess.run(script_path)
