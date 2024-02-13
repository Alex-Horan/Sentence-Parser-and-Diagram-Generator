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





def depTree(sentence: str): #generates dependency tree
    if sentence is not None:
        doc = nlp(sentence)
        html = displacy.render(doc, style="dep")
        imgkit.from_string(html, 'depTree.png')
        
        
    
def conTree(sentence: str): #generates constituent tree
    if sentence is not None:
        tree = ConstituentTree(sentence, conlp)
        tree.export_tree(destination_filepath='conTree.png', verbose=True)
        

async def graphGen(sentence: str):
    await depTree(sentence)
    await conTree(sentence)