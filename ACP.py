import os


shutdown = input("Do you wish to shutdown your computer ? (Yes or No):")

if shutdown == 'no':
    exit()
else:
    os.system("Shutdown  /s /t 1")