class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a, b, cost = [], [], 0
        for i in costs:
            if i[0] < i[1]:
                a.append(i[1]-i[0])
                cost += i[0]
            else:
                b.append(i[0]-i[1])
                cost += i[1]
        x = abs(len(a)-len(b))//2
        if len(a) < len(b):
            b.sort()
            cost += sum(b[:x])
        else:
            a.sort()
            cost += sum(a[:x])
        return cost
