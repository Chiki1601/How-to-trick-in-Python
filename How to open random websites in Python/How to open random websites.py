#python prank program

import random
import time
import webbrowser
while True:
    sites = random.choice(['google.com','instagram.com','github.com','youtube.com','leetcode.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randint(2,5)
    time.sleep(seconds)
