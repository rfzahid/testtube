import glob2
import datetime

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d")
merge_file = open(filename + ".txt","a+")

file_list = glob2.glob("*.txt")

for i in file_list:
    with open(i, "r") as f:
        merge_file.write(f.read() + "\n")
merge_file.close()
