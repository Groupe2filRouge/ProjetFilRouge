import markdown
import os
from os import walk
import tempfile
import shutil
from markdown.extensions.toc import TocExtension

# Concernant la table des matières
#Un document *.md = <ul>, un "#" est un menu, plusieurs "#" qui s'enchainent sont des sous-menus
#La table des matières doit être en haut de la première page (premier doc converti) dans un <div>
#
#

# The service for convertion operations
class ConverterService():

    # Constructor
    def __init__(self):
        print("init ConverterService")

    def convert(self):
        return self.browse("/home/vagrant/tmp/clone")

    # Convert local .md file to .html file 
    def convert2Html(self, folder, fileName, currentFolder, destinationFolder):
        # TODO : la fonction ne gère pas les sous-répertoires quand elle trouve des *.md apparement. Peut-être que rajouter un '/' dans 
        # la concaténation du nom des fichiers devrait suffire...
        chemin=folder+"/"+fileName
        print("le chemin avant conversion :" + chemin)
        with open(chemin, 'r') as f:
            text = f.read()
            html = markdown.markdown(text, extensions=['toc'])
#permet de créer le nom du fichier html à partir du nom d'origine
        fichierHTML=destinationFolder+currentFolder+"/"+fileName[:len(fileName)-3]+".html"
        #permet de créer le chemin de destination en miroir à l'arborescence d'origine
        destination=destinationFolder+currentFolder
        #écrit les fichiers convertis si l'arborescence miroire existe, crée l'arborescence sinon.
        if(os.path.exists(destination)):
            with open(fichierHTML, 'w') as f:
                f.write(html)
        else:
            os.makedirs(destination)
            with open(fichierHTML, 'w') as f:
                f.write(html)

        return "document converted"

    def browse(self, folder):
        #dossier temporaire pour la conversion

        destinationFolder="/home/shared/converter/tmp"        
        # TODO - doit pouvoir servir pour la table des matieres...
        #listeFichiers = []
        for (repertoire, sousRepertoires, fichiers) in walk(folder):
            #ignore les dossiers cachés
            if(repertoire.find('.')==0):
                break
            for f in fichiers:                
                # Si on a un ".md" alors on convertit
                print("Valeur Repertoire : ***"+repertoire)
                if(f.find(".md") != -1):
                    # Compute current folder where f is 
                    currentFolder = repertoire[len(folder) : len(repertoire)]  #retiré le  - 1 après le premier folder
                    print("current folder: " + currentFolder)
                    self.convert2Html(repertoire, f, currentFolder, destinationFolder)
        
            
        return "Done"


def suppr():
    if(not os.path.exists("/home/shared/converter/tmp")):
        os.makedirs("/home/shared/converter/tmp")
    else:
        destinationFolder="/home/shared/converter/tmp"
        print('###Dossier temporaire : ', destinationFolder)
        #suppression du contenu du dossier temporaire
    dossier_tmp=destinationFolder
    try:
        shutil.rmtree(dossier_tmp)
    except OSError as erreur:
        print(f'Error: {dossier_tmp} : {erreur.strerror}')