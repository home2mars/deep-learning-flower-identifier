import os
tdata_dir='/path/to/zip/file'
os.chdir(tdata_dir)
# Make a list to store image file paths
imgpth = []
for dirnm in os.listdir("."):
    if dirnm != '.DS_Store':
        imgdir = os.path.join(tdata_dir, dirnm)
        imgpth.append(imgdir)

# Rename image files & remove unwanted files
for dirnm in imgpth:
    os.chdir(dirnm)
    for fnm in os.listdir("."):
        pos = fnm.find('. ')
        os.rename(fnm, fnm[pos+2:])
        if fnm in ('.jpg', 'DS_Store'):
            os.remove(fnm)

# Print out image file paths for visual inspection
for dirnm in imgpth:
    print('**',dirnm)
    os.chdir(dirnm)
    for fnm in os.listdir("."):
        print('    ',fnm)
