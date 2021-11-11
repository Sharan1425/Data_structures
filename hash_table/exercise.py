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
    
    def avg_first_week(self, keys):
        total_temp = 0
        for key in keys:
            total_temp += self.__getitem__(key)
        avg_temp = total_temp/len(keys)
        return avg_temp
    
obj = HashTable()
obj["Jan 1"]=27
obj["Jan 2"]=31
obj["Jan 3"]=23
obj["Jan 4"]=34
obj["Jan 5"]=37
obj["Jan 6"]=38
obj["Jan 7"]=29
obj["Jan 8"]=30
obj["Jan 9"]=35
obj["Jan 10"]=30
print(obj.arr)
inputs = ["Jan 1","Jan 2","Jan 3","Jan 4","Jan 5","Jan 6","Jan 7"]
print("Average Temp in first week of jan :", obj.avg_first_week(inputs))
