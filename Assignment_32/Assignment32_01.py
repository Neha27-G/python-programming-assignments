import os
import sys
import hashlib


def CalculateChecksum(Filename):
    hobj = hashlib.md5()

    fobj = open(Filename, "rb")
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DisplayCheckSum(DirName):
    Border = "-" * 70

    fobj = open("LogFile1.log", "w")
    fobj.write(f"{Border}\n")
    fobj.write("-------------------------Welcome to Log File----------------------------\n")
    fobj.write(f"{Border}\n")

    if os.path.exists(DirName) == False:
        print(f"{DirName} doesn't exist")
        fobj.close()
        return

    if os.path.isdir(DirName) == False:
        print(f"{DirName} is not a directory")
        fobj.close()
        return

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Ret = CalculateChecksum(fname)
            fobj.write(f"Checksum of {fname} is : {Ret}\n")

    fobj.write(f"{Border}\n")
    fobj.write("-------------------------------Thank youuu!!---------------------------\n")
    fobj.write(f"{Border}\n")

    fobj.close()


def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        print("Usage : python Assignment32_01.py DirectoryName")
        return

    DirName = sys.argv[1]
    DisplayCheckSum(DirName)


if __name__ == "__main__":
    main()
