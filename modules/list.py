import os,json

def medman_list(config, commands, args):
	# TODO: Error-check that config has a base registration path
	with open(config["path"].replace("~",os.environ["HOME"]) + "/index.json","r") as f: # TODO: Clean up the stupid $HOME issue
		ls = json.loads(f.read())["media"]

	

	
	for l in ls:
		print(l["name"])
