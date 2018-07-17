"""
1.Transform userID into New userID
2.Create new-friendship_dictionary based on newID
"""


# file directory.
data_root="/home/zijie/Stance/Data/Semval2016/"
rname1="Targe_User_list_TaskA.txt"
rname2="User_List_Total_10.txt"
rname3="New_friendship_filtered10.txt"
wname1="User_List_Ids"



target_users=set()
all_users=set()
remaining_users=set()

original_to_new=dict()

###read target userIDS
with open(data_root+rname1,'r') as f:
    cnt=0
    for line in f:
        line=line.rstrip('\r\n')
        cnt=cnt+1
        target_users.add(line)
        original_to_new[line]=cnt

###read remaining userIDS

with open(data_root + rname2, 'r') as f:
    for line in f:
        line=line.rstrip("\r\n")
        all_users.add(line)

remaining_users=all_users-target_users


for user in remaining_users:
      cnt=cnt+1
      original_to_new[user]=cnt


### write user_list_ids
with open(data_root+wname1,'w') as f:
  for (old_ID, new_ID) in original_to_new.items():
     f.write(str(old_ID)+"\t"+str(new_ID)+"\r\n")





###############
wname2="New_UserID_Friendship_10.txt"
wfile=open(data_root+wname2,'w')
with open(data_root+rname3,'r') as f:
    for line in f:
        line=line.rstrip("\r\n")
        parts=line.split("\t")
        user=str(original_to_new[parts[0]])
        friends=list()
        if len(parts[1])>0:
            for friend in parts[1].split(":"):
                friends.append(original_to_new[friend])

            friends_str=":".join([str(i) for i in friends])
        else:
            friends_str="\t"

        num=str(parts[2])
        wfile.write(user+"\t"+friends_str+num+"\r\n")



wfile.close()

