# TODO: Figure out how to do this

hooks = {
	"helpshort":"\thelp: Get the help text and usage for a particular module.",
}


def print_help():
	print('''Usage: medman <command> [command args] ...

Registered commands:''')


def medman_help(med, args):
	if len(args) == 0:
		print_help()
		if "helpshort" in config["hooks"].keys():
			for h in config["hooks"]["helpshort"]:
				print(h)
		return 

	
