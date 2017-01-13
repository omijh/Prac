import os

# This is the path where you want to search
path = r'/home/chaitalikelsukar/Downloads/'  

# this is extension you want to detect
extension = '.png'   # this can be : .jpg  .png  .xls  .log .....
#f is the file name to write too
f=open("newfile.csv","w")
f.write("name,path\n")
for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
	    f.write("%s,%s\n"%(file_name,file_name_path))
            print file_name
            print file_name_path 
f.close()
