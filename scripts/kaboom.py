import time
start_time = time.time()

a = 1000000
b = 0
r = a - b
while r > b:
    print (r)
    r = r - 1
else:
    print ("kaboom!!")

print("---Your CPU executed this code in  %s seconds ---" % (time.time() - start_time))
time = (time.time() - start_time)
if time > 10.00:
    print ("your server is crap!!")
else:
    print ("your server is wicked man")
