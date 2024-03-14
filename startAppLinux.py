import subprocess

def startApp():
    result = subprocess.run(["echo $PWD; source ../App/bin/activate; python3 -m flask --app FlaskServer run;"], shell=True, capture_output=True)
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