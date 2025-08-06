from PyLayoutTools import pltTable

tbl = pltTable("Yaoi", ["Name", "Position", "Age"], 
			["Alex Calveley", "Singer/Guitarist", "48"], 
			["Markus Calveley", "Cybersecurity Analyst", "43"], 
			["Dynamo Calveley", "Secondary Student", "15"],
			["Bash \"Rackodo\"", "Tertiary Student", "20"],
			["Theodore Donovan", "Maintenance Company Owner", "35"]
			)

print(tbl())