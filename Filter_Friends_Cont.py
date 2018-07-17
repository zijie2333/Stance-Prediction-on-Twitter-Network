"""
This is for filter friendship.
Parameters:
      filter_threshold
      num_of_actual_user: targeted user number

"""
filter_threshold=25
num_of_actual_user=2713



###################################Input filename

root="/home/zijie/Stance/Data/Semval2016/"
rname="User_Friendship_Total_FINAL_TASKA.txt"
wname="New_friendship_filtered"+str(filter_threshold)+".txt"
wname2="User_List_Total_"+str(filter_threshold)+".txt"
wfile=open(root+wname,'w')
wfile2=open(root+wname2,'w')



def dict_update(friend_list,friends_dict):
    for friend in friend_list:
        if not friends_dict.has_key(friend):
            friends_dict[friend]=1
        else:
            friends_dict[friend]+=1


friends_dict=dict()
user_set=set()
with open(root+rname,'r') as f:
    for line in f:
        if line.startswith('UserID\t'):
          continue
        line=line.rstrip("\r\n")
        parts=line.split("\t")
        user=parts[0]
        user_set.add(user)
        if not friends_dict.has_key(user):
            friends_dict[user]=0
        friend_list=parts[1].split(":")
        dict_update(friend_list, friends_dict)



for (userID, counts) in friends_dict.items():
    if counts >=filter_threshold:
        user_set.add(userID)


friends_num_total=0
no_friends_count=0
with open(root+rname,'r') as f:
    for line in f:
        line=line.rstrip("\r\n")
        parts=line.split("\t")
        user=parts[0]
        friend_list=parts[1].split(":")
        friend_new_list=list()
        for friend in friend_list:
            if friend in user_set:
                friend_new_list.append(friend)

        friends_num=len(friend_new_list)
        if friends_num==0:
            no_friends_count+=1
        friend_list_str=":".join([str(friend) for friend in friend_new_list])
        string=parts[0]+"\t"+friend_list_str+"\t"+str(friends_num)
        wfile.write(string+"\r\n")
        friends_num_total+=friends_num

wfile.close

avg=friends_num_total/num_of_actual_user

print "number of users= %d" % len(user_set)
print "average number of friends per user = %d" % avg
print "number of users without friends= %d" % no_friends_count




for userID in user_set:
    wfile2.write(userID+"\r\n")

wfile2.close()




