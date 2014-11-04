

def medman_define(med, args):
	# TODO: Error message
	if len(args) == 0:
		print("Need args, yo")
		return False

	if args[0] == "category":
		med.create_categories(args[1])
	elif args[0] == "name":
		if len(args) == 2:
			med.create_name(args[1]) 
		else:
			med.create_name(args[1], categories=args[2]) 
	elif args[0] == "help":
		print('''Usage: medman define < name | category | help > <args...>
Commands:
	name <Name> [Category]       : Define an empty name in category provided, puts in root if category not defined
	category <Path/to/Category>  : Define a new category path, and any subcategories if needed
	help                         : Show this text
''')
	else:
		print("Unknown subcommand '{}'".format(args[0]))
		return False

	return True
