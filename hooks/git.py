import os

def git_commit(med, filename):
	if "git" not in med.config.keys() or med.config["git"] != "enabled":
		return

	cwd = os.getcwd()
	os.chdir(med.config["path"])
	os.system('git commit "{}"'.format(filename))
	os.chdir(cwd)
	
def git_index_commit(med):
	git_commit(med, "index.json")


hooks = {
	"postwritefile": [(99,git_commit)],
	"postindexadd": [(99,git_index_commit)],
	"postindexremove": [(99,git_index_commit)]
}
