using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'getMinTime' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY task_memory
 *  2. INTEGER_ARRAY task_type
 *  3. INTEGER max_memory
 */

int getMinTime(vector<int> task_memory, vector<int> task_type, int max_memory) {
    int ans = 0;
    
    map<int, vector<int>> hm;
    for (int i=0; i < task_type.size(); i++) {
        hm[task_type[i]].push_back(task_memory[i]);
    }
    
    // iterate through map, add number of units to answer
    for (auto entry: hm) {
        vector<int>& memories = entry.second;
        sort(memories.begin(), memories.end());
        
        int left = 0;
        int right = memories.size() - 1;
        
        while (left <= right) {
            if (left == right) {
                ans++;
                break;
            }
            
            if (memories[left] + memories[right] <= max_memory) {
                left++;
                right--;
                ans++;
            } else {
                // process right alone
                right--;
                ans++;
            }
        }
    }
    
    return ans;
}
