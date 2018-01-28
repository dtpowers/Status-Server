import boto3
import datetime
import io
import json
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
	s3 = boto3.resource('s3')
	DATABASE = loadDB()
	print("Server initialized...")
	prevStatus = len(DATABASE)
	print('Previous Status #: ' + str(prevStatus))


def recStatus(status):
	prevStatus += 1
	DATABASE = status


def getLastStatus():
	return status = DATABASE[str(prevStatus)]
	

def getStatus(id):
	return DATABASE[id]

##########################DB OPERATIONS#################################


#read database from disk into memory
def loadDB():
	print('Loading Database...')
	response = s3.Bucket('pistatus').get_object(Bucket='pistatus', Key='data.json')
	database = json.loads(response['Body'].read())
	pprint(database)
	DATABASE = database
	print('Finished Loading ')


#write db from memory to disk
def saveDB():
	data = io.BytesIO()

	s3.Bucket('pistatus').put_object(Key=(data.json), Body=data)
	with open('data.json', 'w') as outfile:
    	json.dump(DATABASE, outfile)
    print('Wrote DB to disk...')



############################################## tests
serverInit()
loadDB()