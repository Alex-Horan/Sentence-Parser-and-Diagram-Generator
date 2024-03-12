import subprocess
import os

deps = ["Magick", "pip", "wkhtmltoimage", "node", "git"]

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def installProj():
    sourceDwn = run("git clone https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator.git")    
    

def checkPreReq():
    gcC = run("gcc --version")
    if gcC.returncode != 0:
        print("GCC is not installed, please install msys2 and try again")
        input("Press any key to exit...")
        exit()

    for r in deps:
        result = run(f"{r} --version")
        if result.returncode != 0:
            print(f"ERROR {result.stderr}: {r} is not installed or is not accessible.")
            input("Press any key to Exit...")
            exit()
        else:
            print(f"{r}: Installed")

    print(os.getcwd())
    installProj()


checkPreReq()
    # run("wget https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/blob/master/requirements.txt")