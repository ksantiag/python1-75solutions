#problem15

cents = input("Enter an integer: ")
type(cents)

print "To make "+str(cents)+" cents, you need:"
print ""



quarters = cents / 25
ncents = cents % 25
nickle = ncents / 5
penny = ncents % 5

print str(quarters)+" quarters"
print str(nickle)+" nickles"
print str(penny)+" pennnies"