import os,json

def medman_list(config, commands, args):
	# TODO: Error-check that config has a base registration path


	# Default action: Display all registered names
	if len(args) == 0:
		with open(config["path"].replace("~",os.environ["HOME"]) + "/index.json","r") as f: # TODO: Clean up the stupid $HOME issue
			ls = json.loads(f.read())["media"]

		for l in ls:
			print(l["name"])

		return

	# Otherwise, find the name specified, and display its sublist
	with open(config["path"].replace("~", os.environ["HOME"]) + "/index.json", "r") as f:
		ls = json.loads(f.read())["media"]

	for l in ls:
		if l["name"] == args[0]:
			print(l["path"]) # TODO: Replace with files known to this
			return

	print("Title '{}' not registered!".format(args[0]))
