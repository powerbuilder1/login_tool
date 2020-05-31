# login_tool

Install:

	git clone "https://github.com/powerbuilder1/login_tool.git"
	cd login_tool
	chmod -x lgn
	touch .env
  	ADD /PATH/TO/login_tool/ to PATH
  	Then open the .env file and store the required information for the services you want to use. Use the provided format at the bottom of this README.

Usage:

  	To run the script type in 'lgn <name of the service you want to login>'

Env File Format:

  	AMAZON_EMAIL=YOUR_AMAZON_LOGIN_EMAIL
  	NETFLIX_EMAIL=YOUR_NETFLIX_LOGIN_EMAIL
  	NETFLIX_ACCOUNT_NAME=YOUR_NETFLIX_ACCOUNT_NAME
  	OPAL_USERNAME=OPAL_USERNAME
  	UNIVERSITY_NAME=UNIVERSITY_NAME
  
  	FILE_PATH=PATH/TO/THIS/PROJECT/FOLDER/
  	DRIVER_TYPE=DRIVER_TYPE (f.e. firefox, chrome)

Supported Services:
	
	Amazon, Netflix, Opal
