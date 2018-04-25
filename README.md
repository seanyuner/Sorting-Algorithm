# 15 Sorting Algorithms on 6 Different Arrays with 3 Different orders of magnitude data

I write some [sorting algorithms](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py) and visualize their [comparison](https://github.com/seanyuner/Sorting-Algorithm/blob/master/comparison_sorting_algos.ipynb).

Since [hustcc](https://github.com/hustcc) had a great [explanation and sorting progress visualation](https://github.com/hustcc/JS-Sorting-Algorithm) of the main algorithms, I will focus on their comparison.

![overall](https://github.com/seanyuner/Sorting-Algorithm/blob/master/Images/overall.png)

**15 sorting algorithms:**
- bubble sort
- cocktail sort
- comb sort
- selection sort
- double selection_sort
- insertion sort
- shell sort
- gnome sort
- merge sort
- quick sort
- heap sort
- counting sort
- bucket sort
- radix sort
- sorted (python3 build in timsort)

**6 different arrays:**
- random array
- ascending array (asc_array)
- almost ascending array (alm_asc_array)
- descending array (desc_array)
- dense array
- sparse array

**3 different orders of magnitude data:**
- 100
- 1000
- 10000
---

## 算法简单阐述
> 这里以目标序列为递增序列为例说明, 动图均源自wikipedia。
- [bubble sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L1-L12)，冒泡排序。可将数组视为左侧未排序和右侧已排序两部分（刚开始时全部为未排序），每轮遍历在未排序部分从左往右依次比较两相邻值大小，左边值大则交换位置，则每次遍历后，最大值会自然‘上浮’至未排序部分最右侧，下次遍历时将该值作为已排好序部分第一个元素，循环至未排序部分只剩一个元素则完成排序。可以在每轮遍历时设置一个flag，如果该轮没有发生元素交换，则说明数组已经排好序，可提前结束循环。
<p align='center'> <img src=Images/Bubble_sort_animation.gif> </p>

- [cocktail sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L15-L31)，鸡尾酒排序，又叫搅拌排序、涟漪排序等。冒泡排序的一个改进版，可将数组看作三部分，左侧已排好序的小数部分，右侧已排好序的大数部分，中间为未排序部分，在每次遍历时不仅从左往右‘上浮’最大值，而且从右往左‘下沉’最小值。
<p align='center'>
<img src=Images/Sorting_shaker_sort_anim.gif>
</p>
- [comb sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L34-L50)，梳排序。也是冒泡排序的一个改良，和下述希尔排序的思想类似，即改变冒泡排序中每次都是比较相邻值的方法，比较距离从大到小（一般取1.3倍递减率为优，程序中乘法比较快，约等于递增0.8倍）。其旨在消除冒泡排序中的[乌龟](https://www.wikiwand.com/en/Bubble_sort#/Rabbits_and_turtles)（数组尾部的小数值,这些数是造成冒泡排序缓慢的主因）。
<p align='center'>
<img src=Images/Comb_sort_demo.gif>
</p>
- [selection sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L53-L63)

- [double selection_sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L66-L97)

- [insertion sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L100-L111)

- [shell sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L114-L127)

- [gnome sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L130-L140)

- [merge sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L143-L164)

- [quick sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L167-L194)

- [heap sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L197-L-241)

- [counting sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L244-L262)

- [bucket sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L265-L281)

- [radix sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L284-L292)

- sorted (python3 build in [timsort](https://en.wikipedia.org/wiki/Timsort))

