from Simple_generator_triponacchi import range_


class Tribonachi_iter:
    def __iter__(self):
        return self

    def __init__(self, range_):
        self.range_ = range_
        self.t1 = 0
        self.t2 = 0
        self.t3 = 1


    def __next__(self):
        for i in range(range_):
            sum1 = self.t1 + self.t2 + self.t3
            print(self.t1)
            self.t1 = self.t2
            self.t2 = self.t3
            self.t3 = sum1

        else:
            raise StopIteration

print("реализачия через экземпляр класса")
iter = Tribonachi_iter(range_)
for i in iter:
    print(i)



