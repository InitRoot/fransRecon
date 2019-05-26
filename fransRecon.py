# The script requires dig and need to be placed on same sublist3r folder.
# Enter the domain name as argument.
# Created by InitRoot (Frans Hendrik Botes)
#!/usr/bin/env python

import os
import sys
import subprocess
import json
import pprint
import re
import sys
import time
import pandas as pd
import requests
import argparse
import click
import json
import ssl
import sublist3r 
###############################################################################
#									CONFIGS	                                  								  #
###############################################################################
enumDomain = ""
finalDomains= []
completeDomains = []
###############################################################################
#									INTRO			                                    						  #
###############################################################################
art = """
  ______                         _____                          
 |  ____|                       |  __ \                         
 | |__  _ __  __ _  _ __   ___  | |__) | ___   ___  ___   _ __  
 |  __|| '__|/ _` || '_ \ / __| |  _  / / _ \ / __|/ _ \ | '_ \ 
 | |   | |  | (_| || | | |\__ \ | | \ \|  __/| (__| (_) || | | |
 |_|   |_|   \__,_||_| |_||___/ |_|  \_\\___| \___|\___/ |_| |_|
                                                                
                                                                """
def printArt():
	print art
	

###############################################################################
#									CLEANUP				                                  					  #
###############################################################################
#remove previous results files
def cleanupFiles():
	if os.path.exists("horDoms.txt"):
	  os.remove("horDoms.txt")
	  
	if os.path.exists("finalDoms.txt"):
	  os.remove("finalDoms.txt")
	  
	if os.path.exists("vertDoms.txt"):
	  os.remove("vertDoms.txt")

###############################################################################
#							VERTICAL ENUMERATION	                            						  #
###############################################################################
def verticalEnum():
	for domain in finalDomains:
		print "Performing vertical enumeration for: " + domain + " using Sublist3r."
		subdomains = sublist3r.main(domain, 40, 'vertDoms.txt',ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
		time.sleep(30)
		global completeDomains
		for dom in subdomains:
			completeDomains.append(dom)
		
	
	print "Sublist3r done, port scan will start next."
	print (completeDomains)

###############################################################################
#							HORIZONTAL ENUMERATION	                          						  #
###############################################################################
# Scrapes the viewdns site
def getdatafromViewDNS(searchQuery):
	searchQuery = searchQuery.replace(" ", "+")
	url = "https://viewdns.info/reversewhois/?q=" + searchQuery
	print ("[*] Extracting from: " + url)
	try:
		result = pd.read_html(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text)
		response = result[3][0]
		iter_url = iter(response)
		return iter_url
       # next(iter_url)
        #for url in iter_url:
		#	print(url)			
	except Exception as e:
		print("[!] Couldn't send query, error: {e} exiting...\n")
		exit
	
# Will return the org name for any domain name.
def getOrganization(inputDomain):
	enumDomain=inputDomain
	whoisCMD = 'whois '+enumDomain+'| grep "Registrant Organization" | sed "s:Organization::" | grep -o -m 1 -P "(?<=: ).*"'
	domainOrg=subprocess.Popen(whoisCMD, shell=True, stdout=subprocess.PIPE).stdout
	domainOrg = domainOrg.read()
	return domainOrg
	
# Main function to scrape other domain names based on the org and initial domain name.
# [1] We start by scraping the org for horizontal domains and add to array.
# [2] We scrape the inputDomain for horizontal domains and add to array.
# [3] The array list is then send to Amass for vertical enumeration.

def horizontalEnum():
	#First set of enumeration only using the current domain name
	global finalDomains
	enumDomain=sys.argv[1]
	finalDomains.append(sys.argv[1])
	print "Fetching domain organisation for " + enumDomain + " using WHOIS."
	enumOrg = getOrganization(enumDomain)
	print "- WHOIS lookup done, performing horizontal enumeration for {if found}: " + enumOrg
	#now we need to scrape other domains based on the organisation.
	scrapedData = getdatafromViewDNS(enumOrg)
	next(scrapedData)
	for url in scrapedData:
		finalDomains.append(url)
		
	#now we need to scrape other domains based on the inputDomain.
	time.sleep(20)
	scrapedData = getdatafromViewDNS(enumDomain)
	next(scrapedData)
	for url in scrapedData:
		finalDomains.append(url)
		
	#HorizontalArrayBuilt enumuerating using Amass
	print ("- All horizontal domains have been enumerated.")
	with open('horDoms.txt','w') as f:
		f.write( ','.join(finalDomains))
	

###############################################################################
#							  PORT ENUMERATION							                            	  # 
###############################################################################



	
###############################################################################
#								MAIN PROGRAM		                                						  #
###############################################################################

def main(arguments):
	printArt()
	cleanupFiles()
	horizontalEnum()
	verticalEnum()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		sys.exit(main(sys.argv[1]))
	else:
		printArt()
		print ("Please use domainname with e.g. fransRecon.py domainName")
		exit
