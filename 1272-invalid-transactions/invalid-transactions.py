class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = defaultdict(list) 

        for i, t in enumerate(transactions):
            name, time_str, amt_str, city = t.split(",")
            time = int(time_str)
            amt = int(amt_str)
            parsed[name].append((time, amt, city, i)) # apppend index as well so we can map it back
        
        invalid = set()

        for transaction_list in parsed.values():
            transaction_list.sort(key=lambda x: x[0])

            for l, (time, amt, city, idx) in enumerate(transaction_list):
                if amt > 1000:
                    invalid.add(idx)
                
                r = l + 1
                while r < len(transaction_list) and transaction_list[r][0] - time <= 60:
                    if city != transaction_list[r][2]:
                        invalid.add(idx)
                        invalid.add(transaction_list[r][3])
                    r += 1
        
        return [transactions[i] for i in invalid]