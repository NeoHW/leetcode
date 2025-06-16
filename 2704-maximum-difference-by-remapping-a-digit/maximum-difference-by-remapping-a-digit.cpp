class Solution {
public:
    int minMaxDifference(int num) {
        string biggest = to_string(num);
        string smallest = biggest;
        size_t pos = biggest.find_first_not_of('9');

        if (pos != string::npos) {
            char a = biggest[pos];
            replace(biggest.begin(), biggest.end(), a, '9');
        }

        char b =  smallest[0];
        replace(smallest.begin(), smallest.end(), b, '0');
        return stoi(biggest) - stoi(smallest);
    }
};