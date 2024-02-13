import spacy
import os.path
from spacy import displacy
from constituent_treelib import ConstituentTree, Language, Structure
import imgkit
from flask import jsonify
import shutil
import os

language = Language.English #sets the language for con tree
spacy_model_size = ConstituentTree.SpacyModelSize.Small
conlp = ConstituentTree.create_pipeline(language, spacy_model_size) #creates pipeline

nlp = spacy.load("en_core_web_sm")


def treeDeterminer(type, body): #selects either dep or constit tree
    if type == "dep":
       return depTree(body)
    elif type == "con":
       return conTree(body)
    else:
        return "no type specified"

def picExists(type, alt):   #checks if the tree was created properly
    if os.path.exists(f"{type}.png"):
            if os.path.exists(f"{alt}.png"):
                ifExists = jsonify({"Content-Type": "application/json", type: True, alt: True})
                print("both exist")
                print(ifExists)
                return ifExists
            else:
                ifExists = jsonify({"Content-Type": "application/json", type: True, alt: False})
                cwd = os.path.abspath(os.getcwd())
                conPic = os.path.abspath('con.png')
                wd = cwd.replace("Flask_Files", "Flutter_Project\\assets\\images")
                print(wd)
                if os.path.exists(f"{wd}\\con.png"):
                    os.remove(f"{wd}\\con.png")

                shutil.move(conPic, wd)

                
                return ifExists
    else:
        print('pic doesnt exist')

def depTree(sentence: str): #generates dependency tree
    if sentence is not None:
        doc = nlp(sentence)
        html = displacy.render(doc, style="dep")
        imgkit.from_string(html, 'dep.png')
        return picExists("dep", "con")
        
        
    
def conTree(sentence: str): #generates constituent tree
    if sentence is not None:
        tree = ConstituentTree(sentence, conlp)
        tree.export_tree(destination_filepath='con.png', verbose=True)
        return picExists("con", "dep")

