names = tuple(("areasus","pannu","kalu","dallu"))
iterator = iter(names) #also can for strings
print(next(iterator))
print(next(iterator))
print(next(iterator))

class nameIterator:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x= self.a
        self.a+=1
        return x
    
numbers = nameIterator()
myiter = iter(numbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
