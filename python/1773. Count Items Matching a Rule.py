from typing import List

# straight forward approach, just check each key in items
def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    dic = {'type': 0,'color': 1,'name': 2}
    count = 0
    for i in items:
        if i[dic[ruleKey]] == ruleValue:
            count += 1
    return count

# approach using n space
def countMatches2(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    dic = {
        'type': 0,
        'color': 1,
        'name': 2
    }
    arr = [i[dic[ruleKey]] for i in items]
    return arr.count(ruleValue)

if __name__ == '__main__':
    cases = [
        [[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver",1],
        [[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone",2]
    ]
    for case in cases:
        print(countMatches2(case[0],case[1],case[2]),'|',case[3])