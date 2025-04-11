class Vector:
    def __init__(self, vec):
        self.vec = vec

    def _str_(self):
        str1 = ""
        index = 0
        for i in range(len(self.vec)):
            str += f"{i}a{index} +"
            index +=1
        return str1[:-1]
    
    def _add_(self,vec2):
           newList = []
    for i in range(len(self.vec)):
               newList.append(self.vec[i]) + vec2.vec[i]
            return Vector(newList)  

    def _mul_(self,vec2):
           sum = 0
    for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
            return sum
  
v1 = Vector([1,4,6])
v2 = Vector([1,6,9])  
print(v1 + v2)
print(v1 * v2)