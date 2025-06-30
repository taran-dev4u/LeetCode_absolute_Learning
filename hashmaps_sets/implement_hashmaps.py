class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
            
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k==key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return True
        return False
    
    def __str__(self):
        return str(self.buckets)
    
hm = HashMap()
hm.put("apple", 1)
hm.put("banana", 2)
print(hm.get("apple"))    # ➜ 1
hm.put("apple", 100)
print(hm.get("apple"))    # ➜ 100
hm.remove("banana")
print(hm.get("banana"))   # ➜ None
      