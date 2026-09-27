import bisect
from typing import List

class Solution:

    def maxEarnings(self, meetings: List[List[int]]) -> int:
        # Sort meetings by their end times
        meetings.sort(key=lambda x: x[1])

        # dp stores pairs of [end_time, max_chain_value_so_far]
        dp = []
        max_earnings = 0

        for s, e, r in meetings:
            w = s + r - e

            # Find the maximum chain value that ends at or before the current start time 's'
            idx = bisect.bisect_right(dp, [s, float("inf")]) - 1
            max_prev = dp[idx][1] if idx >= 0 else float("-inf")

            # Calculate the best chain value ending exactly at 'e' using this meeting
            best_at_e = max(-s, max_prev) + w

            # Total earnings if this meeting is the final meeting in the chain
            max_earnings = max(max_earnings, best_at_e + e)

            # Maintain the prefix maximum in the dp array
            current_max = dp[-1][1] if dp else float("-inf")
            if best_at_e > current_max:
                if dp and dp[-1][0] == e:
                    dp[-1][1] = max(dp[-1][1], best_at_e)
                else:
                    dp.append([e, best_at_e])

        return max_earnings
