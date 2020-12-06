import random
import os
import sys

path = r"C:\Users\ZhenP\OneDrive\Desktop\David Goggins motivation\Pictures"

files = os.listdir(path)
generator = random.choice(files)
os.startfile(generator)