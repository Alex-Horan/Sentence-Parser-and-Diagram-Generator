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
    

    k = subprocess.run(["npx kill-port --port 1212, 5000"], shell=True, capture_output=True)
    if k.returncode != 0:
        print("Failed to kill electron app running on port 1212 and Flask server running on port 5000")
        exit()
    else:
        print("Successfully exited app!")
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