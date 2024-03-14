import subprocess
import os

def startApp():
    result = subprocess.Popen(["../App/bin/python3 -m flask --app FlaskServer run;"], shell=True, stdout=subprocess.PIPE)
    code = result.communicate()
    if code.returncode != 0:
        print("Failed to start Flask Server")
        input("Press <Enter> to exit...")
        exit()
    else:
        print("Flask server has started")
        appStart = subprocess.run(["npm start"], shell=True, capture_output=True)
        if appStart.returncode != 0:
            print("Failed to start Electron app.")
            input("Press <Enter> to exit...")
            exit()
        else:
            pass

startApp()