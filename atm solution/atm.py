# allowed papers: 100, 50, 10, 5, and rest of request
allowed = [200, 100, 50, 20, 10, 5, 1]
money = 500

request = 277
i = 0
while request > 0 and i < len(allowed):
    paper = allowed[i]
    while request >= paper:
        print ('give ' + str(allowed[i]))
        request -= allowed[i]

    i += 1
if request == 0:
    print ('')

elif request < 0:
    print ('Enter a valid amount!! ')

else:
    print ('give ' + str(request))
