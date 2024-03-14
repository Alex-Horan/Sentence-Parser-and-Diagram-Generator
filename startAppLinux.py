import subprocess
import os

def startApp():
    venvPath = (os.getcwd()).replace("Sentence-Parser-and-Diagram-Generator", "")
    result = subprocess.run([f"source {venvPath}/App/bin/activate; python3 -m flask --app FlaskServer run;"], shell=True, capture_output=True)
    if result.returncode != 0:
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