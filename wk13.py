#import OS module
import os

#get the list of files

req_path = os.getcwd()
all_f_ds = os.listdir(req_path)

# define the empty ;ist
req_files = []
for each_files in all_f_ds:
    the_stats = os.stat(each_files)
    the_path = os.path.abspath(each_files)

    req_files.append(each_files)
    req_files.append(the_path)
    req_files.append(the_stats.st_size)

print(*req_files,sep='\n')

    
