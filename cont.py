import os
i = 0
turn = "false"
while i <= 11:
	os.system("python crawl.py %s %s" %(i, turn))
	i+=1
	if i == 10:
		turn = "true"