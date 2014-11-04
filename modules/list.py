import os,json

hooks = {
	"helpshort":"\tlist: Display a list of names, or a list of files for a name"
}

def medman_list(med, args):
	# TODO: Error-check that config has a base registration path


	# Default action: Display all registered names
	if len(args) == 0:
		for l in med.get_names():
			print(l)

		return True


	# Otherwise, find the name specified, and display its sublist
	s = med.name_to_file(args[0])
	if s:
		print(s)
	else:
		print("Title '{}' not registered!".format(args[0]))
