#!/usr/bin/python

devices_to_monitor = [
	{"board_config":"<BOARD_ID like D221AP>","ecid":"<DEVICE HEX ECID>"},
	{"board_config":"another id","ecid":"another ecid"},
]

program_path = "<PATH TO THE PROGRAM FOLDER>/AutoTSS/"
blob_storage_path = program_path + "Blobs/"

import urllib2, json
from os import listdir, makedirs
from os.path import isfile, join, exists
from subprocess import call

"""
Determine if we need to save a blob into a given folder (ie is the build already stored in here?)
"""
def needsToSaveBlob(build_id,device_path):
	device_blobs = listdir(device_path)

	for blob in device_blobs:
		if build_id in blob:
			return False
	return True


#We need to modify our UA or else CF will filter us
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]




for device in devices_to_monitor:
	board = device["board_config"]
	ecid = device["ecid"]
	firmware_URL = "https://ipsw.me/api/ios/v3/device/" + board
	
	response = opener.open(firmware_URL)
	json_response = json.loads(response.read())
	
	device_model = json_response.keys()[0]
	firmwares = json_response[device_model]["firmwares"]
	for firmware in firmwares:
		build_id = firmware["buildid"]
		version = firmware["version"]
		is_signed = firmware["signed"]
		
		if is_signed:
			print("[" + str(device_model) + "] Found firmware " + str(version) + " (" + str(build_id) + "): is signed " + str(is_signed))
			if not exists(blob_storage_path + ecid):
				makedirs(blob_storage_path + ecid)
				print("\t~> device folder not found, creating")
			if needsToSaveBlob(build_id, blob_storage_path + ecid):
				print("\t~> Trying to download")
				call([program_path + "tsschecker","--boardconfig",board,"-e",ecid,"-s","--save-path",blob_storage_path + ecid,"--buildid",build_id])
				
