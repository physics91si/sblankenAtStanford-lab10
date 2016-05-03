
class Set:
    def __init__(self):
        self.list = []
    def __contains__(self, object):
        for i in self.list : 
            if(object == i):
                return True
        return False 
    def __add__(self, object):
         if not self.__contains__(object):
            self.list.append(object)
    def __remove__(self, object) :
            if(self.__contains__(object)):
                self.list.remove(object)
    def __size__(self):
        num = 0;
        for i in self.list:
            num = num + 1
        return num        
    def __str__(self):
        return str(self.list)
    def __union__(self, other):
        result = Set()
        for i in self.list + other.list:
            result.__add__(i)
        return result
    def __intersection__(self, other):
        result = Set()
        for i in self.list:
            if(other.__contains__(i)):
                result.__add__(i)
        return result
    def __subtract__(self,other):
        result = Set()
        for i in self.list:
            if(not other.__contains__(i)):
                result.__add__(i)
        return result
       
               
            
      
            
        