class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int numPlayers = skill.size();
        int totalSkill = 0;
        
        unordered_map<int,int> hm;

        for (int s : skill) {
            totalSkill += s;
            hm[s]++;
        }

        int numTeams = numPlayers / 2;
        int teamSkill = totalSkill / numTeams;
        long long res = 0;

        for (auto& [currSkill, currFreq] : hm) {
            int partnerSkill = teamSkill - currSkill;

            if (!hm.contains(partnerSkill) || currFreq != hm[partnerSkill]) {
                return -1;
            }

            res += ((long long)currSkill * (long long)partnerSkill * (long long)currFreq);
        }
        
        // reuturn half as each pair counted twice
        return res / 2;
    }
};