import numpy as np
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
     np_accounts = np.array(accounts)
     row_sums = np.sum(np_accounts, axis=1)
     max_value = np.max(row_sums)
     return int(max_value)
