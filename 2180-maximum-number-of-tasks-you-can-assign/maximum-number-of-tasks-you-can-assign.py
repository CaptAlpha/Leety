class Solution:
    def can_assign(self, tasks, workers, m, strength, pills):
        m_largest_workers = collections.deque(workers[-m:])
        for i in range(m-1, -1, -1):
            if not m_largest_workers:
                return False
            if m_largest_workers[-1] >= tasks[i]:
                m_largest_workers.pop()
            else:
                if pills == 0:
                    return False
                idx = bisect.bisect_left(m_largest_workers, tasks[i] - strength)
                if idx == len(m_largest_workers):
                    return False
                pills -= 1
                del m_largest_workers[idx]
        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        l, r = 0, len(tasks)
        while l < r:
            m = l + (r-l)//2
            if self.can_assign(tasks, workers, m, strength, pills):
                l = m+1
            else:
                r=m
        return l if self.can_assign(tasks, workers, l, strength, pills) else (l-1)

        