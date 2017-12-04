import sys
#The end='' in the print statements makes it so the code does not skip lines inbetween each command. It makes the code read in one line as a sentence rather than each command occupying its own line of text. So after the "hello," commanded in line 3, terminal goes right into running line 5, then line 7.
print('Hello, ', end='')

print(sys.argv[1], end='')

print('! Welcome.')
#To run this code/program, I entered in terminal the command: "python3 /users/matthewleone/desktop/python/hello.py 'Matthew, Michael, and Nick' "