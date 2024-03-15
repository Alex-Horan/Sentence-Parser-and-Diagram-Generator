import subprocess
import os
import time

def startApp():
    f = subprocess.Popen(["../App/bin/python3 -m flask --app FlaskServer run"], shell=True)
    if f.poll() is None:
        print("[+] The Flask server has started successfully.")
        e = subprocess.Popen(["npm start"], shell=True)
        if e.poll() is None:
            print("Electron/React app has started successfully.")
        else:
            print("Electron/React app has failed to start")
            input("Press <Enter> to exit...")
            exit()
    else:
        print("The Flask server failed to start.")
        input("Press <Enter> to exit...")
        exit()

    while f.poll() is None:
        time.sleep(0.5)
    
    exit()
    # if result.returncode != 0:
    #     print("Failed to start Flask Server")
    #     input("Press <Enter> to exit...")
    #     exit()
    # else:
    #     print("yoop")
    #     pass
    # print("Flask server has started")
    # appStart = subprocess.run(["npm start"], shell=True, capture_output=True)
    # if appStart.returncode != 0:
    #     print("Failed to start Electron app.")
    #     input("Press <Enter> to exit...")
    #     exit()
    # else:
    #     pass

startApp()