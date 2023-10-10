class MyHashMap:

    def __init__(self):
        self.ks = []
        self.vs = []

    def put(self, key: int, value: int) -> None:
        if key in self.ks:
            self.vs[self.ks.index(key)] = value
        else:
            self.ks.append(key)
            self.vs.append(value)

    def get(self, key: int) -> int:
        if key in self.ks:
            return self.vs[self.ks.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.ks:
            ind = self.ks.index(key)
            self.ks.pop(ind)
            self.vs.pop(ind)

class MyHashMap2:

    def __init__(self):
        self.m = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m[key]

    def remove(self, key: int) -> None:
        self.m[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == "__main__":
    cases = [
        [
            ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
            [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
        ]
    ]
    ans = []
    for c in cases:
        for i in range(len(c[0])): 
            method_name = c[0][i]
            args = c[1][i]
            if method_name == "MyHashMap":
                obj = MyHashMap2()
                ans.append(None)
            elif method_name == "put":
                ans.append(obj.put(*args))
            elif method_name == "get":
                ans.append(obj.get(*args))
            elif method_name == "remove":
                ans.append(obj.remove(*args))
    print('passed' if ans == [None, None, None, 1, -1, None, 1, None, -1] else 'failed')