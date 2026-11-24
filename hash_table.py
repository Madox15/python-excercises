# freeCodeCamp hash table certification project


class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(
        self, key
    ):  # Take a string as a parameter. Return a hashed value computed as the sum of the Unicode code points of each character in the string. You can use the ord function to get the code point of each character.
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(
        self, key, value
    ):  # Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary. If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value.
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {key: value}
        else:
            self.collection[hashed_key][key] = value

    def remove(
        self, key
    ):  # Remove the corresponding key-value pair from the hash table. If the key does not exist in the collection, it should not raise an error or remove anything.
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    def lookup(
        self, key
    ):  # Compute the hash of the key, and return the corresponding value stored inside the hash table. If the key does not exist in the collection, it should return None.
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        else:
            return None
