#   insert, Lookup, Delete

class HashMap:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _bucket_index(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        for i, (k, _)in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
    
    def get(self, key):
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
    

    def remove(self, key):
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]       
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
        raise KeyError(key)
    