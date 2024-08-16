class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int smallest = INT_MAX;
        int smallestIndex = 0;
        int secondSmallest = INT_MAX;
        int secondSmallestIndex = 0;
        int biggest = INT_MIN;
        int biggestIndex = 0;
        int secondBiggest = INT_MIN;
        int secondBiggestIndex = 0;

        int ans = 0;

        for (int i = 0; i < arrays.size(); i++) {
            vector<int> arr = arrays[i];
            int localMin = arr[0];
            int localMax = arr[arr.size()-1];

            if (localMax > biggest) {
                secondBiggest = biggest;
                secondBiggestIndex = biggestIndex;
                biggest = localMax;
                biggestIndex = i;
            } else if (localMax > secondBiggest) {
                secondBiggest = localMax;
                secondBiggestIndex = i;
            }

            if (localMin < smallest) {
                secondSmallest = smallest;
                secondSmallestIndex = smallestIndex;
                smallest = localMin;
                smallestIndex = i;
            } else if (localMin < secondSmallest) {
                secondSmallest = localMin;
                secondSmallestIndex = i;
            }
        }

        if (biggestIndex != smallestIndex) {
            return biggest - smallest;
        } else {
            return max(biggest-secondSmallest, secondBiggest - smallest);
        }
    }
};