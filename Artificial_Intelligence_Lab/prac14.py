print("welcome to careerpath  decision maker")
print("select subject \nmath.\nphy.\nchemistry.\nprogramming.\ncircuits.\nbiology")
sub1=input("enter your first choice :")
sub2=input("enter your second subject:")
if((sub1=="math" and sub2=="phy")  or (sub1=="phy" and sub2=="math")):
		print("suggestion is" "mechanical engineering")
elif((sub1=="math" and sub2=="circuit")  or (sub1=="circuit" and sub2=="math")):
		print("suggestion is" "electronics engineering")
elif((sub1=="chemistry" and sub2=="biology")  or (sub1=="biology" and sub2=="chemistry")):
		print("suggestion is" "biotechnology engineering")
elif((sub1=="math" and sub2=="programming")  or (sub1=="programming" and sub2=="math")):
		print("suggestion is" "computer engineering")
elif((sub1=="programming" and sub2=="circuits")  or (sub1=="circuit" and sub2=="programming")):
		print("suggestion is" "ENTC engineering")									
else:
                  print("no branch related to this")
