# COMMAND LINE INPUT
import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

# ----------------------------------------------------
def SendMail(LogFile, ReceiverMail):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Marvellous Platform Surveillance System Report"
        msg['From'] = "nehadgupta2718@gmail.com"
        msg['To'] = ReceiverMail

        msg.set_content("Please find attached platform surveillance system log file.")

        with open(LogFile, "rb") as f:
            file_data = f.read()

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(LogFile)
        )

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("nehadgupta2718@gmail.com", "elphsheultghbieh")
        server.send_message(msg)
        server.quit()

    except Exception as e:
        print("Unable to send email :", e)

# ----------------------------------------------------
def CreateLog(FolderName):
    Border = "-" * 90

    if os.path.exists(FolderName) == False:
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("---------------- Marvellous Platform Surveillance System ----------------\n")
    fobj.write("Log file created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    # ---------------- SYSTEM INFORMATION ----------------
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border + "\n")

    fobj.write("Disk Usage Report\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    net = psutil.net_io_counters()
    fobj.write("Network Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Network Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n\n")

    # ---------------- PROCESS INFORMATION ----------------
    Data = ProcessScan()

    for info in Data:
        fobj.write("Process Name : %s\n" % info.get("name"))
        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
        fobj.write("Memory RSS : %.2f MB\n" % info.get("rss"))
        fobj.write("Memory VMS : %.2f MB\n" % info.get("vms"))
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write("Threads Count : %s\n" % info.get("threads"))
        fobj.write("Open Files Count : %s\n" % info.get("open_files"))
        fobj.write("Timestamp : %s\n" % time.ctime())
        fobj.write(Border + "\n")

    # ---------------- TOP 10 MEMORY CONSUMING PROCESSES ----------------
    fobj.write("\nTop 10 Memory Consuming Processes (RSS)\n")
    fobj.write(Border + "\n")

    Data.sort(key=lambda x: x.get("rss"), reverse=True)
    Top10 = Data[:10]

    for info in Top10:
        fobj.write("Process Name : %s\n" % info.get("name"))
        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("Memory RSS : %.2f MB\n" % info.get("rss"))
        fobj.write(Border + "\n")

    fobj.write("End of Log File\n")
    fobj.write(Border + "\n")


    fobj.close()

    # Send email after log creation
    SendMail(FileName, sys.argv[2])

# ----------------------------------------------------
def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = {}

            info["pid"] = proc.pid
            info["name"] = proc.name()

            info["cpu_percent"] = proc.cpu_percent(interval=0.1)
            info["memory_percent"] = proc.memory_percent()

            mem = proc.memory_info()
            info["rss"] = mem.rss / (1024 * 1024)
            info["vms"] = mem.vms / (1024 * 1024)

            info["threads"] = proc.num_threads()

            try:
                info["open_files"] = len(proc.open_files())
            except psutil.AccessDenied:
                info["open_files"] = "Access Denied"

            listprocess.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return listprocess

# ----------------------------------------------------
def main():
    Border = "-" * 90
    print(Border)
    print("Marvellous Platform Surveillance System")
    print(Border)

    # Usage:
    # PlatformSurveillance.py LogDirectory ReceiverEmail TimeInterval
    if len(sys.argv) == 4:
        print("Directory Name :", sys.argv[1])
        print("Receiver Email :", sys.argv[2])
        print("Time Interval (minutes) :", sys.argv[3])

        schedule.every(int(sys.argv[3])).minutes.do(CreateLog, sys.argv[1])

        print("Platform Surveillance System Started")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid command line arguments")
        print("Usage : PlatformSurveillance.py LogDirectory ReceiverEmail TimeInterval")

# ----------------------------------------------------
if __name__ == "__main__":
    main()
