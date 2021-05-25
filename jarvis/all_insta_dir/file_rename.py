import os 


dir_path = input("Enter the full path of directory to change files from: ")
path = os.chdir(dir_path)
i = 0
new_file = input("Enter the new file name: ")
for file in os.listdir(path):
    new_file_name = new_file+"{}.jpg".format(i)
    
    os.rename(file, new_file_name)
    
    i = i+1
