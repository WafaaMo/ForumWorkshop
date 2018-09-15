# allowed papers: 100, 50, 10, 5, and rest of request
allowed = [200, 100, 50, 20, 10, 5, 1]
money = 500

request = 840

for cent in allowed:

    while request >= cent:
        print ('give ' + str(cent))
        request -= cent

if request == 0:
    print ('')

elif request < 0:
    print ('Enter a valid amount!! ')

else:
    print ('give ' + str(request))
