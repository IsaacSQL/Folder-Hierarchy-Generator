import os
parent_dir = input("Name of parent directory")
directory = input("Name of you main folder")
path = os.path.join(parent_dir, directory)
try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)
sub_folders = int(input("Enter how many folders should be inside: "))
shared_folders = int(input("Enter the number of folders that should be shared across?: "))
shared_folders_names = []
for x in range(shared_folders):
    name_folder = input("Name of "+str(x)+" shared folder:")
    shared_folders_names.append(name_folder)
for x in range(sub_folders):
    sub_folders_names = input("Name of subfolder "+str(x)+"?")
    path = os.path.join(parent_dir, directory, sub_folders_names)
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
        for i in range(len(shared_folders_names)):
            path = os.path.join(parent_dir, directory, sub_folders_names, shared_folders_names[i])
            try:
                os.mkdir(path)
            except:
                print("Folder %s already exists" % path)
    except FileExistsError:
        for i in range(len(shared_folders_names)):
            path = os.path.join(parent_dir, directory, sub_folders_names, shared_folders_names[i])
            try:
                print("Folder %s created!" % path)
                os.mkdir(path)
            except:
                print("Folder %s already exists" % path)
        print("Folder %s already exists" % path)