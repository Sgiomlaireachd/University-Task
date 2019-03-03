from collections import Counter
import random
import matplotlib.pyplot as plt

l = []
answer = input("Input a way of filling list (m/f/a):")
if answer == "a":
    amount = 300
    rng = 20
    l = [random.randint(0,rng) for i in range(amount)]
elif answer == "m":
    amount = int(input("Input size:"))
    for i in range(amount):
        l.append(float(input()))
elif answer == "f":
    with open('./file.txt') as file:
        l = [int(i) for i in file.read().split()]
        amount = len(l)
l.sort()
table = Counter()
table.update(l)
values = list(table.values())
keys = list(table.keys())
def functionPlot():
    n = sum(values)
    x = [keys[0] - 1,keys[0]]
    y = [0,0]
    Sum = 0
    for i in range(len(keys)-1):
        Sum += values[i]/n
        x.append(keys[i])
        x.append(keys[i+1])
        y.append(Sum)
        y.append(Sum)
        
    plt.plot(x,y)
    plt.show()
def showSequence():
    print('Sequence:\n',l)
def showTable(keys,values):
    print("Xi",end="\t")
    for key in keys:
        print(key,end="\t")
    print("\nNi",end="\t")
    for val in values:
        print(val,end="\t")
    print()
def findR(n):
    r = 0
    while n > 2 ** r:
        r += 1
    # print("R:",r)
    return r
def getSum(arr):
    sum = 0
    for i in arr:
        sum += table[i]
    return sum
def getContinuousInfo():
    diff = l[-1] - l[0]
    # print("Amount:",amount)
    separator = diff/findR(amount)
    # print("Separator:",separator)
    num = keys[0]
    s = []
    i = 1
    while num + (separator * i) < keys[-1]:
        s.append(num + (separator * i))
        print(s,i,separator*i,num)
        i+=1
    s.append(num + (separator * i))
    # print("S:",s)
    vals = []
    for i in range(len(s)):
        vals.append([])
        end = s[i]
        start = s[i-1] if i > 0 else keys[0]
        for j in range(len(keys)):
            if j == len(keys) - 1:
                if keys[j] >= start and keys[j] <= end:
                    vals[i].append(keys[j])
            else:
                if keys[j] >= start and keys[j] < end:
                    vals[i].append(keys[j])
            if keys[j] > end: break
    # print("VALS:",vals)
    x = [(i[0] + i[-1])/2 for i in vals]
    y = [ getSum(i) for i in vals]
    return x,y,vals,s
def printFunction():
    print("\nFunction:")
    n = sum(values)
    Sum = 0
    print("F(x) = 0,\tx<{}".format(keys[0]))
    for i in range(len(keys) - 1):
        Sum += values[i]/n
        print("F(x) = {},\t{}<=x<{}".format(round(Sum,3),keys[i],keys[i+1]))
    print("F(x) = 1,\tx>={}".format(keys[-1]))
    print()

x,y,vals,s = getContinuousInfo()

def showIntervals():
    opening = "["
    closing = ")"
    s.insert(0,0)
    for i in range(len(s) - 1):
        if i == len(s) - 2: closing = "]"
        print(opening + str(round(s[i],3)) + ", " + str(round(s[i+1],3)) + closing, end="  ")
    print()


def discrette():
    plt.figure(num='Discrette')

    plt.subplot(1,2,1)
    plt.title("Bar chart")
    plt.bar(table.keys(),table.values())

    plt.subplot(1,2,2)
    plt.title("Broken Line")
    plt.plot(table.keys(),table.values())
    plt.show()
def continuous():
    X = []
    Y = []
    for i in range(len(vals)):
        X.extend(vals[i])
        for j in range(len(vals[i])):
            Y.append(y[i])

    plt.figure(num='Continuous')
    plt.subplot(1,2,1)
    plt.title("Bar chart")
    plt.bar(X,Y)

    plt.subplot(1,2,2)
    plt.title("Broken Line")
    plt.plot(X,Y)
    plt.tight_layout()
    plt.show()
