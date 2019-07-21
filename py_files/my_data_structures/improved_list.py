import collections.abc

class ImprovedList(collections.abc.MutableSequence):
    
    __slots__ = ["__inner_list", "__size", "__max_elem"]
    
    def __init__(self, args):
        super().__init__()
        if isinstance(args, list):
            self.__inner_list = args
        else:
            self.__inner_list = list(args)
        self.__size = len(self.__inner_list)
        self.__max_elem = max(args)
        
    def __if_bigger(self, item):
        if self.__max_elem < item:
            self.__max_elem = item        
        
    @property
    def max_elem(self):
        return self.__max_elem
        
    def __len__(self):
        return self.__size
    
    def __getitem__(self, index):
        return self.__inner_list[index]
    
    def __setitem__(self, index, item):
        is_bigger = False
        if self.__inner_list[index] == self.__max_elem:
            is_bigger = True
        else: 
            self.__if_bigger(item)        
        self.__inner_list[index] = item
        if is_bigger:
            self.__max_elem = max(self.__inner_list)
        
    def __delitem__(self, key):
        is_bigger = False
        if  self.__inner_list[key] == self.max_elem:
            is_bigger = True
        del  self.__inner_list[key]
        if is_bigger:
            self.__max_elem = max(self.__inner_list)
        self.__size -= 1
        
    def insert(self, index, item):
        self.__inner_list.insert(index, item)
        self.__size += 1
        self.__if_bigger(item)
        
    def __str__(self):
        lst = self.__inner_list[self.__size - 1]
        res = ""
        for elem in self.__inner_list:
            if not elem == lst:
                res += "{}, ".format(elem)
            else:
                res += "{}".format(elem)
        return "$"+ res + "$"
            
    
a = ImprovedList([4, 3, 1])
print(a.max_elem)
a.insert(0, 5)
print(a.max_elem)
a[0] = 1
print(a.max_elem)