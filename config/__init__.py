import json
import os
import io
import codecs

#Config class
class Config:
	key_values = dict()
	#if the dictionary is empty, the config is created from the json file
	def __init__(self,key_values={},config_file_address="", config_file_name = "config.json"):
		if(not key_values):
			if os.path.isdir(config_file_address) and os.access(os.path.join(config_file_address,config_file_address), os.R_OK):
				with codecs.open(os.path.join(config_file_address,config_file_name), 'r') as input_file:
					self.key_values = dict(json.load(input_file))
				# checks if file exists
			else:
				print ("Could not read json file from address: "+config_file_address)
				print ("Trying to create config file in: "+config_file_address)
				try:
					with io.open(os.path.join(config_file_address, config_file_name), 'w') as db_file:
						db_file.write(json.dumps(self.key_values))
				except Exception as e:
					print("Config file couldn't be created due to exception:"+ str(e))
		else:
			self.key_values= key_values
	def getKeyValues(self):
		return self.key_values;
	def getValue(self,key,val_type=bool):
			try:
				return val_type(self.key_values[key])
			except:
				try:
					if(val_type==bool):
						return False
					elif(val_type==int):
						return 0
					elif(val_type==float):
						return 0
					else:
						return val_type("")
				except:
					return None





