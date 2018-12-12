# -*- coding: utf-8 -*-
#=================================================
# 	IMPORTS
#=================================================
from str_module import *
from colors import *
import validators
from settings import *


# The function shows the default options for SQLHuntt tool
# "-u" Specifies the target url to attack
def SHOW_USAGE( exec_name ):
	SCRIPT_BOLD("How to use " + V_NAME + ":")
	SCRIPT_BOLD(exec_name + " " + C_URL + " \"[TARGET URL]\"\n")
	SCRIPT_BOLD("Options:")
	SCRIPT_BOLD(" " + C_URL + " \"[URL]\":")
	SCRIPT_INFO("Specify the target url for SQL Injection. You can pass an URL with a SQL injection and " + V_NAME + " will test if the injection works (Ex: http://website.com/?a=0+union+select ...) or just pass an URL with GET parameters (Ex: http://website.com/?a=1).")
	SCRIPT_BOLD(" " + C_HELP + " or " + C_HELP_2 + ":")
	SCRIPT_INFO("Show this help.")
	SCRIPT_BOLD(" " + C_FULL_HELP + ":")
	SCRIPT_INFO("Show the detailed help. This shows how to do attacks with an url containing the SQL injection.")
	SCRIPT_INFO("\nCopyright " + V_NAME + ".")
	SCRIPT_INFO("Developped by " + V_NAME_DEV + ". " + V_WEBSITE)


# The function show all the different options that you can
# use, when an url with a payload injection is passed in 
# parameter
# Different Options:
# 	"--limit-tables": 
def SHOW_PAYLOAD_ATTACKS( exec_name ):
	SCRIPT_BOLD("Available attacks [OPTIONS]:" )
	SCRIPT_BOLD("\n " + C_UNION + "(Coming soon):")
	SCRIPT_INFO("An injection with an UNION clause. Starts a FULL guided attack")
	SCRIPT_INFO("If you're use this attack, make sure your select statement has indentifiable parameters")
	SCRIPT_INFO("Ex: " + E_URL_WITH_SQLI)
	SCRIPT_BOLD("\n " + C_UNION_LIMIT + ":")
	SCRIPT_INFO("An injection with a UNION and a LIMIT clause. Starts a full guided attack")
	SCRIPT_INFO("Ex: " + E_URL_WITH_SQLI_LIMIT)
	SCRIPT_BOLD("\nUse them like this: " + exec_name + " " + C_URL + " \"[TARGET URL]\" [OPTION]")


# The function shows in the command line the full information of how to use SQLHuntt
def SHOW_FULL_USAGE( exec_name ):
	SCRIPT_BOLD("Advanced usage of " + V_NAME + ":")
	SCRIPT_BOLD(V_NAME + " supports URLs containing an SQL injection inside.")
	SHOW_SEPARATION_LINE()
	SCRIPT_BOLD("\nUsing " + V_NAME + " without SQL Injection:")
	SCRIPT_INFO("The URL needs to have a GET parameter in order to find an SQL Injection.")
	SCRIPT_INFO(" Example: " + E_URL_GET)
	SCRIPT_BOLD("\nUsing " + V_NAME + " with SQL Injection:")
	SCRIPT_INFO(V_NAME + " can manage URLs that contain already an SQL Injection inside.")
	SCRIPT_INFO("See full details of this type of attack below.")
	SCRIPT_INFO(" Example: " + E_URL_WITH_SQLI)
	SCRIPT_INFO("\nSpecify the target url using the option '" + C_URL +"'. Like this: " + exec_name + " " + C_URL + " \"" + E_URL_GET + "\"")
	SCRIPT_BOLD("\n\n1. URLs containing already an SQL Injection need to specify an option attack:")
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