from sqlalchemy import Column, Integer, String , create_engine, Float, JSON,ForeignKey,TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import sys
from sqlalchemy_utils import database_exists
#sys.path.append('/opt/lucidya/config')
#import config as Config
#to maps classess into tables
Base = declarative_base()


class Users(Base):
	__tablename__   = "Users"
	userid     		= Column(Integer,primary_key=True)
	username 		= Column(String,nullable = False,primary_key=True)

	def __init__(self,userid,username):
		self.userid 	 = userid
		self.username    = username


class Tweets(Base):
	__tablename__   = "Tweets"
	id 				= Column(Integer,primary_key=True,autoincrement=True)
	tweet_json  	= Column(TEXT,nullable=False)
	userid 			= Column(Integer,ForeignKey(Users.userid),nullable = False)


	def __init__(self,tweet_json,userid):
		self.tweet_json = tweet_json
		self.userid    = userid


class Personality(Base):
	__tablename__   = "Personality"

	userid = Column(Integer,ForeignKey(Users.userid),nullable = False,primary_key=True)
	score  = Column(Float,nullable=False,primary_key=True)

	def __init__(self,userid,score):
		self.userid = userid
		self.score  = score

	def __str__(self):
		print("<username {} has scored {} ".format(self.userid.username,self.score))	

#selecting engine, sqlite in this project
databasePATH = 'db'
engine = create_engine('sqlite:///{}.db'.format(databasePATH))

#bind it
Base.metadata.bind = engine
