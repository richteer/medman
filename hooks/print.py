# Sample hook file, prints the current file being edited

hooks = {
	"postwritefile":[(1,lambda x,y: print(y))]
}
