"""
This is for counting friendship number for
filtered and unfiltered friendship datasets.
"""


root="/home/zijie/Stance/Data/Semval2016/"
rname1="User_Friendship_Total_FINAL_TASKA.txt"
rname2="New_friendship_filtered.txt"
wname="friendship_count.txt"
wfile=open(root+wname,'w')

original=dict()
new_numbers=dict()
num_of_users=int(2714)
with open(root+rname1,'r') as f:
    for line in f:
        if len(line)>5:
            line=line.rstrip("\r\n")
            parts=line.split("\t")
            friend_list=parts[1].split(":")
            original[parts[0]]=len(friend_list)


with open(root+rname2,'r') as f:
    for line in f:
        if len(line)>5:
            line=line.rstrip("\r\n")
            parts=line.split("\t")
            new_numbers[parts[0]]=parts[2]




original_total=0
new_total=0
for (userID,original_count) in original.items():
    new_count=new_numbers[userID]
    string=userID+"\t"+str(original_count)+"\t"+str(new_count)
    wfile.write(string+'\r\n')
    original_total+=int(original_count)
    new_total+=int(new_count)





