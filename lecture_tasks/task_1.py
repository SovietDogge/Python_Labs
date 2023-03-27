import numpy as np


# ex 1 L1
def ex_1():
    print(np.version)
    print(np.__version__)


# ex 2 L1
def ex_2():
    exmpl_arr = np.array([1, 2, 3, 4, 55])
    print(exmpl_arr)


# ex 8 L2
def ex_8():
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)

    print(a)
    print(b)
    print(np.vstack((a, b)))


# ex 9 L2
def ex_9():
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    print(np.hstack((a, b)))


# ex 10 L2
def ex_10():
    a = np.array([1, 2, 3])
    b = np.array(np.repeat(a, 3))
    c = np.array(np.tile(a, 3))
    d = np.append(b, c)
    print(d)


# ex 11 L2
def ex_11():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    is_common = []

    for item in a:
        if item in b:
            is_common.append(True)
        else:
            is_common.append(False)

    print(np.unique(a[is_common]))


# # ex 34 L3
def ex_34():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

    condition = []
    for row in iris_2d:
        if row[0] < 5 and row[2] > 1.5:
            condition.append(True)
        else:
            condition.append(False)

    print(iris_2d[condition])


# ex 58 L3
def ex_48():
    np.random.seed(100)
    a = np.random.randint(0, 5, 10)
    print('Array: ', a)

    uniq_nums = np.unique(a).tolist()
    condition = []
    for num in a:
        if num in uniq_nums:
            condition.append(False)
            uniq_nums.remove(num)
        else:
            condition.append(True)

    print(condition)

# L3
def ex_30():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
    print(sepallength)

    exp_matrix = np.zeros(sepallength.shape)
    for i in range(sepallength.shape[0]):
        exp_matrix[i] = np.exp(sepallength[i])

    exp_matrix /= exp_matrix.sum()
    print(exp_matrix)


# L4
def ex_49():
    np.random.seed(100)
    arr = np.random.randint(1, 11, size=(6, 10))
    print(arr)

    nums_count = np.zeros((6, 10))
    for i in range(arr.shape[0]):
        unique, counts = np.unique(arr[i], return_counts=True)
        nums_count[i][unique - 1] = counts

    print(nums_count)


# L4
def ex_51():
    np.random.seed(101)
    arr = np.random.randint(1, 4, size=6)
    print(arr)

    result_arr = np.zeros((np.shape(arr)[0], np.max(arr)))
    for i in range(arr.shape[0]):
        result_arr[i][arr[i] - 1] = 1
    print(result_arr)


# L4 I copied solution because i didn't understand how to do it
def ex_70():
    window_length = 4
    strides = 2
    arr = np.arange(15)

    arr_strides = ((arr.size - window_length) // strides) + 1
    return np.array([arr[s:(s + window_length)] for s in np.arange(0, arr_strides * strides, strides)])


print(ex_70())
