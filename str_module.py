# -*- coding: utf-8 -*-
from colors import *
# -------------------------
# Use with: Python_2
# This library is used to extract data from the injections
# -------------------------

# Checks for a message inside a page
# Return: True if the message appears or False if not
# Params:
# 	page -> The web page, where we check for the message
#	message -> The message to check for 
def check_for( page, message ):
	if page.find( message ) != -1:
		return True
	else:
		return False


# Checks for a specific string inside the page
# Return: The result wanted
# Params:
# 	string -> The string where we search for the result
# 	start_delimiter -> Where to begin the search
#	end_delimiter -> Where to end the search
def check_result( string, start_delimiter, end_delimiter ):
	result_cut = string[ string.find( start_delimiter ) + len( start_delimiter ) : ]
	result_cut = result_cut[ 0 : result_cut.find( end_delimiter ) ]
	return result_cut



#======================================================
# SCRIPT MESSAGE, WARNING AND ERRORS
#======================================================
# Prints a message on the command line
# Script prettier tho
def SCRIPT_INFO( message ):
	print( message )

# Prints a red ERROR color message
def SCRIPT_ERROR( message ):
	print( bcolors.BOLD + bcolors.FAIL + "Error: " + message + bcolors.END )

# Prints a red color message
def SCRIPT_ERROR_SIMPLE( message ):
	print( bcolors.BOLD + bcolors.FAIL + message + bcolors.END ) 

# Prints a yellow color message
def SCRIPT_WARNING( message ):
	print( bcolors.WARNING + message + bcolors.END )
# Prints a green color message
def SCRIPT_GOOD( message ):
	print( bcolors.GOOD + message + bcolors.END )
# Prints a bold message
def SCRIPT_BOLD( message ):
	print( bcolors.BOLD + message + bcolors.END )