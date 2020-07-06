#!/usr/bin/env python
import json, sys
import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error, http.client

def main():
	args=sys.argv[1:]
	filename=args[0]
	lfns=[]
	f=open(filename,'r')
	for lfn in f:
		#This line is to remove the carrige return	
		lfn = lfn.rstrip('\n')
		lfns.append(lfn)
	for file in lfns:
		url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/data?file='+file
		result = json.read(urllib.request.urlopen(url).read())
		dataset=result['phedex']['dbs']
		if len(dataset)>0:#in phedex
			print(file)
	sys.exit(0);

if __name__ == "__main__":
	main()	
