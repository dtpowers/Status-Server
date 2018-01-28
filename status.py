import boto3
import datetime
import io
import json
import pprint
# from flask import Flask
# app = Flask(__name__)



# ########### ROUTES
# @app.route("/")
# def hello_world():
#   return "Hello, World!"




##################SERVER LOGIC

def serverInit():
    global DATABASE
    global prevStatus
    global s3
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    s3 = boto3.client('s3')
    DATABASE = loadDB()
    print("Server initialized...")
    prevStatus = len(DATABASE)
    print('Previous Status #: ' + str(prevStatus))

def recStatus(status):
    prevStatus += 1
    DATABASE = status


def getLastStatus():
    status = DATABASE[str(prevStatus)]
    return status
    

def getStatus(id):
    return DATABASE[id]

##########################DB OPERATIONS#################################


#read database from disk into memory
def loadDB():
    print('Loading Database...')
    response = s3.get_object(Bucket='pistatus', Key='data.json')
    database = json.loads(response['Body'].read().decode("UTF-8"))
    pp.pprint(database)
    DATABASE = database
    print('Finished Loading ')


#write db from memory to disk
def saveDB():
    s3.Bucket('pistatus').put_object(Key='data.json', Body=DATABASE)
    print('Wrote DB to disk...')



############################################## tests
serverInit()
loadDB()
