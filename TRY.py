rfile=open("/home/zijie/Stance/Data/Semval2016/try.txt",'r')

for line in rfile:
    line=line.rstrip("\r\n")
    parts=line.split("\t")
    length=len(parts[2])
    print 123



