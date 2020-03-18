# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import sys


def select_sort(a):
    # 选择排序
    # 每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    # 顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    # 选择排序是不稳定的排序方法。

    a_len = len(a)
    for i in range(a_len):  # 在0-n-1上依次选择相应大小的元素
        min_index = i  # 记录最小元素的下标
        for j in range(i + 1, a_len):  # 查找最小值
            if (a[j] < a[min_index]):
                min_index = j
        if min_index != i:  # 找到最小元素进行交换
            a[i], a[min_index] = a[min_index], a[i]



def shell_sort(a):
    # shell排序

    a_len=len(a)
    gap=a_len/2 # 增量
    while gap>0:
        for i in range(a_len): # 对同一个组进行选择排序
            m=i
            j=i+1
            while j<a_len:
                if a[j]<a[m]:
                    m=j
                j+= gap # j增加gap
            if m!=i:
                a[m], a[i] = a[i], a[m]
        gap/=2


def partition1(A, p, r):

    # 方法一，两个指针索引一前一后逐步向后扫描的方法

    x = A[r]
    i = p - 1
    j = p
    while j < r:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def partition2(A, p, r):

    # 两个指针从首尾向中间扫描的方法

    i = p
    j = r
    x = A[p]
    while i == x and i < j:
        j -= 1
    A[i] = A[j]
    while A[i] <= x and i < j:
        i += 1
    A[j] = A[i]
    A[i] = x
    return i

# quick sort
def quick_sort(A, p, r):

    # 快速排序的最差时间复杂度为O(n2)，平时时间复杂度为O(nlgn)

    if p < r:
        q = partition2(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def merge(nums, first, middle, last):
    # 切片边界,左闭右开并且是了0为开始
    lnums = nums[first:middle+1]
    rnums = nums[middle+1:last+1]
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
    l = 0
    r = 0
    for i in range(first, last+1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l+=1
        else:
            nums[i] = rnums[r]
            r+=1
def merge_sort(nums, first, last):
    ''''' merge sort
    merge_sort函数中传递的是下标，不是元素个数
    '''
    if first < last:
        middle = (first + last)/2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle+1, last)
        merge(nums, first, middle,last)


def insert_sort(a):
    ''' 插入排序
    有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，
    但要求插入后此数据序列仍然有序。刚开始 一个元素显然有序，然后插入一
    个元素到适当位置，然后再插入第三个元素，依次类推
    '''
    a_len = len(a)
    for i in range(a_len):
        key = a[i]
        j = i - 1
        while a_len == 0 and a[j] > key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
    return a


if __name__ == '__main__':
    A = [10, -3, 5, 17, 1, 3, 7]
    print 'Before sort:', A
    select_sort(A)
    print 'After select_sort:', A
    shell_sort(A)
    print 'After shell_sort:', A
    merge_sort(A, 0, 6)
    print 'merge sort:', A
    insert_sort(A)
    print 'insert_sort:', A

