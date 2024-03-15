import spacy
import os.path
from spacy import displacy
from constituent_treelib import ConstituentTree, Language
import imgkit
from flask import jsonify
import shutil
import os
import sys
import platform

config=""

curOS = os.name
if curOS == "nt":
    config = imgkit.config(wkhtmltoimage="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")
else:
    config = imgkit.config(wkhtmltoimage="/usr/bin/wkhtmltoimage")

nlp = spacy.load("en_core_web_md") # loads spacy pipeline
language = Language.English #sets the language for con tree
spacy_model_size = ConstituentTree.SpacyModelSize.Medium
conlp = ConstituentTree.create_pipeline(language, spacy_model_size) #creates pipeline



def checkImg():
    cDir = os.getcwd() + "/conTree.png"
    dDir = os.getcwd() + "/depTree.png"
    ncDir = os.getcwd() + "/assets/images/conTree.png"
    ndDir = os.getcwd() + "/assets/images/depTree.png"
    if ((os.path.exists(cDir)) and (os.path.exists(dDir))):
        shutil.move(cDir, ncDir)
        shutil.move(dDir, ndDir)
        return "done"
    else:
        return "image move failed"



def depTree(sentence: str): #generates dependency tree
    if sentence is not None:
        doc = nlp(sentence)
        html = displacy.render(doc, style="dep")
        imgkit.from_string(html, 'depTree.png', config=config)
        
        
    
def conTree(sentence: str): #generates constituent tree
    if sentence is not None:
        tree = ConstituentTree(sentence, conlp)
        tree.export_tree(destination_filepath='conTree.png', verbose=True)
        

def graphGen(sentence: str):
    print(os.getcwd())
    depTree(sentence)
    conTree(sentence)
    return checkImg()