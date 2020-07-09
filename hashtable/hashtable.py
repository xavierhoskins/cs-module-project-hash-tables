class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
            self.storage = [None] * self.capacity
        else:
            print(f"ERROR: enter capacity {MIN_CAPACITY}")
            self.capacity = MIN_CAPACITY
        self.s_keys = 0
        self.load_factor = 0.7
        self.FNV_prime = 0x100000001b3
        self.FNV_offset = 0xcbf29ce484222325 



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return self.capacity
      
  # help 
    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

        hash_value = FNV_offset
        for i in key:
            hash_value *= FNV_prime
            hash_value ** ord(i)
        return FNV_offset

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here

        hash_value = 0

        for i in key:
            hash_value = (hash_value * 33) + ord(i)
        return hash_value


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        target = self.hash_index(key)
        item = self.storage[target]
        if not item:
            self.storage[target] = HashTableEntry(key,value)
        else:
            prev_enter = None
            while item:
                if item.key == key:
                    item.value= value
                    return

                prev_enter = item
                item = item.next

            item = HashTableEntry(key,value)
            prev_enter.next = item

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        if self.s_keys / self.capacity:
            if self.capacity >= 8:
                self.resize(self.capacity)
        target = self.hash_index(key)
        item = self.storage[target]
        if not item:
            print('key not found')

        else:
            prev_enter = None
            while item:
                if item.key == key:
                    if prev_enter:
                        item.value = None
                        return
                    else:
                        item.value = None
                        return
                prev_enter = item
                item = item.next
            print('key not found')
                

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        
        #get value stored with given key
        target = self.hash_index(key)
        item = self.storage[target]
        if item:
            # while loop
            while item:
                if item.key == key:
                    # if key is found return value
                    return item.value
                item = item.next

        # if the key not found return None          
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here

        self.capacity = new_capacity
        orig_storage = self.storage
        self.storage = [None] * self.capacity

        for item in orig_storage:
            while item:
                self.put(item.key, item.value)
                item = item.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

