f = open("issue_pool")
f2 = open("issue_pool.md","w")

intro = f.readline()
f2.write(intro)

f.readline()
f2.write("\n")

intro2 = f.readline()
f2.write(intro2)

f.readline()
f2.write("\n")

i = 1
q = f.readline()
while q != '':
    f2.write("Issue %d\n" % i)
    f2.write("========\n")
    f2.write(q)
    
    f.readline()
    f2.write("\n")


    q = f.readline()
    f2.write(q)

    f.readline()
    f2.write("\n")
    while q != '' and q[0:5] != "Write":
        q = f.readline()
        f2.write(q)

        f.readline()
        f2.write("\n")


    q = f.readline()
    i += 1
