import os

def add(med, name, files):
	data = med.read_name(name)
	
	for f in files:
		if f[0] != "/":
			f = os.getcwd() + "/" + f
		data["files"].append(f)

	for f in files:
		if not os.path.exists(f):
			print("Warning: File '{}' does not appear to exist".format(f))

	med.write_name(name, data)

def delete(med, name, files):
	data = med.read_name(name)

	# OPTIMIZE: Oh god this.
	files = [f if f[0] == "/" else os.getcwd() + "/" + f for f in files] # Ensure file is absolute path
	
	data["files"] = [f for f in data["files"] if f not in files]

	med.write_name(name, data)

def medman_file(med, args):
	if len(args) == 0:
		print("wat u say?")
		return False

	if args[0] == "add":
		add(med, args[1], args[2:])
	elif args[0] == "delete":
		delete(med, args[1], args[2:])
	else:
		print("Unknown command '{}'".format(args[0]))
		return False

	return True
