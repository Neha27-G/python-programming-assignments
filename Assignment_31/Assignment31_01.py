import os
import sys

def DirectoryfileSearch(Dirname,Extension):

    fobj=open("Assignmt31.log","w")

    Ret=os.path.exists(Dirname)
    if(Ret==False):
        fobj.write("Directory Does not Exist")
        return
    
    Ret=os.path.isdir(Dirname)
    if(Ret==False):
        fobj.write(f"{Dirname} is not a directory")
        return
    
    for FolderName,SubFolder,Filename in os.walk(Dirname):
        for fname in Filename:
            if(fname.endswith(Extension)):
                fobj.write("File name :"+fname+"\n")

    fobj.close()
    
def main():

    if len(sys.argv)!=3:
        print("Invalid number of arguments")

    DirNum=sys.argv[1]
    extension=sys.argv[2]
    DirectoryfileSearch(DirNum,extension)

if __name__=="__main__":
    main()