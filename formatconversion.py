import os 
homedir = os.environ['HOME']
presentdir =homedir+ "/Antennas and Wave Propagation"
files=os.listdir(presentdir)

for file in files:
	if file.endswith(".ipynb"):
		with open(presentdir+"/"+file,"rb") as filedata:
			with open(presentdir+"/txtconverted/"+file.split(".")[0]+".txt","w") as newfile:
				newfile.write(filedata.read())

