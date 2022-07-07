



range_ = int(input("Ведите количество элементов последовательности :"))

#простая реализация
t1 = 0
t2 = 0
t3 = 1
range1 = range_
for i in range(range1):
    sum1 = t1 + t2 + t3
    print(t1)
    t1 = t2
    t2 = t3
    t3 = sum1

print("********************************")

# реализация через список
start = [0, 0, 1]
range2 = range_

while 1:
    if len(start) >= range2:
        break
    next_element = sum(start[-3:])
    start.append(next_element)
print(start)
print("********************************")

# реализация генератором

range3 = range_
def tribonacci_gener(range_3):
    t1, t2, t3 = 0, 0, 1  # start
    for i in range(range_3):
        t1, t2, t3 = t2, t3, t1 + t2 + t3
        yield t1
#выззов tribonacci_gener
t = tribonacci_gener(range3)
for i in range(range3-1):
    print(next(t))
