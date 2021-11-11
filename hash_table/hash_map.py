class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)  # ord() is used to get the ascii code of inputs. 
        return hash % self.MAX
    
    def __setitem__(self, key, value):  # before name is add now is __setitem__
        hash = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[hash]):
            if len(element)==2 and element[0]==key:
                self.arr[hash][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[hash].append((key,value))
    
    def __getitem__(self, key): # before name is get now is __getitem__
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][index]

obj = HashTable()
obj["march 6"] = 120
obj["march 6"] = 78
obj["march 8"] = 67
obj["march 9"] = 4
obj["march 17"] = 459
#del obj["march 6"]
print(obj.arr)
print(obj["march 6"])
del obj["march 17"]
print(obj.arr)
#before used
# obj.add("march 6", 99)
# print(obj.get("march 6"))