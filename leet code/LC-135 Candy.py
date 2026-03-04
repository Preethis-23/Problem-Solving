class Solution:
    def candy(self, ratings):
        n = len(ratings)
        lr = [1] * n
        rl = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                lr[i] = lr[i-1] + 1     # in qsn given that, current kid's candy should be higher than prev if rating[i] > ratign[i-1]

        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                rl[j] = rl[j+1] + 1     # same statement in reverse order

        total = 0
        for k in range(n):
            total += max(lr[k], rl[k])

        return total
