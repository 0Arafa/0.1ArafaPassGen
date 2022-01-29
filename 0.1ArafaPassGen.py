#!/usr/bin/python3

from string import ascii_lowercase,ascii_uppercase
from random import shuffle,choices
from os import system


system("clear"),print("""#####    Simple and Powerful Password Generator    #####
	       ##    By: Abd Almoen Arafa    ##
	       ##    Age: 15    	     ##\n""")
def content():
	l_l,l_u,nums,syms=ascii_lowercase,ascii_uppercase,"0123456789","!@#$%^&*()_+-=[]{};:'|\/,.<>?"
	list=[l_l,l_u,nums,syms]
	shuffle(list)
	all=list[0]+list[1]+list[2]+list[3]
	try:
		ask=int(input("How many elements: "))
		print("\n","\t"*3,"#"*31,"\n")
		ran=choices(all,k=ask)
		List="".join(ran)
		print(List),print("\n","\t"*3,"#"*31,"\n")
	except ValueError:	print("Sorry,You have to write just a numbers here\n"),content()
	except KeyboardInterrupt:	print("\nBye ;)\n")
content()
#By Abd Almoen Arafa
#I'm 15 years old
