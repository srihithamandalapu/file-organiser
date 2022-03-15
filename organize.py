from commonFiles import commonFiles;

import shutil;
from os import listdir, makedirs, startfile;
from os.path import isfile, join;
import json

from tkinter import filedialog
from tkinter import *

with open("extensions.json") as f:
    extensions = json.load(f)

def chooseFolder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected;

def getFileExtension(fileName):
    fileType = ('.' + fileName.split(".")[-1]).upper();
    return extensions[fileType] if fileType in extensions else "Unknown";

def createFolder(folderName):
    try:
        makedirs(folderName);
    except FileExistsError:
        pass;

def moveFile(source, destination):
    shutil.move(source, destination);

def isCommonFile(fileName):
    return fileName.lower() in commonFiles;

def organize(folderName):
    for file in listdir(folderName):
        if isfile(join(folderName, file)):
            fileExtension = getFileExtension(file);
            path = '';
            if fileExtension != "Unknown":
                fileType = fileExtension['type'];
                fileDescription = fileExtension['description'];
                if(isCommonFile(fileType)):
                    path = join(folderName, fileType);
                else:
                    path = join(folderName, fileType, fileDescription);
            else:
                path = join(folderName, 'MISC');
            
            createFolder(path);
            moveFile(join(folderName, file), join(path, file));

folderName = chooseFolder();
organize(folderName);
startfile(folderName);

