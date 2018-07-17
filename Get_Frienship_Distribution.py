"""
This is for drawing friendship distribution.

Parameters:
      filter_thresholds: a list of filter thresholds
"""

import matplotlib.pyplot as plt
import numpy as np
filter_thresholds=[5,10,15,20]
num_of_users=2713

cnt=0
x = np.zeros((4,2000))
y = np.zeros((4,2000))
for filter_threshold in filter_thresholds:

  ######################################################input root  rname  and wname
  root="/home/zijie/Stance/Data/Semval2016/"
  rname="New_friendship_filtered"+str(filter_threshold)+".txt"
  wname="Friend_Distribution_"+str(filter_threshold)+".txt"

  friend_cont=dict()

  with open(root+rname,'r') as f:
    line_num=0
    for line in f:
        line_num+=1
        if  line_num==1:
          continue
        line=line.rstrip("\r\n")
        parts=line.split("\t")
        friend_list = parts[1].split(":")
        friend_num=len(friend_list)
        if not friend_cont.has_key(friend_num):
            friend_cont[friend_num]=1
        else:
            friend_cont[friend_num]+=1


  index=0
  for (friend_num, count) in friend_cont.items():
    x[cnt][index]=int(friend_num)
    y[cnt][index]=int(count)
    index+=1

  cnt+=1

plt.figure()
plt.subplots_adjust(wspace =0.2, hspace =0.3)
p1=plt.subplot(2,2,1)
p2=plt.subplot(2,2,2)
p3=plt.subplot(2,2,3)
p4=plt.subplot(2,2,4)


p1.stem(x[0],y[0],'r','ro')
p1.set_xlabel("Number of followers")
p1.set_ylabel("Frequency")
p1.set_title("Following Number Distribution with filter_threshold= %d" % filter_thresholds[0])
p1.set_ylim(0,80)
p1.set_xlim(xmin=0,xmax=1000)


p2.stem(x[1],y[1],'r','ro')
p2.set_xlabel("Number of followers")
p2.set_ylabel("Frequency")
p2.set_title("Following Number Distribution with filter_threshold= %d" % filter_thresholds[1])
p2.set_xlim(xmin=0,xmax=1000)
p2.set_ylim(0,80)

p3.stem(x[2],y[2],'r','ro')
p3.set_xlabel("Number of followers")
p3.set_ylabel("Frequency")
p3.set_title("Following Number Distribution with filter_threshold= %d" % filter_thresholds[2])
p3.set_xlim(xmin=0,xmax=1000)
p3.set_ylim(0,80)

p4.stem(x[3],y[3],'r','ro')
p4.set_xlabel("Number of followers")
p4.set_ylabel("Frequency")
p4.set_title("Following Number Distribution with filter_threshold= %d" % filter_thresholds[3])
p4.set_xlim(xmin=0,xmax=1000)
p4.set_ylim(0,80)

plt.show()









