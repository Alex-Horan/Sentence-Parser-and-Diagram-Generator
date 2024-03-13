import subprocess
import os
# THIS FILE IS INCOMPLETE
deps = ["Magick", "pip", "wkhtmltoimage", "node", "git"]

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def spacyInstFix():
    spacyFix = run("py -m pip install -U setuptools wheel")
    if spacyFix.returncode != 0:
        print("Failed to install the dependencies for spaCy.")
        input("Press any key to exit...")
        exit()
    else:
        print("Dependencies for spaCy have been installed.")
        spacyCont = run("py -m pip install -U spacy")
        if spacyCont.returncode != 0:
            print("Failed to install spaCy.")
            input("Press any key to exit...")
            exit()
        else:
            print("SpaCy has finished installing.")
            spacyFin = run("py -m spacy download en_core_web_md")
            if spacyFin.returncode != 0:
                print("Failed to install spaCy model.")
                input("Press any key to exit...")
                exit()
            else:
                print("Finished installing spaCy model")
    installNodeMods()

def Start():

    for r in deps:
        result = run(f"{r} --version")
        if result.returncode != 0:
            print(f"ERROR {result.stderr}: {r} is not installed or is not accessible.")
            input("Press any key to exit...")
            exit()
        else:
            print(f"{r}: Installed")
    installProj()


def installProj():
    sourceDwn = run("git clone https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator.git")    
    if sourceDwn.returncode != 0:
        print("Failed to download project files.")
        input("Press any key to exit...")
        exit()
    else:
        depDown = run("py -m pip install -r ./requirements.txt")
        if depDown.returncode != 0:
            print("Failed to install python dependencies")
            input("Press any key to exit...")
            exit()
        else:
            
            print("Finished installing python dependencies")
    spacyInstFix()
            

def installNodeMods():
    instN = run("npm install --prefix ./Sentence-Parser-and-Diagram-Generator/")
    if instN.returncode != 0:
        print("Failed to install node dependencies.")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished installing Node packages")



Start()
    # run("wget https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/blob/master/requirements.txt")