class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = deque()
        for i in range(len(logs), 0, -1):
            for j in range(i):
                if (j + 1) == len(logs):
                    break
                if re.match("[0-9]", logs[j].split()[1]):
                    nums.appendleft((logs.pop(j)))
                if self.isGreater(logs[j], logs[j + 1]):
                    logs[j], logs[j + 1] = logs[j + 1], logs[j]
        logs = logs + list(nums)
        return logs
            
    def isGreater(self, origin: str, new: str):
        s_origin = origin.split()
        s_new = new.split()
        
        count = len(s_origin) if len(s_origin) < len(s_new) else len(s_new)
        
        for i in range(1, count):
            inner_count = len(s_origin[i]) if len(s_origin[i]) < len(s_new[i]) else len(s_new[i])
            
            for j in range(inner_count):
                if ord(s_origin[i][j]) > ord(s_new[i][j]):
                    return True
                if ord(s_origin[i][j]) < ord(s_new[i][j]):
                    return False
                
            if len(s_origin) != len(s_new):
                return False if len(s_origin) < len(s_new) else True