def median(keys,values):
    Sum = 0
    if amount % 2:
        # print("NEPARNE",amount%2)
        center = amount//2
        for i in range(len(values)):
            Sum += values[i]
            if Sum >= center:
                # print("Sum:",Sum,i,"Center:",center)
                print("Median:",keys[i])
                return
    else:
        # print("ELSE")
        center = amount//2
        for i in range(len(values)):
            Sum += values[i]
            if Sum >= center:
                # print("Sum:",Sum,i,"Center:",center)
                if Sum >= center + 1:
                    print("Median:",keys[i])
                else:
                    print("Median:",(keys[i] + keys[i+1]) /2)
                return
def mode(keys,values):
    Max = max(values)
    Max_indexes = [i for i in range(len(values)) if values[i] == Max]
    print("Mode:",end=" ")
    for i in Max_indexes: print(keys[i], end=" ")
    print()
def average(keys,values):
    Sum = 0
    for key,val in zip(keys,values):
        Sum += key*val
    print("Average:",Sum/amount)
    return Sum/amount
def deviation(keys,values,avg):
    Sum = 0
    for key,val in zip(keys,values):
        Sum += val * (key - avg) ** 2
    print("Deviation:",Sum)
    return Sum
def swing(keys):
    print("Swing:",keys[-1] - keys[0])
def variance_standart_variation(deviation,avg):
    variance = deviation/(amount-1)
    print("Variance:",variance)
    standard = abs(variance ** 0.5)
    print("Standard:",standard)
    print("Variation:",standard/avg)
def getElementByNumber(keys,values,number):
    i = 0
    Sum = 0
    while Sum < number:
        Sum += values[i]
        i+= 1
    return keys[i-1]
def quantiles(keys, values, number):
    if number == 10: s = "D"
    if number == 4: s = "Q"
    if not amount % number:
        divider = amount // number
        first = getElementByNumber(keys,values,divider)
        for i in range(1,number):
            elem = getElementByNumber(keys,values,i*divider)
            print(s + str(i) + ": x[{}] = {}".format(str(i*divider), str(elem)))
        print("-> Quantile width:",elem-first)
    else:
        print("No quantiles.")
def moments(keys, values, average):
    print("Start moments:")
    for k in range(1,5):
        print("{}:".format(str(k)), end=" ")
        Sum = 0
        for i in range(len(keys)):
            Sum += keys[i] * ((values[i]) ** k)
        moment = Sum/average
        print(moment)
    print("Cantral moments:")
    m = []
    for k in range(1,5):
        print("{}:".format(str(k)), end=" ")
        Sum = 0
        for i in range(len(keys)):
            Sum += keys[i] * ((values[i] - average) ** k)
        moment = Sum/average
        print(moment)
        m.append(moment)
    return m
def assymetry(m):
    print("γ1: {}".format(str(m[2]/(m[1]**(3/2)))))
def excense(m):
    print("γ2: {}".format(str(m[3]/(m[1]**2))))

def discNumericChars():
    print("\n-----> Discrette: <------")
    median(keys,values)
    mode(keys,values)
    avg = average(keys,values)
    dev = deviation(keys,values,avg)
    swing(keys)
    variance_standart_variation(dev,avg)
    print("Quantiles:")
    quantiles(keys,values,4)
    quantiles(keys,values,10)
    m = moments(keys,values,avg)
    assymetry(m)
    excense(m)
def contNumericChars():
    print("\n------> Continuous: <------")
    median(x,y)
    mode(x,y)
    avg = average(x,y)
    dev = deviation(x,y,avg)
    swing(y)
    variance_standart_variation(dev,avg)
    print("Quantiles:")
    quantiles(x,y,4)
    quantiles(x,y,10)
    m = moments(x,y,avg)
    assymetry(m)
    excense(m)

def main():
    showSequence()
    print("\nDiscrette Table:")
    showTable(keys,values)
    printFunction()
    functionPlot()
    discNumericChars()
    discrette()
    print("\nContinuous Table:")
    showIntervals()
    showTable(x,y)
    contNumericChars()
    continuous()

if __name__ == '__main__': main()
