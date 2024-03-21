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
import fitz

config=""
conConfig=""

curOS = os.name
if curOS == "nt":
    conConfig="C:\\Program Files\\wkthmltopdf\\bin\\wkhtmltopdf.exe"
    config = imgkit.config(wkhtmltoimage="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")
else:
    conConfig="/usr/bin/wkhtmltopdf"
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
        if curOS == "nt":
            tree.export_tree(destination_filepath="./conTree.png", verbose=True)
        else:
            tree.export_tree(destination_filepath='./conTree.pdf', verbose=True, wkhtmltopdf_bin_filepath=conConfig)
            pdf = fitz.open("conTree.pdf")
            for page in pdf:
                pix = page.get_pixmap(dpi=1300)
                pix.save("conTree.png")

def graphGen(sentence: str):
    print("Current path: " + os.getcwd())
    depTree(sentence)
    conTree(sentence)
    return checkImg()