
# this asks the user for a number and turns the answer
# into an integer
n = int(input("How many times should I loop? "))

# Now, print "Hello, World!" n times.
i = 0
while i < n:
    print("Hello World!")
    i += 1


p = input('Do you want to stop? ')
while p != 'yes':
    p = input('Do you want to stop? ')