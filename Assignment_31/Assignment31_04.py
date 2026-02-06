import os
import sys

def CopyFile(Dirname1,Dirname2,extension):

    Ret1=os.path.exists(Dirname1)
    Ret2=os.path.exists(Dirname2)

    if(Ret1==False):
        print(f"{Dirname1} does not exist")

    if(os.path.isdir(Dirname1)==False):
        print(f"{Dirname1} is not a directory")
        return

    if(Ret1==True and Ret2==True):
        print(f"{Dirname2} already exist")
        return
    
    os.mkdir(Dirname2)
    print(f"{Dirname2} created successfully")

    for FolderName,SubFolder,Filename in os.walk(Dirname1):
        for fname in Filename:
            dirpath1=os.path.join(FolderName,fname)
            dirpath2=os.path.join(Dirname2,fname)

            obj1=open(dirpath1,"r")
            
            Dat=None

            if(fname.endswith(extension)):
                Data=obj1.read()
                obj2=open(dirpath2,"w")
                obj2.write(Data)
                obj2.close()
    
            obj1.close()
    
    
def main():

    if len(sys.argv)!=4:
        print("Invalid number of arguments")

    DirNme1=sys.argv[1]
    DirNme2=sys.argv[2]
    extension=sys.argv[3]

    CopyFile(DirNme1,DirNme2,extension)

    print("Files content created successfully")
    

if __name__=="__main__":
    main()