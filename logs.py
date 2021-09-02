import json
import os
import sys

import requests


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


os.system("cls" if os.name == "nt" else "clear")

r = requests.get(sys.argv[1], stream=True)

for line in r.iter_lines():
    if line:
        decoded_line = line.decode("utf-8")
        content = json.loads(decoded_line[6:])
        if content["stream_name"] == "stdout":
            print(content["data"][:-1])
        elif content["stream_name"] == "stderr":
            if "[Parallel(n_jobs=-1)]" in content["data"]:
                print(bcolors.OKGREEN + content["data"][:-1] + bcolors.ENDC)
            else:
                print(bcolors.WARNING + content["data"][:-1] + bcolors.ENDC)
