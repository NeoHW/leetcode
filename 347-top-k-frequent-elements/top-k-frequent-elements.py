class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            # 3. move pivot to correct position (store index)
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            '''
            Sorts a list within left...right till kth less frequent element takes its place
            '''

            # base case
            if left == right:
                return
            
            # select a random pivot
            pivot_index = random.randint(left, right)

            # find pivot's actual position
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == k_smallest:
                return
            elif pivot_index > k_smallest: # go left
                quickselect(left, pivot_index, k_smallest)
            else:
                quickselect(pivot_index, right, k_smallest)


        # back to main function
        n = len(unique)
        quickselect(0, n-1, n-k)
        
        # return the right part which is top k most frequent
        return unique[n-k:]