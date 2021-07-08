import markdown
import os
from os import walk
import tempfile

# The service for convertion operations
class ConverterService():

    # Constructor
    def __init__(self):
        print("init ConverterService")

    def convert(self):
        return self.browse("/home/vagrant/tmp/clone/")

    # Convert local .md file to .html file 
    def convert2Html(self, folder, fileName, currentFolder, destinationFolder):

        chemin=folder+fileName
        with open(chemin, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
#permet de créer le nom du fichier html à partir du nom d'origine
        fichierHTML=destinationFolder+currentFolder+fileName[:len(fileName)-3]+".html"
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
        #destinationFolder = "/home/shared/converter/tmp"
        destinationFolder= tempfile.TemporaryDirectory(dir = "/home/shared/converter") # support de la concaténation absent pour la partie convert, à changer
        print('###Dossier temporaire : ', destinationFolder)
        # TODO - doit pouvoir servir pour la table des matieres...
        listeFichiers = []
        for (repertoire, sousRepertoires, fichiers) in walk(folder):
            #ignore les dossiers cachés
            if(repertoire.find('.')==0):
                    break
            for f in fichiers:                
                # Si on a un ".md" alors on convertit
                if(f.find(".md") != -1):
                    # Compute current folder where f is 
                    currentFolder = repertoire[len(folder) - 1 : len(repertoire)]
                    print("current folder: " + currentFolder)
                    self.convert2Html(repertoire, f, currentFolder, destinationFolder)
        destinationFolder.cleanup()
            
        return "Done"