def jobscheduling(jobs): # jobs: id, dealine, profit
    max_d = max(job[1] for job in jobs)
    slots = [-1]*max_d
    total = 0 
    for jid, d, pro in sorted(jobs, key=lambda x:x[2], reverse=True):
        for t in range(min(max_d, d)-1, -1, -1):
            if slots[t]==-1:
                slots[t] = jid
                total += pro
                break
    return total, [jid for jid in slots if jid!=-1]

jobss = [
    (1, 2, 100),  # Job 1: deadline=2, profit=100
    (2, 1, 19),   # Job 2: deadline=1, profit=19
    (3, 2, 27),   # Job 3: deadline=2, profit=27
    (4, 1, 25),   # Job 4: deadline=1, profit=25
    (5, 3, 15)    # Job 5: deadline=3, profit=15
]
print(jobscheduling(jobss))


