
# Print the numbers described in the exercise
for n in range(1,11):
    #for number in range(1,n+1):
    #    print(number, end=' ')
    #print()
    print(*range(1,n+1)) #Dette gøres i stedet for de udskraverede, og sørgger for ikke at have mellemrum tilsidst i linjen. 