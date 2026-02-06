import os
import sys

def RenameExtension(Dirname,Extension1,Extension2):

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
            if(fname.endswith(Extension1)):
                Oldpath=os.path.join(FolderName,fname)
                words=os.path.splitext(fname)
                NewName=words[0] + Extension2

                Newpath=os.path.join(FolderName,NewName)

                os.rename(Oldpath,Newpath)
    fobj.close()
    
def main():

    if len(sys.argv)!=4:
        print("Invalid number of arguments")

    DirNum=sys.argv[1]
    extension1=sys.argv[2]
    extension2=sys.argv[3]

    RenameExtension(DirNum,extension1,extension2)

    print("Renamed file name with first extension to seconfd extension successfully")
    

if __name__=="__main__":
    main()