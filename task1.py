class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in range(len(self.table[key_hash])):
                if self.table[key_hash][pair][0] == key:
                    self.table[key_hash].pop(pair)
                    return True  
            return False 
        return False


# Тест
hash_table = HashTable(5)
hash_table.insert("Олена", 25)
hash_table.insert("Іван", 30)
hash_table.insert("Марія", 35)

print(hash_table.get("Олена"))   # : 25
print(hash_table.get("Іван"))    # : 30
print(hash_table.get("Марія"))   # : 35

print(hash_table.delete("Олена"))   # Видалення "Олена", : True
print(hash_table.delete("Іван"))    # Видалення "Іван", : True
print(hash_table.delete("Марія"))   # Видалення "Марія", : True

print(hash_table.get("Олена"))   # Очікується: None,
print(hash_table.get("Іван"))    # Очікується: None
print(hash_table.get("Марія"))   # Очікується: None
