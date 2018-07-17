##### This is the dataset description.


1.Airlines: Contains tweets about 5 airline companies and their judges.  (1W+)
   	    need to crawl user friendships


2.GOP: Contains tweets about hilary and trump.    (1W+)
       need to crawl user friendships.

3.HEALTH: Contains tweets about health issue.  (4500)    https://bitbucket.org/speriosu/updown/src/1deb8fe45f60/data/?at=default
          need to crawl user friendships( I think the friendship provided is incomplete.)	


4. Semval2016: official data for Semval2016 Task 6

5. Bistance: a version of the Semval2016 Task 6


6.data format:

#training_all_data, test_all_data, trial_all_data:
        New_Tweet_ID \t Target \t Tweet \t New_User_ID \t New_friend_IDS(new_id1:new_id2:new_id3.....) \t Stance


#user_list_ids:
       User_ID \t New_User_ID

#tweet_list_ids
       tweet_ID \t New_tweet_id

#New_friendship_filtered(5,10,15,20,25)
       User_ID \t friend_Ids(id1:id2:id3.....) \t total_friends_count
