from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:  
            return 1  # If there's only one person and no trust relationships, they are the judge
        
        trust_count = [0] * (n + 1)  # Stores how many people trust `i`
        trusted_by_others = [0] * (n + 1)  # Stores if `i` trusts someone (1 if they trust, 0 otherwise)
        
        for a, b in trust:
            trust_count[b] += 1  # Person `b` is trusted by `a`
            trusted_by_others[a] = 1  # Person `a` trusts someone, so they can't be a judge

        # The judge should be trusted by `n-1` people and trust nobody
        for i in range(1, n + 1):
            if trust_count[i] == n - 1 and trusted_by_others[i] == 0:
                return i

        return -1
