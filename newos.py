import os

os.getcwd()
os.chdir("/home/ubuntu")
os.makedirs("dir1",exist_ok=True)

for path,dir,files in os.walk("/home/ubuntu/dir1"):
    print(path,dir,files)

