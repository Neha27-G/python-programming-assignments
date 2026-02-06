import hashlib
import os
import sys

def FileChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024) # 1kb = 1024 bytes

    while( len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DisplayDuplicate(Directory):

    fobj = open("logFile3.log","w")

    fobj.write("------------------Log file for Assignmnet 3---------------------\n")
    fobj.write("-----------Automation script for deleting duplicate files-------\n")

    if(os.path.exists(Directory) == False):
        fobj.write(f"{Directory} directory does not exist\n")
        return

    if(os.path.isdir(Directory) == False):
        fobj.write(f"{Directory} is not directory\n")
        return
    
    Duplicate = {}
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Checksum = FileChecksum(fname)

            if(Checksum in Duplicate):
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    Result = list(filter((lambda x: (len(x)>1)), Duplicate.values()))

    fobj.write("Deleted Files are : \n")
    cnt=0
    for values in Result:
        for i in values:
            fobj.write(f"{i}\n")
            os.remove(i)
            cnt=cnt+1
    fobj.write(f"Total deleted files : {cnt}")

    fobj.close()

def main():
   
    if(len(sys.argv) !=2 ):
        print("Invalid number of argumnets\n")
        return

    DirNm = sys.argv[1]
    DisplayDuplicate(DirNm)


if __name__ == "__main__":
    main()