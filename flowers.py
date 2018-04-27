import csv
from moreVec import Vector
import perceptron as pt
import adaline as ad

rows = []


def read_data(filename):
    global rows
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)


def dataSetFromFileName(filename):
    read_data(filename)
    setosa = []
    versicolor = []
    combined = []
    # extract Iris_setosa and Iris-versicolor
    global rows
    for each in rows:
        if each[4] == "Iris-versicolor":
            versicolor.append([each[0], each[2], 1])
        elif each[4] == "Iris-setosa":
            setosa.append([each[0], each[2], 0])

    # print("setosa ----")
    # print(setosa)
    # print("versicolor ====")
    # print(versicolor)
    combined = setosa + versicolor
    # print("combined------")
    # print(combined)

    first_value = []
    second_value = []
    for x in setosa:
        first_value.append(x[0])
    for x in versicolor:
        first_value.append(x[0])
    for x in setosa:
        second_value.append(x[1])
    for y in versicolor:
        second_value.append(y[1])

    first_value = list(map(float, first_value))
    second_value = list(map(float, second_value))

    normalized_data1 = []
    normalized_data2 = []

    for each in first_value:
        normalized_data1.append((each - min(first_value)) / (max(first_value) - min(first_value)))
    for each in second_value:
        normalized_data2.append((each - min(second_value)) / (max(second_value) - min(second_value)))

    formated_list1 = []
    formated_list2 = []

    for each1, each2 in zip(normalized_data1, normalized_data2):
        str1 = format(each1, '.2f')
        str2 = format(each2, '.2f')
        formated_list1.append(str1)
        formated_list2.append(str2)

    index = 0
    for each1, each2 in zip(formated_list1, formated_list2):
        combined[index][0] = list('{0:07b}'.format(int(float(each1) * 100) - 1))
        combined[index][1] = list('{0:07b}'.format(int(float(each2) * 100) - 1))
        index = index + 1

    # print(combined)
    for each in combined:
        # print(each)
        each[0] = each[0] + each[1] + ['1']
        each.remove(each[1])
        temp = ''.join(each[0])
        print(temp)
        temp = temp.replace("-", "0")
        # temp = temp.replace("0","-1")
        print(temp)
        each[0] = list(temp)
        # each[0] = int(each[0])
        each[0] = [int(x) for x in each[0]]
        print(each[0])
        for n, i in enumerate(each[0]):
            if i == 0:
                each[0][n] = -1
        print(each[0])
    # print(combined)

    result = []
    for each in combined:
        each1 = each[0]
        v = (Vector([int(each1[x]) for x in range(len(each1))]), each[1])
        result.append(v)

    # print(result)
    return result


D = dataSetFromFileName("flowers.csv")
# if (D[0] != (Vector(data=[0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1]), 0) or
#     D[-1] != (Vector(data=[0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]), 1)):
#     print("Error in normalizing flowers data")
# p = pt.makePerceptron(.1, 14, lambda: .5, 1)
# pt.train(p,D,1)
# print(p)
# pt.train(p,D,2)
# print(p)
# pt.train(p,D,3)
# print(p)
# pt.train(p,D,4)
# print(p)

a = ad.makeAdaline(.1, 14, lambda: 0.0, 1)
# ad.train(a,D,17)
# print(a)
# ad.train(a,D,18)
# print(a)
# ad.train(a,D,19)
# print(a)
# ad.train(a,D,20)
# print(a)
ad.train(a,D,21)
print(a)
ad.train(a,D,40)
print(a)




# 4b answer:
# The values of the perceptron are as follows after it is trained, using the bound as 4
# Perceptron(eta=0.1, weightVec=Vector(data=[0.5, 0.20000000000000004, -0.19999999999999998, -0.09999999999999998, -0.09999999999999998, 0.10000000000000003, 0.10000000000000003, 0.7, 0.6, 0.30000000000000004, 2.7755575615628914e-17, 0.20000000000000004, 2.7755575615628914e-17, -0.19999999999999998, -0.6]), trace=1)
# 4c answer:
# The values of the Adaline are as follows after it is trained using the bound as 21
# Adaline(eta=0.1, weightVec=Vector(data=[-0.12115716876194214, -0.034371783975996814, -0.01655035129743585, -0.02636204605241367, 0.007996211088722182, -0.03958521513052999, 0.0716434219562489, 0.8213400640763855, 0.5725681947887036, 0.2532474927322912, 0.1266965964660204, 0.09127237158925716, 0.019935105431656528, -0.017223644968048155, 0.06814901031627846]), trace=1)
# Using the bound as 40
# Adaline(eta=0.1, weightVec=Vector(data=[-0.1211571687619423, -0.03437178397599691, -0.016550351297435987, -0.026362046052413764, 0.007996211088722168, -0.03958521513053006, 0.07164342195624888, 0.8213400640763858, 0.5725681947887039, 0.2532474927322912, 0.12669659646602038, 0.09127237158925719, 0.019935105431656473, -0.017223644968048204, 0.06814901031627835]), trace=1)
