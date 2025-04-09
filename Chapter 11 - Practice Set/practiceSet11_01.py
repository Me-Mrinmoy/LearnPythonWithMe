class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def _str_(self):
        return f"{self.icap}i + {self.jcap}j"    


class C3dVe(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k

    def _str_(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"    

v2d = C2dVec(1,3)
v3d = C3dVe(1, 9, 7)      
print(v2d)
print(v3d)  
