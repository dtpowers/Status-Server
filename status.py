from flask import Flask
app = Flask(__name__)


# Status Format
```
{
	statuses: 
		{
		statusID: 1
		status : {
			time: str
			weight: str
			comment: str
			}
	    },
		{
		statusID: 2
		status : {
			time: str
			weight: str
			comment: str
			}
	    }
}
```

########### ROUTES
@app.route("/")
def hello_world():
  return "Hello, World!"




##################SERVER LOGIC

def serverInit():
	global DATABASE
	global prevStatus
	DATABASE = loadDB()
	print("Server initialized...")
	prevStatus = len(DATABASE)
	print('Previous Status #: ' + str(prevStatus))

def recStatus(status):
	prevStatus += 1
	DATABASE['statuses'][] = status


def getLastStatus():
	return status = DATABASE[str(prevStatus)]
	

def getStatus(id):
	return DATABASE[where id = statusID]

##########################DB OPERATIONS#################################


#read database from disk into memory
def loadDB():
	print('Loading Database...')
	database = json.loads(open('data.json'))
	pprint(database)
	DATABASE = database
	print('Finished Loading ')


#write db from memory to disk
def saveDB():
	with open('data.json', 'w') as outfile:
    	json.dump(DATABASE, outfile)
    print('Wrote DB to disk...')
