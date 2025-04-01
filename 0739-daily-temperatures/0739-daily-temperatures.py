class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        hottest = temperatures[-1]
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            j = i+1
            while temperatures[j] <= temperatures[i]:
                j += output[j]
            output[i] = j-i
        return output