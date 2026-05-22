# Initialize dictionary
test_direct = {'Cordignal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

# printing original dictionary
print("The original dictionary : " + str(test_direct))

# Initialize value
K = 2

# Using loop
# Selective key values in dictionary
res = 0
for key in test_direct:
    if test_direct[key] == K:
        res = res + 1

# printing result
print("Frequency of K is : " + str(res))