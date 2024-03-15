import subprocess
import os

def startApp():
    result = subprocess.run(["../App/bin/python3 -m flask --app FlaskServer run;"], shell=True, capture_output=True)
    if result.returncode is None:
        print("flask server is running and is executing")
        pass
        # print("Failed to start Flask Server")
        # input("Press <Enter> to exit...")
        # exit()
    elif result.returncode != 0:
        print("Flask server failed to start")
        input("Press <Enter> to exit...")
        exit()
    else:
        print("flask server has closed")
        input("Press <Enter> to exit...")
        exit()
    # print("Flask server has started")
    # appStart = subprocess.run(["npm start"], shell=True, capture_output=True)
    # if appStart.returncode != 0:
    #     print("Failed to start Electron app.")
    #     input("Press <Enter> to exit...")
    #     exit()
    # else:
    #     pass

startApp()