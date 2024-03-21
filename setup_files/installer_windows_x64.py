import subprocess
from os import remove
import os
from sys import argv

deps = ["magick", "pip", "wkhtmltopdf", "node", "git", "gcc"]

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def start():
    for r in deps:
        #checks for the non-python dependencies
        result = run(f"'{r} --version'")
        if result.returncode != 0:
            print(f"ERROR {result.stderr}: {r} is not installed or is not accessible.")
            input("Press any key to exit...")
            remove(argv[0])
            exit()
        else:
            print(f"{r}: Installed")
    linCMD() #starts the installation
    
def linCMD():
    #creates a directory for the project
    instStart = run("'New-Item -ItemType Directory -Name 'Sentence-Parser''")
    # instStart = run(["mkdir ./Sentence-Parser"])
    if instStart.returncode != 0:
        print("Unable to create directory, please check file permissions")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        print("Finished creating directory for the app!")
        # python3 -m pip install -U setuptools wheel; python3 -m pip install -U spacy; python3 -m spacy download en_core_web_md;
        # source App/bin/activate
        # cd ./Sentence-Parser; source ./App/bin/activate

        #creates a venv for the python deps, added both to make testing and debugging easier and to make it more convenient for others using the app
        makeEnv = run(["Set-Location -Path '.\\Sentence-Parser'; py -m venv App"])
        # makeEnv = run(["cd ./Sentence-Parser; python3 -m venv App;"])
        if makeEnv.returncode != 0:
            print("Failed to create virtual python environment.")
            input("Press any key to exit...")
            remove(argv[0])
            exit()
        else:
            print("Finished creating a virtual environment!")
            spacyCMD()

def spacyCMD():
    print("[*] Don't worry if it seems like it's frozen here, spacy takes anywhere from 10 seconds to 20 years to install depending on its mood apparently")
    # spacy is a bit weird when installing so i added this as a safeguard in case spacy just kinda dies when attempting to install normally
    instSpacy = run(["cd .\\Sentence-Parser; .\\App\\bin\\pip install setuptools wheel spacy;"])
    if instSpacy.returncode != 0:
        print("Failed to install spacy in the virtual environment")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        print("Finished installing Spacy, now installing spaCy model.")
        instModel = run(["cd .\\Sentence-Parser; .\\App\\bin\\python -m spacy download en_core_web_md;"])
        if instModel.returncode != 0:
            print("Failed to install spaCy model.")
            input("Press <Enter> to exit...")
            remove(argv[0])
            exit()
        else:
            print("Finished preventing spaCy jank!")
            projCMD()

def projCMD():
    # clones the github repo
    instProj = run(["cd .\\Sentence-Parser; git clone https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator.git; rm -recursive -force -Path '.\\Sentence-Parser-and-Diagram-Generator\\Windows_Setup_x64.c'; rm -recursive -force -Path '.\\Sentence-Parser-and-Diagram-Generator\\setup_files'; rm -recursive -force -Path '.\\Sentence-Parser-and-Diagram-Generator\\Linux_Setup_x64.c'"])
    # code = instProj.communicate()
    if instProj.returncode != 0:
        print("Failed to clone project")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        print("Finished cloning files!")
        pyCMD()

def pyCMD():
    # installs all of the python deps into the virtenv
    instPy = run(["cd .\\Sentence-Parser; .\\App\\bin\\pip install -r .\\Sentence-Parser-and-Diagram-Generator\\requirements.txt;"])
    if instPy.returncode != 0:
        print("Failed to install python dependencies.")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        print("Finished installing python dependencies!")
        nodeCMD()

def nodeCMD():
    # installs the dependencies for the actual react/electron project
    instNode = run(["cd .\\Sentence-Parser; npm install --prefix .\\Sentence-Parser-and-Diagram-Generator\\"])
    if instNode.returncode != 0:
        print("Failed to install npm packages")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        print("Finished installing npm packages!")
        finInst()

def finInst():
    # compiles the "app" to an executable. This is linux unique because the chances of someone having gcc installed on a linux distro is far higher than for someone on windows
    # windows will use a precompiled binary that is just obfuscated, aka in a different folder, until setup has run and finished
    makeApp = run(["cd .\\Sentence-Parser\\Sentence-Parser-and-Diagram-Generator; gcc .\\ApplicationWindows.c -o ParserApp"])
    if makeApp.returncode != 0:
        print("Failed to install app.")
        input("Press any key to exit...")
        remove(argv[0])
        exit()
    else:
        cleanUp = run(["cd .\\Sentence-Parser-and-Diagram-Generator; rm -force -Path '.\\Sentence-Parser-and-Diagram-Generator\\ApplicationWindows.c'"])
        if cleanUp.returncode != 0:
            print("current path: " + os.getcwd())
            print("Failed to cleanup setup files.")
            input("Press <Enter> to exit...")
            remove(argv[0])
            exit()
        else:
            print("current path: " + os.getcwd())
            print("Finished installing the application!")
            input("Press any key to exit...")
            remove(argv[0])
            exit()
        # very goofy line of code, it makes this file delete itself
        # the reason for deleting this file after completion is because after cloning the repo in an earlier step, there will be 2 copies of the setup script

start()