import pymongo
from bson.json_util import dumps, loads
import random
import json

# The service for database's operations
class DatabaseService():
    
    # Constructor
    def __init__(self):
        print("init DatabaseService")
        pymongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        base_de_donnees = pymongoClient["projetFR"]
        self.redacteurs = base_de_donnees["redacteurs"]
        
    def get_redacteur_token(self, git):
            
        myquery = { "git": git }
    
        l = list(self.redacteurs.find(myquery)) # Converts object to list

        return dumps(l[0]["token"]) # Converts to String
        
    def get_redacteur_canal(self, git):
            
        myquery = { "git": git }
    
        l = list(self.redacteurs.find(myquery)) # Converts object to list

        return dumps(l[0]["canal"]) # Converts to String
