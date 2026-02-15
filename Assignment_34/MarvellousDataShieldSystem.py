# COMMAND LINE INPUT
import shutil
import sys
import os
import time
import schedule
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

LOG_DIR = "Logs"
HISTORY_FILE = "backup_history.txt"
EXCLUDE_EXT = (".tmp", ".log", ".exe")

# ---------------- LOG SYSTEM ----------------
def create_log():
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    logfile = os.path.join(LOG_DIR, f"BackupLog_{timestamp}.txt")
    return open(logfile, "w"), logfile

# ---------------- ZIP CREATION ----------------
def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "-" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(EXCLUDE_EXT):
                continue
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)
            zobj.write(full_path, relative)

    zobj.close()
    return zip_name

# ---------------- HASH ----------------
def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        hobj.update(data)

    fobj.close()
    return hobj.hexdigest()

# ---------------- BACKUP ----------------
def BackupFiles(Source, Destination, logf):
    Copied_Files = []
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            if file.endswith(EXCLUDE_EXT):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or (
                calculate_hash(src_path) != calculate_hash(dest_path)
            ):
                shutil.copy2(src_path, dest_path)
                Copied_Files.append(relative)
                print("Copied:", relative, file=logf)

    return Copied_Files

# ---------------- EMAIL ----------------
def send_mail(receiver, logfile, zipfile_name):
    msg = EmailMessage()
    msg['Subject'] = "Marvellous Data Shield Backup Report"
    msg['From'] = "nehadgupta2718@gmail.com"       
    msg['To'] = receiver
    msg.set_content("Backup completed successfully.\nLog file attached.")

    with open(logfile, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=logfile)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("nehadgupta2718@gmail.com", "elphsheultghbieh")  # CHANGE
    server.send_message(msg)
    server.quit()

# ---------------- HISTORY ----------------
def update_history(files_count, zipname):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{time.ctime()} | Files: {files_count} | Zip: {zipname}\n")

def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            print(f.read())
    else:
        print("No history found")

# ---------------- RESTORE ----------------
def restore_backup(zipname, destination):
    with zipfile.ZipFile(zipname, 'r') as z:
        z.extractall(destination)
    print("Restore completed")

# ---------------- MAIN BACKUP FUNCTION ----------------
def MarvellousDataShieldStart(Source="Data", receiver=None):
    logf, logfile = create_log()

    print("Backup started at:", time.ctime(), file=logf)

    BackupName = "MarvellousBackup"
    files = BackupFiles(Source, BackupName, logf)

    zip_file = make_zip(BackupName)

    print("Backup completed", file=logf)
    print("Files copied:", len(files), file=logf)
    print("Zip created:", zip_file, file=logf)

    update_history(len(files), zip_file)

    if receiver:
        send_mail(receiver, logfile, zip_file)

    logf.close()

# ---------------- MAIN ----------------
def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        show_history()

    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        restore_backup(sys.argv[2], sys.argv[3])

    elif len(sys.argv) == 4:
        interval = int(sys.argv[1])
        source = sys.argv[2]
        receiver = sys.argv[3]

        schedule.every(interval).minutes.do(MarvellousDataShieldStart, source, receiver)

        print("Data Shield started...")
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("python Script.py 10 Data receiver@gmail.com")
        print("python Script.py --restore zipfile destination")
        print("python Script.py --history")

if __name__ == "__main__":
    main()
