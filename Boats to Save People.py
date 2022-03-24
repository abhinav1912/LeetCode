class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        i,j = 0, len(people)-1
        while i<=j:
            ans += 1
            if i==j:
                break
            elif people[i]+people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
        return ans
