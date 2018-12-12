# -*- coding: utf-8 -*-
#=================================================
# 	IMPORTS
#=================================================
from str_module import *
from colors import *
import validators
from settings import *


# The function shows the default options for SQLHunt tool
# "-u" Specifies the target url to attack
def SHOW_USAGE( exec_name ):
	SCRIPT_BOLD("How to use SQLHunt:")
	SCRIPT_BOLD(exec_name + " -u \"[TARGET URL]\"\n")
	SCRIPT_BOLD("Options:")
	SCRIPT_BOLD(" -u [URL]:")
	SCRIPT_INFO("Specify the target url for SQL Injection. You can pass an URL with a SQL injection and SQLHunt will test if the injection works (Ex: http://website.com/?a=0+union+select ...) or just pass an URL with GET parameters (Ex: http://website.com/?a=1).")
	SCRIPT_BOLD(" -h or -help:")
	SCRIPT_INFO("Show this help.")
	SCRIPT_BOLD(" --full-help:")
	SCRIPT_INFO("Show the detailed help. This shows how to do attacks with an url containing the SQL injection.")
	SCRIPT_INFO("\nCopyright SQLHunt.")
	SCRIPT_INFO("Developped by Juanpii. http://juan-dev.com/")


# The functions show all the different options that you can
# use, when an url with a payload injection is passed in 
# parameter
# Different Options:
# 	"--limit-tables": 
def SHOW_PAYLOAD_ATTACKS( exec_name ):
	SCRIPT_BOLD("Available attacks [OPTIONS]:\n" )
	SCRIPT_BOLD("--limit-tables:")
	SCRIPT_INFO("An injection with LIMIT clause in order to dump the database tables")
	SCRIPT_INFO("Ex: https://website.com/?a=0 UNION SELECT 1,2 LIMIT 1,1;#")
	SCRIPT_BOLD("\nUse them like this: " + exec_name + " -u \"[TARGET URL]\" [OPTION]")


# Full information of how to use SQLHunt
def SHOW_FULL_USAGE( exec_name ):
	SCRIPT_BOLD("Advanced usage of SQLHunt:")
	SCRIPT_BOLD("SQLHunt supports URLs containing an SQL injection inside.")
	SHOW_SEPARATION_LINE()
	SCRIPT_BOLD("\nUsing SQLHunt without SQL Injection:")
	SCRIPT_INFO("The URL needs to have a GET parameter in order to find an SQL Injection. Example: https://website.com/?a=1")
	SCRIPT_BOLD("\nUsing SQLHunt with SQL Injection:")
	SCRIPT_INFO("SQLHunt can manage URLs that contain already an SQL Injection inside. Example: https://website.com/?a=0 UNION SELECT 1,2,3,4;#")
	SCRIPT_INFO("See full details of this type of attack below.")
	SCRIPT_INFO("\nSpecify the target url using the option '-u'. Like this: " + exec_name + " -u \"https://website.com/?a=1\"")
	SCRIPT_BOLD("\n\nURLs containing already an SQL Injection need to specify an option attack:")
	SHOW_SEPARATION_LINE()
	SHOW_PAYLOAD_ATTACKS( exec_name )

# Shows a line to separe text in the command line
def SHOW_SEPARATION_LINE():
	SCRIPT_INFO("------------------------------------------")

# The function checks if the target URL parameter is good 
# A good url would look like:
# 	- http:// or https://
# 	- A dot '.'
def check_url( url ):
	if url.find("http://") == -1 and url.find("https://") == -1:
		return False
	else:
		if url.find(".") == -1:
			return False
		else:
			return True



# The function checks if the target URL has any payload
# List of payloads:
# UNION
# UNION ALL 
def has_payload( u ):
	# print(u)
	if u.find("union all select") != -1 or u.find("union+all+select") != -1 or u.find("union%20all%20") != -1:
		return True
	elif u.find( "union select" ) != -1 or u.find( "union+select" ) != -1 or u.find( "union%20select" ) != -1:
		return True
	else:
		return False


# Function check if the SQL injection is blind or not
def is_blind( u ):
	# TO DO
	return False