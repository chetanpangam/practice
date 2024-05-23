
class HashTable:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    def find_key(self, key, bucket):
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                return index
        return -1
    
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        index = self.find_key(key, bucket)
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if index != -1:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        index = self.find_key(key, bucket)
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if index != -1:
            return bucket[index][1]
        else:
            return "No record found"
 
    # Remove a value with specific key
    def delete_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        index = self.find_key(key, bucket)
        
        if index != -1:
            bucket.pop(index)
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
 
 
hash_table = HashTable(50)
print(hash_table)
print()
# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()
 
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
 
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
 
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)