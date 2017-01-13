import glob
import os

os.chdir("/home/chaitalikelsukar/Downloads/")
filename_arr={}
i=0
for files in glob.glob("*.png"):
    filename_arr[i] = files
    i= i+1

for key,value in filename_arr.items():
    print key , value
