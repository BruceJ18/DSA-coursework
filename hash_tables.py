# hash tables  coursework Assignment 2

# does not include linear probing
class BasicHashTable:

    MAX_HASH_TABLE_SIZE = 4096


    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size


    def get_index(self, string):
        total_sum_letters = 0
        for letter in string:
            letter_to_int = ord(letter)
            total_sum_letters += letter_to_int
        list_index = total_sum_letters % len(self.data_list)
        return list_index


    def insert(self, key, value):
        hash_index = self.get_index(key)
        while True:
            if self.data_list[hash_index] is not None:
                hash_index += 1
            else:
                self.data_list[hash_index] = (key, value)
                break


    def find(self, key):
        hash_index = self.get_index(key)
        value = self.data_list[hash_index]
        if value is None:
            return None
        else:
            return value

    def update(self, key, value):
        hash_index = self.get_index(key)
        self.data_list[hash_index] = (key, value)


    def list_all(self):
        pairs = [key[0] for key in self.data_list if key is not None]
        return pairs



# includes linear probing
class ProbingHashTable:

    MAX_HASH_TABLE_SIZE = 4096


    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list2 = [None] * max_size


    def get_index(self, string):
        total_sum_letters = 0
        for letter in string:
            letter_to_int = ord(letter)
            total_sum_letters += letter_to_int
        list_index = total_sum_letters % len(self.data_list2)
        return list_index


    def get_valid_index(self, key):
        hash_index = self.get_index(key)
        while True:
            kv = self.data_list2[hash_index]
            if kv is None:
                return hash_index
            k, v = kv
            if k == self.data_list2[hash_index][0]:
                return hash_index
            hash_index += 1
            if hash_index == len(self.data_list2):
                hash_index = 0


    def insert2(self, key, value):
        hash_index = self.get_valid_index(key)
        self.data_list2[hash_index] = (key, value)


    def find2(self, key):
        hash_index = self.get_valid_index(key)
        kv = self.data_list2[hash_index]
        return None if kv is None else kv[1]


    def update2(self, key, new_value):
        hash_index = self.get_valid_index(key)
        self.data_list2[hash_index] = (key, new_value)


    def list_all2(self):
        pairs = [key[0] for key in self.data_list2 if key is not None]
        return pairs





