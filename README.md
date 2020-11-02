# login_tool

Requriements:
	Python 3, pip
	
Install:

	git clone "https://github.com/powerbuilder1/login_tool.git"
	cd login_tool
	chmod +x lgn
	touch .env
	pip3 install -r requirements.txt
  	ADD /PATH/TO/login_tool/ to your $PATH
  	Then open the .env file and store the required information for the services you want to use. Use the provided format at the bottom of this README.

Usage:

  	To run the script type in 'lgn <name of the service you want to login>'

Env File Format:

	Optional:
	
  		AMAZON_EMAIL="<YOUR_AMAZON_LOGIN_EMAIL>"
  		NETFLIX_EMAIL="<YOUR_NETFLIX_LOGIN_EMAIL>"
  		NETFLIX_ACCOUNT_NAME="<YOUR_NETFLIX_ACCOUNT_NAME>"
  		OPAL_USERNAME="<OPAL_USERNAME>"
  		UNIVERSITY_NAME="<UNIVERSITY_NAME>"
		
  	Required:
	
  		FILE_PATH=<PATH/TO/THIS/PROJECT/FOLDER/>
  		DRIVER_TYPE=<"DRIVER_TYPE"> (f.e. firefox, chrome)

Example(Env File Format):
	
	OPAL_USERNAME="opaluser123"
	UNIVERSITY_NAME="TU Dresden"
	FILE_PATH=~/bin/login_tool/
	DRIVER_TYPE="firefox"

Supported Services:
	
	Amazon, Netflix, Opal

Supported Systems:

	Linux

Example(execute skript):
	
	lgn opal
	lgn netflix
	lgn amazon
