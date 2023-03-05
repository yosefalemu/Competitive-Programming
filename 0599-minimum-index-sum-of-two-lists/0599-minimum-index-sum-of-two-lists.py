class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        dict2 = {}
        dict3 = {}
        index = 0
        ans = []
        min_value = 0
        for c in list1:
            dict1.update({c:index})
            index += 1
        index = 0
        for c in list2:
            dict2.update({c:index})
            index += 1
        for c in dict1:
            if c in dict1 and c in dict2:
                dict3.update({c:(dict1[c] + dict2[c])})
        min_value = min(dict3.values())
        for x, y in dict3.items():
            if y == min_value:
                ans.append(x)
        return ans
            
        
                
        