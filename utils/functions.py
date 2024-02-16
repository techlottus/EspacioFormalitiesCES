from database.mongo import database
import datetime
import json
import re
import jwt

class functions:

    def createList(self, responsePLCampus):
        #lista a convertir
        listCampus = []
        Campus = responsePLCampus.json()
        indice = 1
        for campus in Campus:
            objTMP = {
                "label": campus['Value'],
                "Value": indice,
            }
            listCampus.append(objTMP)
            indice = indice + 1
            objTMP = {}
        indice = 0
        return listCampus

    def verificatedDateOfcollection(self,date, documentCampus):

        #pattern = "r" + str(date).split(" ")[0]
        pattern = str(date).split(" ")[0]
        #print(pattern)#fecha actual
        sequence = str(documentCampus["date"]).split(" ")[0]
        #print(sequence)#fecha almacenadada

        if re.match(pattern, sequence):
        #if re.match("2021-12-12", "2021-12-10"): #example fechas
            return  True
        else:
            return False

    def verificatedCollectionCampus(self, mongo):

        documentCampus = mongo.db.Campus.find()
        print(documentCampus)

    def write_token(self ,payload, clave):
        encoded_jwt = jwt.encode(payload, clave, algorithm="HS256")
        #print(encoded_jwt)
        return encoded_jwt

    def validate_token(self,encoded_jwt, clave):
        try:
            payload = jwt.decode(encoded_jwt, clave, algorithms=['HS256'])
            return payload
        except jwt.exceptions.DecodeError:
            return "Token no valido"