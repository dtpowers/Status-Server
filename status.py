import boto3
import datetime
import io
import json
from time import sleep
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
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    DATABASE = loadDB()
    print("Server initialized...")
    prevStatus = len(DATABASE)
    print('Previous Status #: ' + str(prevStatus))

def shutdownServer():
    saveDB()


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
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='pistatus', Key='data.json')
    database = json.loads(response['Body'].read().decode("UTF-8"))
    pp.pprint(database)
    DATABASE = database
    print('Finished Loading ')
    return database


#write db from memory to disk
def saveDB():
    buf = json.dumps(DATABASE).encode('UTF-8')
    s3 = boto3.resource('s3')
    s3.Bucket('pistatus').put_object(Key='data.json', Body=buf)
    print('Wrote DB to disk...')



############################################## tests
serverInit()
loadDB()
sleep(5)
shutdownServer()
