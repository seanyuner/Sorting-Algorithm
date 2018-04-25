# 冒泡排序 
def bubble_sort(array):   
    count = len(array)
    for i in range(count - 1):
        flag = True  # 如果本次循环没有交换，说明已经排好
        for j in range(count - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            return array
    return array


# 鸡尾酒排序 (略微改进版冒泡排序，每次同时找最大和最小值)
def cocktail_sort(array):
    count = len(array)
    flag = True  # 如果本次循环没有交换，说明已经排好
    i = 0
    while flag and i < count // 2:
        flag = False
        for j in range(i, count - 1 - i):  # 正向找最大值
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        for k in range(count - 2 - i, i, -1):  # 反向找最小值
            if array[k] < array[k - 1]:
                array[k], array[k - 1] = array[k - 1], array[k]
                flag = True
        i += 1
    return array


# 梳排序 （改良的冒泡算法，分组冒泡，又类似shell排序）
def comb_sort(array):
    count = len(array)
    RATE = 1.3
    flag = True
    gap = count
    while True:
        flag = False
        gap = int(gap / RATE) if gap > 1 else gap
        for i in range(count - gap):
            des = i + gap
            if array[des] < array[i]:
                array[i], array[des] = array[des], array[i]
                flag = True
        if flag == False and gap == 1:  # 当且仅当gap为1且没有交换时排好序
            break
    return array


# 选择排序
def selection_sort(array):
    count = len(array)  
    for i in range(count - 1):
        min_index = i  # 选择后面最小的元素进行交换
        for j in range(i + 1, count):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


# 双向选择排序          
def double_selection_sort(array):
    count = len(array)  
    for i in range(count // 2 + 1):
        min_index = i  # 选择后面最小的元素进行交换
        max_index = count - 1 - i  # 选择前面最大的元素进行交换
        for j in range(i, count - i):
            if array[min_index] > array[j]:
                min_index = j
                continue
            if array[max_index] < array[j]:
                max_index = j
        # 特殊情况1：i为最大位置，count-1-i为最小位置
        if max_index == i and min_index == count - 1 - i:
            array[min_index], array[max_index] = \
                              array[max_index], array[min_index]
        # 特殊情况2：i为最大位置，但count-1-i不是最小位置，需先交换最大位置
        elif max_index == i and min_index != count -1 - i:
            array[count - 1 - i], array[max_index] = \
                        array[max_index], array[count - 1 - i]
            array[i], array[min_index] = array[min_index], array[i]
        # 特殊情况2：count-1-i为最小位置，但i不是最小位置，需先交换最小位置
        #elif max_index != i and min_index == count - 1 - i:
         #   array[i], array[min_index] = array[min_index], array[i]
          #  array[count - 1 - i], array[max_index] = \
           #             array[max_index], array[count - 1 - i]
        # 普通情况：i, count-1-i均不是最值位置，交换次序不限，此时也可随便合并到2/3
        else:
            array[i], array[min_index] = array[min_index], array[i]
            array[count - 1 - i], array[max_index] = \
                        array[max_index], array[count - 1 - i]
    return array


# 插入排序
def insertion_sort(array):
    count = len(array)
    for i in range(1, count):  # 列表左侧已排好序，右侧逐个插入左侧合适处， 扑克牌
        pre_index = i - 1
        current = array[i]
        while pre_index >= 0 and array[pre_index] > current:
            array[pre_index + 1] = array[pre_index]
            pre_index -= 1
        array[pre_index + 1] = current
    return array


# 希尔排序（缩小增量排序Diminishing Increment Sort）
def shell_sort(array):
    count = len(array)
    gap = count // 2  # 初始化增量
    while gap:
        for i in range(gap, count):
            pre_index = i - gap  # 间隔相同的组内进行插入排序
            current = array[i]
            while pre_index >= 0 and array[pre_index] > current:
                array[pre_index + gap] = array[pre_index]
                pre_index -= gap
            array[pre_index + gap] = current
        gap = gap // 2  # 递减增量至1即完成排序
    return array


# 地精排序
def gnome_sort(array):
    count = len(array)
    i = 0
    while i < count:
        if i == 0 or array[i - 1] <= array[i]:  #等于0或者正序则递增寻找后面逆序
            i += 1
        else:  # 找到逆序后交换，并继续比较前面已排好元素 
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    return array


# 归并排序
def merge_sort(array):
    count = len(array)
    if count <= 1:  # 递归终止条件：长度小于2后停止
        return array
    middle = count // 2  # 否则递归分左右
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    
    return merge(left, right)  # 合并左右
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 快速排序1
quick_sort1 = lambda array: array if len(array) <= 1 else \
              quick_sort1([item for item in array[1:] if item <= array[0]]) + \
              [array[0]] + \
              quick_sort1([item for item in array[1:] if item > array[0]])

# 快速排序2
def quick_sort2(array):
    if len(array) <= 1:   # 递归终止条件：长度小于2后停止
        return array
    pivot = array[0]
    return quick_sort2([x for x in array[1:] if x < pivot]) + \
           [pivot] + \
           quick_sort2([x for x in array[1:] if x >= pivot])

# 快速排序3
def quick_sort3(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = []  # 将小于和大于pivot的元素分别记录
    right = []
    for n in array[1:]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    return quick_sort3(left) + [pivot] + quick_sort3(right)


# 堆排序1  （循环版）
def heap_sort1(array):
    count = len(array)
    for start in range(count // 2 - 1, -1, -1):  # 构建大顶堆，从下往上（最后一个有孩子节点到0）
        shift_down(array, start, count - 1)
    for end in range(count - 1, 0, -1):  # 每次取最大值置尾，调整堆，从上往下
        array[0], array[end] = array[end], array[0]
        shift_down(array, 0, end - 1)
    return array
def shift_down(array, start, end):
    root = start  # 对每个节点而言，
    while True:
        child = 2 * root + 1 # 左子节点
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:  # 寻找最大孩子节点
            child += 1
        if array[root] < array[child]:  # 交换最大孩子节点和父节点
            array[root], array[child] = array[child], array[root]
            root = child  # 循环
        else:  # 若父节点不小于左右子节点，则退出循环
            break

# 堆排序2  （递归版）
def heap_sort2(array):
    global count
    count = len(array)
    for i in range(count // 2 - 1, -1, -1):
        heapify(array, i)
    for i in range(count - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        count -= 1
        heapify(array, 0)
    return array
def heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < count and array[left] > array[largest]:
        largest = left
    if right < count and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest)


# 计数排序
def counting_sort(array):
    min_ = 2**31  # 寻找列表的最大值和最小值
    max_ = 0
    for i in array:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
    length = max_ - min_ + 1
    counts = [0] * length  # 构建列表，依次存储最值间所有数值出现次数
    for i in array:
        counts[i - min_] += 1
    index = 0  # 按照计数重新排列
    for n in range(length):
        for i in range(counts[n]):
            array[index] = n + min_
            index += 1
    return array


# 桶排序
import math
def bucket_sort(array):
    count = len(array)
    min_ = min(array)
    max_ = max(array)
    num_buckets = int(count ** 0.5)
    buckets = [[] for i in range(num_buckets)]
    step = (max_ - min_) // num_buckets + 1
    # step = math.ceil((max_ - min_) / num_buckets)
    # max_ += 1
    for i in array:
        buckets[(i - min_) // step].append(i)
    array = []
    for bucket in buckets:
        array.extend(quick_sort2(bucket))
    return array
    

# 基数排序
def radix_sort(array):
    for k in range(len(str(max(array)))):  # 从低位到高位依次遍历
        s = [[] for i in range(10)]  # 十进制：十种数字0-9
        for i in array:
            s[i // (10 ** k) % 10].append(i)
        array = [j for i in s for j in i]
    return array


import random
from time import time


def run_sort(sort, array):
    # print('original array: ', array)
    start = time()
    array_sorted = sort(array)
    run_time = time() - start
    # print('sorted array: ', array_sorted)
    print('{:>25} running time: {:>7.4f}s.'.format(sort.__name__, run_time))
    
    for i in range(len(array_sorted) - 1):  # 核查排序是否正确
        if array_sorted[i] > array_sorted[i + 1]:
            print('sorry, %s failed at index: %d.' % (sort.__name__, i))

    return run_time


def gene_data(n, m, alp, bet, gam):
    random_array = []                                  # 随机
    for i in range(n):
        random_array.append(random.randint(0, m))
        
    asc_array = sorted(random_array)                   # 正序
    
    alm_asc_array = asc_array                          # 几乎正序
    for i in range(int(m * alp)):
        p = random.randint(0, n-1)
        q = random.randint(0, n-1)
        alm_asc_array[p], alm_asc_array[q] = alm_asc_array[q], alm_asc_array[p]

    desc_array = asc_array[::-1]                       # 逆序
        
    dense_array = []                                   # 密集
    for i in range(n):
        dense_array.append(random.randint(0, m * bet))

    sparse_array = []                                  # 稀疏
    for i in range(n):
        sparse_array.append(random.randint(0, m * gam))

    array_names = ['random_array', 'asc_array', 'alm_asc_array', \
              'desc_array', 'dense_array', 'sparse_array']
    arrays = [random_array, asc_array, alm_asc_array, \
              desc_array, dense_array, sparse_array]
    
    return array_names, arrays


if __name__=="__main__":
    # import resource, sys
    # resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
    # sys.setrecursionlimit(10**6)
    
    N = 10000       # 参与排序元素个数
    M = N          # 参与排序元素最大值（默认等于N，最小值默认为0）
    alpha = 0.02   # 几乎正序数组乱序比例
    beta = 0.1     # 密集数组最大值缩减系数
    gamma = 10     # 稀疏数组最大值放大系数
    T = 5          # T次求平均
    A = 6          # array种类数

    sorting_algorithms = [bubble_sort, cocktail_sort, comb_sort, \
                          selection_sort, double_selection_sort, \
                          insertion_sort, shell_sort, gnome_sort, \
                          merge_sort, quick_sort2, heap_sort1, \
                          counting_sort, bucket_sort, radix_sort, \
                          sorted]
    
    times = [[[] for i in range(A)] for j in range(T)]
    
    for j in range(T):
        print("Running time %d......." % (j+1))
        arr_names, arrs = gene_data(N, M, alpha, beta, gamma)
        for i in range(A):
            print('On %s.' % arr_names[i])
            for sa in sorting_algorithms:
                times[j][i].append(run_sort(sa, arrs[i].copy()))
            print('\n')
        print('\n\n\n')
        
    times_avg = [[] for i in range(A)]
    for i in range(len(sorting_algorithms)):
        for j in range(A):
            time = 0
            for k in range(T):
                time += times[k][j][i]
            times_avg[j].append(time / T * 1000)   # ms
            # times_avg[j].append(time / T * 1000 if N <=1000 else time / T)

    s = 'sorting_algos'
    for arr_name in arr_names:
        s += ',' + arr_name
    s += '\n'

    for i in range(len(sorting_algorithms)):
        s += sorting_algorithms[i].__name__
        for j in range(A):
            s += ', %.6f' % times_avg[j][i]
        s += '\n'

    with open('sa_times_%d.csv' % N, 'w') as f:
        f.write(s)
