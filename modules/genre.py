# Example of a module purely meant for tagging

def handle_name(med, name, genres):
	data = med.read_name(name)
	if genres == []:
		if "genres" in data.keys():
			print("{}: ".format(name))
			for g in data["genres"]:
				print(g)
		else:
			print("Genres not defined for '{}'".format(name))
		return True

	if "genres" not in data.keys():
		data["genres"] = []

	add = [g[1:] for g in genres if g.startswith("+")]
	delete = [g[1:] for g in genres if g.startswith("-")]

	data["genres"] = [g for g in data["genres"] + add if g not in delete]

	med.write_name(name, data)
	return True


# Same thing as name, just operate on entries instead
def handle_entry(med, name, entry, genres):
	pass


def medman_genre(med, args):
	if len(args) == 0:
		print("ARGSSSS")
		return False

	if args[0] == "help":
		print('''Usage: medman genre <command> [args...]

Commands:
	help  : Display this help text

	name  : Edit and display the genres for a name
		medman name <name> [[+|-]genres...]

	entry : Edit and display the genres for an entry
		medman entry <name> <entry> [[+|-] genres...]

Genres can be specified with a prefix + or - to add or remove them respectively.
If neither is specified, the genre is ignored
''')
		return True
	elif args[0] == "name":
		return handle_name(med, args[1], args[2:])
	elif args[0] == "entry":
		return handle_entry(med, args[1], args[2], args[3:])
