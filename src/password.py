import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
lowercase = False
uppercase = False
number = False
special = False

for c in password:
    if c.islower():
        lowercase = True
    elif c.isupper():
        uppercase = True
    elif c.isnumeric():
        number = True
    elif c in "$#@":
        special = True
    
length = 6 <= len(password) <= 16

is_valid = lowercase and uppercase and number and special and length
print(is_valid)
