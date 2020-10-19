# a test of ssh and cron

import os

os.system('date > temp.txt')
os.system('git add .')
os.system('git commit -m "add test')
os.system('git push')
