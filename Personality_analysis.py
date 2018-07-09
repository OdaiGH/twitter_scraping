from twitter_scraping.database import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

def main():
	if(database_exists("sqlite:///{}.db".format(databasePATH))):
		if not engine.dialect.has_table(engine,"Personality"):
			Personality.__table__.create(engine)
			print("Personality table has been created")
		else:
			pass
	else:
		Base.metadata.create_all()
		print("database has been created!")

if __name__ == '__main__':
	main()