class Twitter {
public:
    unordered_map<int, unordered_set<int>> friends;

    // userId: {time, tweetId}
    unordered_map<int, vector<pair<int,int>>> tweets;

    // for knowing how recent tweet is in maxHeap
    int time = 0;

    Twitter() {
        
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({++time, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        // same as merge k sorted list

        // maxHeap: contains {time, userId, index, tweetId}
        // time is first so that pq is sorted by max Time
        priority_queue<vector<int>> pq; 
        vector<int> ans;

        for (auto &f : friends[userId]) {
            // if friends have tweets
            if (tweets[f].size()) {
                // add their latest tweet info
                auto [time,tId] = tweets[f].back();
                pq.push({time, f, (int)tweets[f].size()-1, tId});
            }
        }

        // add user latest tweet info
        if (tweets[userId].size()) {
            auto [time,tId] = tweets[userId].back();
            pq.push({time, userId, (int)tweets[userId].size()-1, tId});
        }

        // pull the 10 latest tweets
        int k = 10;
        while (k-- > 0 && !pq.empty()) {
            vector<int>v = pq.top(); // [time, userId, index, tweetId]
            pq.pop();
            ans.push_back(v[3]);

            // add the next latest tweet from user that was popped
            if (v[2] != 0) {
                auto [newTime, newTweetId] = tweets[v[1]][v[2]-1];
                pq.push({newTime,v[1],v[2]-1,newTweetId});
            }
        }

        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        friends[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (friends[followerId].contains(followeeId)) {
            friends[followerId].erase(followeeId);
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */