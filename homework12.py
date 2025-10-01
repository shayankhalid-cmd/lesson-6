import os
shutdown = input("are you sure you want to shutdown your computer? yes/no:")
if shutdown=="no":
    exit()
else:
    os.system("shutdown /s /t 1")