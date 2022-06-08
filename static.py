class static:
    noe=0
    @staticmethod
    def unoe():
        static.noe +=1

employ1=static()
employ2=static()
employ1.unoe()
employ2.unoe()
print(static.noe)