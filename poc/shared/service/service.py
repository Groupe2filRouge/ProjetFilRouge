import pymongo
from bson.json_util import dumps, loads
import random
import json

class Service():

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        base_de_donnees = myclient["tp-python"]
        self.donnees_machines = base_de_donnees["machines"]
        
    # https://www.w3schools.com/python/python_mongodb_getstarted.asp

    def get_machines(self):
        # Returns a JSON of the machines defined above. jsonify is a Flask function that serializes the object for us.
        lst = list(self.donnees_machines.find({})) # Converts object to list
        return dumps(lst) # Converts to String

    def get_machine(self, hostname):
            
        myquery = { "hostname": hostname }
    
        l = list(self.donnees_machines.find(myquery, {"_hostname": 0})) # Converts object to list

        return dumps(l) # Converts to String
        
    def delete_machine(self, hostname):

        myquery = { "hostname": hostname }

        self.donnees_machines.delete_one(myquery)
        
        return "Deleted"
        
    def update_machine(self, hostname, machine):

        myquery = { "hostname": hostname }
       
        self.donnees_machines.replace_one(myquery, machine)
        return "Updated"    

    def add_machine(self, machine):
        x = self.donnees_machines.insert_one(machine)
        
        return "Added"



