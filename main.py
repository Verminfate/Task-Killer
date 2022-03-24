import psutil
import os

procs = []
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processID = proc.pid
        if processName in procs:
            pass
        else:
            procs.append(processName)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

for i in procs:
    print(i)
    os.system("taskkill -F -IM " + i)
