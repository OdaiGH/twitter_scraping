from selenium import webdriver
from twitter_scraping.database import *
from twitter_scraping.scrape import *
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker
def get_all_username():
    values = []
    wb = open_workbook('excel_file/Twitter_Arabic_Celebrities.xlsx')
    for s in wb.sheets():
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value  = (s.cell(row,col).value)
                try : value = str(int(value))
                except : pass
                col_value.append(value)
            values.append(col_value)
    return values

if __name__ == "__main__":
	if(database_exists("sqlite:///{}.db".format(databasePATH))):
		DBSession = sessionmaker(bind=engine)
		session = DBSession()
		usernames = get_all_username()
		usernames.pop(0)
		driver = webdriver.PhantomJS(executable_path="twitter_scraping/phantomjs/bin/phantomjs")
		for user in usernames:
			result = start_phantom(user,driver)
			for i in result:
				userid  	= int(i['user']['id'])
				username 	= i['user']['screen_name']
				check_user 	= session.query(Users).filter_by(userid=userid).scalar() is None
				if check_user:
					add_user = Users(userid,username)
					session.add(add_user)
					print("{} has been added".format(username))
				try:
					add_tweet = Tweets(str(i),userid)
					session.add(add_tweet)
					print("tweet has been added.")
				except Exception as e:
					print(e)
					session.rollback()
				session.commit()	
	else:
		Base.metadata.create_all()
		print("database has been created!")