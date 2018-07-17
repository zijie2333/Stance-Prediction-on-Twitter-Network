"""
1.Writing in the following form:
New_Tweet_ID \t Target \t Tweet \t New_User_ID \t New_friend_IDS(new_id1:new_id2:new_id3.....) \t Stance

"""


# file directory.
data_root="/home/zijie/Stance/Data/Semval2016/"
rnames=["testdata-taskA-twitter-user-ids.txt","testdata-taskB-twitter-user-ids.txt"\
    ,"trainingdata-twitter-user-ids.txt","trialdata-twitter-user-ids.txt"]

rnames2=["testdata-taskA-all-annotations.txt","testdata-taskB-all-annotations.txt",\
        "trainingdata-all-annotations.txt","trialdata-all-annotations.txt"]

wnames=["Test_A_ALL.txt","Test_B_ALL.txt","Training_ALL.txt","Trial_ALL.txt"]

ruser="User_List_Ids.txt"
rtweetuser="Tweet_User_List_Ids.txt"
rfriends="New_UserID_Friendship_10.txt"

#construct old_new_tweet_id ->> new tweet id
old_to_new_tweet=dict()
old_tweet_to_old_user=dict()
with open(data_root+rtweetuser,"r") as f:
    for line in f:
        if len(line)>5:
            line=line.rstrip("\r\n")
            parts=line.split("\t")
            old_to_new_tweet[parts[1]]=parts[0]
            old_tweet_to_old_user[parts[1]]=parts[3]

#constrct new_tweet_id ->>>new_user_ID
old_to_new_user=dict()
with open(data_root + ruser, "r") as f:
    for line in f:
        if len(line) > 5:
            line = line.rstrip("\r\n")
            parts = line.split("\t")
            old_to_new_user[parts[0]]=parts[1]


#construct new_tweet_id ->>>new friends ids
new_to_new_friends=dict()
with open(data_root + rfriends, "r") as f:
    for line in f:
        if len(line) > 5:
            line = line.rstrip("\r\n")
            parts = line.split("\t")
            new_to_new_friends[parts[0]]=parts[1]


cnt=0
for rname in rnames2:
    wfile=open(data_root+wnames[cnt],'w')
    with open(data_root+rname,'r')as f:
        for line in f:
            if line.startswith("ID\t"):
                continue

            line=line.rstrip("\r\n")
            parts=line.split("\t")
            old_tweet_id=parts[0]
            target=parts[1]
            tweet=parts[2]
            stance=parts[3]
            if old_to_new_tweet.has_key(old_tweet_id):
                new_tweet_id=old_to_new_tweet[old_tweet_id]
                old_user_id=old_tweet_to_old_user[old_tweet_id]
                new_user_id=old_to_new_user[old_user_id]
                new_friends_ids=new_to_new_friends[new_user_id]
                information=[new_tweet_id,target,tweet,new_user_id,new_friends_ids,stance]
                string="\t".join([str(i) for i in information])
                wfile.write(string+"\r\n")

    cnt+=1

