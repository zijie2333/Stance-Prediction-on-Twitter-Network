"""
1.Transform twitterID into New twitterID
2.Create new-friendship_dictionary based on newID
"""


# file directory.
data_root="/home/zijie/Stance/Data/Semval2016/"
rnames=["testdata-taskA-twitter-user-ids.txt","testdata-taskB-twitter-user-ids.txt"\
    ,"trainingdata-twitter-user-ids.txt","trialdata-twitter-user-ids.txt"]
wname1="Tweet_User_List_Ids.txt"
rname2="User_List_Ids.txt"


all_tweets=set()
original_to_new=dict()


##################################renumber tweets
for rname in rnames:
    with open(data_root+rname,'r') as f:
        for line in f:
            line=line.rstrip("\r\n")
            if len(line)>5:
                parts=line.split("\t")
                if parts[2]!='0':
                    all_tweets.add(parts[0]+"\t"+parts[1]+"\t"+parts[2])


cnt=0
for tweet in all_tweets:
    cnt+=1
    original_to_new[tweet]=cnt

########writing format: new-tweet-id    old-new-tweet-id    original-tweet-id   original-user-id
with open(data_root+wname1,'w') as f:
    for (old_tweet, new_tweet) in original_to_new.items():
        f.write(str(new_tweet)+"\t"+old_tweet+"\r\n")


#####reading new user IDS
original_to_new_users=dict()
with open(data_root+rname2,'r') as f:
    for line in f:
        line=line.rstrip("\r\n")
        if len(line)>5:
            parts=line.split("\t")
            original_to_new_users[parts[0]]=parts[1]




