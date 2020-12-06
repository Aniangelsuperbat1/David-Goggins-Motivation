import random
import os
import sys

path = r"C:\Users\ZhenP\OneDrive\Desktop\David Goggins motivation\Pictures"

files = os.listdir(path)
d = random.choice(files)
os.startfile(d)