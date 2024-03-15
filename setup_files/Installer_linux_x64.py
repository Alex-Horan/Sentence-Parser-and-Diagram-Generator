import subprocess
from os import remove
from sys import argv

deps = ["magick", "pip", "wkhtmltoimage", "node", "git", "gcc"]

def run(cmd):
    completed = subprocess.run(cmd, shell=True, capture_output=True)
    return completed

def start():
    for r in deps:
        #checks for the non-python dependencies
        result = run([f"{r} --version"])
        if result.returncode != 0:
            print(f"ERROR {result.stderr}: {r} is not installed or is not accessible.")
            input("Press any key to exit...")
            exit()
        else:
            print(f"{r}: Installed")
    linCMD() #starts the installation
    
def linCMD():
    #creates a directory for the project
    instStart = run(["mkdir ./Sentence-Parser"])
    if instStart.returncode != 0:
        print("Unable to create directory, please check file permissions")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished creating directory for the app!")
        # python3 -m pip install -U setuptools wheel; python3 -m pip install -U spacy; python3 -m spacy download en_core_web_md;
        # source App/bin/activate
        # cd ./Sentence-Parser; source ./App/bin/activate

        #creates a venv for the python deps, added both to make testing and debugging easier and to make it more convenient for others using the app
        makeEnv = run(["cd ./Sentence-Parser; python3 -m venv App;"])
        if makeEnv.returncode != 0:
            print("Failed to create virtual python environment.")
            input("Press any key to exit...")
            exit()
        else:
            print("Finished creating a virtual environment!")
            spacyCMD()

def spacyCMD():
    print("[*] Don't worry if it seems like it's frozen here, spacy takes anywhere from 10 seconds to 20 years to install depending on its mood apparently")
    # spacy is a bit weird when installing so i added this as a safeguard in case spacy just kinda dies when attempting to install normally
    instSpacy = run(["cd ./Sentence-Parser; ./App/bin/python3 -m pip install setuptools wheel spacy; ./App/bin/python3 -m spacy download en_core_web_md;"])
    if instSpacy.returncode != 0:
        print("Failed to install spacy in the virtual environment")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished preventing spaCy jank!")
        projCMD()

def projCMD():
    # clones the github repo
    instProj = run(["cd ./Sentence-Parser; git clone https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator.git"])
    # code = instProj.communicate()
    if instProj.returncode != 0:
        print("Failed to clone project")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished cloning files!")
        pyCMD()

def pyCMD():
    # installs all of the python deps into the virtenv
    instPy = subprocess.Popen(["cd ./Sentence-Parser; ./App/bin/python3 -m pip install -r ./Sentence-Parser-and-Diagram-Generator/requirements.txt;"], shell=True, stdout=subprocess.PIPE)
    code = instPy.communicate()
    if code.returncode != 0:
        print("Failed to install python dependencies.")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished installing python dependencies!")
        nodeCMD()

def nodeCMD():
    # installs the dependencies for the actual react/electron project
    instNode = run(["cd ./Sentence-Parser; npm install --prefix ./Sentence-Parser-and-Diagram-Generator/"])
    if instNode.returncode != 0:
        print("Failed to install npm packages")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished installing npm packages!")
        finInst()

def finInst():
    # compiles the "app" to an executable. This is linux unique because the chances of someone having gcc installed on a linux distro is far higher than for someone on windows
    # windows will use a precompiled binary that is just obfuscated, aka in a different folder, until setup has run and finished
    makeApp = run(["cd ./Sentence-Parser/Sentence-Parser-and-Diagram-Generator; gcc ./ApplicationLinux.c -o ParserApp"])
    if makeApp.returncode != 0:
        print("Failed to install app.")
        input("Press any key to exit...")
        exit()
    else:
        print("Finished installing the application!")
        input("Press any key to exit...")
        # very goofy line of code, it makes this file delete itself
        # the reason for deleting this file after completion is because after cloning the repo in an earlier step, there will be 2 copies of the setup script
        remove(argv[0])
        exit()

start()


# this is just obsolete code left in for fun

# def installProj():
#     sourceDwn = run("git clone https://github.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator.git")    
#     if sourceDwn.returncode != 0:
#         print("Failed to download project files.")
#         input("Press any key to exit...")
#         exit()
#     else:
#         depDown = run("py -m pip install -r ./requirements.txt")
#         if depDown.returncode != 0:
#             print("Failed to install python dependencies")
#             input("Press any key to exit...")
#             exit()
#         else:
#             print("Finished installing python dependencies")
#     spacyInstFix()
            
# def installNodeMods():
#     instN = run("npm install --prefix ./Sentence-Parser-and-Diagram-Generator/")
#     if instN.returncode != 0:
#         print("Failed to install node dependencies.")
#         input("Press any key to exit...")
#         exit()
#     else:
#         print("Finished installing Node packages")
# def spacyInstFix():
#     spacyFix = run("py -m pip install -U setuptools wheel")
#     if spacyFix.returncode != 0:
#         print("Failed to install the dependencies for spaCy.")
#         input("Press any key to exit...")
#         exit()
#     else:
#         print("Dependencies for spaCy have been installed.")
#         spacyCont = run("py -m pip install -U spacy")
#         if spacyCont.returncode != 0:
#             print("Failed to install spaCy.")
#             input("Press any key to exit...")
#             exit()
#         else:
#             print("SpaCy has finished installing.")
#             spacyFin = run("py -m spacy download en_core_web_md")
#             if spacyFin.returncode != 0:
#                 print("Failed to install spaCy model.")
#                 input("Press any key to exit...")
#                 exit()
#             else:
#                 print("Finished installing spaCy model")
#     installNodeMods()
