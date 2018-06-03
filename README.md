# 15 Sorting Algorithms on 6 Different Arrays with 3 Different orders of magnitude data

I write some [sorting algorithms](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py) and visualize their [comparison](https://github.com/seanyuner/Sorting-Algorithm/blob/master/comparison_of_sorting_algos.ipynb).

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


## 目录
- [算法原理简述](https://github.com/seanyuner/Sorting-Algorithm/blob/master/README.md#算法原理简述)
- [算法性能比较](https://github.com/seanyuner/Sorting-Algorithm/blob/master/README.md#算法性能比较)
- [实际排序比较](https://github.com/seanyuner/Sorting-Algorithm/blob/master/README.md#实际排序比较)


## 算法原理简述
> 这里以目标序列为递增序列为例说明, 动图均源自wikipedia。
- [bubble sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L4-L15)，冒泡排序。可将数组视为左侧未排序和右侧已排序两部分（初始时全部为未排序），每轮遍历在未排序部分从左往右依次比较两相邻值大小，左边值大则交换位置，则每次遍历后，最大值会自然‘上浮’至未排序部分最右侧，下次遍历时将该值作为已排好序部分第一个元素，循环至未排序部分只剩一个元素则完成排序。可以在每轮遍历时设置一个flag，如果该轮没有发生元素交换，则说明数组已经排好序，可提前结束循环。
<p align='center'> 
<img src=Images/Bubble_sort_animation.gif> 
</p>

- [cocktail sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L18-L34)，鸡尾酒排序，又名搅拌排序、涟漪排序等。冒泡排序的一个改进版，可将数组看作三部分，左侧已排好序的小数部分，右侧已排好序的大数部分，中间为未排序部分，在每次遍历时不仅从左往右‘上浮’最大值，而且从右往左‘下沉’最小值。鸡尾酒排序可以解决冒泡排序中的[乌龟](https://www.wikiwand.com/en/Bubble_sort#/Rabbits_and_turtles)（数组尾部的小数值，这些数是造成冒泡排序缓慢的主因）。
<p align='center'>
<img src=Images/Sorting_shaker_sort_anim.gif>
</p>

- [comb sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L37-L53)，梳排序。也是冒泡排序的一个改良，和下述希尔排序的思想类似，即改变冒泡排序中每次都是比较相邻值的方法，比较距离从大到小（一般取1.3倍递减为优，程序中乘法比较快，约等于递增0.8倍）。其要旨在消除冒泡排序中的乌龟，兔子（前部的大数值）并不影响冒泡排序的性能。
<p align='center'>
<img src=Images/Comb_sort_demo.gif>
</p>

- [selection sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L53-L63)，选择排序。也可以将数组视为两部分，不过左侧为已排序部分，右侧为未排序部分，每次遍历在未排序部分通过比较找到最小值，然后将其和未排序第一个元素互换，下次遍历时将该值作为已排好序部分最后一个元素，循环至未排序部分只剩一个元素则完成排序。
<p align='center'>
<img src=Images/Selection_sort_animation.gif>
</p>

- [double selection_sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L69-L100)，双向选择排序。选择排序的改良版，类似于鸡尾酒排序对冒泡排序的改良，数组左右部分分别为已排好序的小数和大数，中间为未排序部分，每次遍历时不仅找到未排序部分最小数的index，也寻找其最大值的index，然后将二者分别和未排序部分的首位和末尾交换（这部分存在最小/大值刚好在未排序部分首/末位的特殊情况，需要分类小心讨论）。


- [insertion sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L103-L113)，插入排序。将数组视为两部分，左侧排好序，右侧未排序（初始时将数组第一个元素视为已排序），每次循环时选取未排序部分第一个元素，然后对已排序部分从右往左扫描，找到大小合适的位置后将所选元素放置。实现时一般采用只占用O(1)空间的方法，在从后往前扫描过程中，需要反复把已排序元素向后挪位，为新元素留出空间。
<p align='center'>
<img src=Images/Insertion_sort_animation.gif>
</p>

- [shell sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L116-L129)，希尔排序，又名缩小增量排序。插入排序的改良版，主要解决其每次移动时只能移动一位的低效性。希尔排序通过将数组分为若干个区域来加速排序，每个区域内数的index差即gap值（‘增量’之意）是相同的，先选取较大的gap，可以让元素以较大的步伐移向正确位置附近，逐步递减，至gap为1时就是移位不大于一的插入排序了。
<p align='center'>
<img src=Images/Sorting_shellsort_anim.gif>
</p>

- [gnome sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L132-L142)，地精排序。想法和实现应该是这里面最简单的，只需要一个循环，数组从左往右遍历，依次比较相邻值，遇到逆序（此处即是右边大于左边）则将右侧值往前一直交换至合适位置，其中不断往前寻找合适位置类似插入排序，但是不是通过移位，而是采用交换的方式，这又类似冒泡排序。一个可选的优化方法是：在遇到逆序时将当前index存储，找到合适位置后直接返回至该index然后继续往后寻找逆序，如下方动图所示。
<p align='center'>
<img src=Images/Sorting_gnomesort_anim.gif>
</p>

- [merge sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L145-L167)，归并排序。[分治法](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm)的典型应用，1945年由冯·诺伊曼首次提出。将数组不断分解至1/2个相邻元素，然后对其进行排序，再将相邻的两组1/2个元素的小组进行合并，不断合并左右部分直至所有元素排序完毕。
<p align='center'>
<img src=Images/Merge_sort_animation2.gif>
</p>

- [quick sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L170-L197)，快速排序。首先在数组中选出一个元素作为pivot，遍历数组使小于该值的元素放在其左侧，大于该值的元素放在其右侧（相等的元素左右均可），递归地对左右部分进行排序。其每一次迭代至少会将一个元素放在其正确的位置，也因此必然会结束迭代。
<p align='center'>
<img src=Images/Sorting_quicksort_anim.gif>
</p>

- [heap sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L200-L-248)，堆排序。利用[堆](https://en.wikipedia.org/wiki/Heap_(data_structure))这种数据结构所设计的一种排序算法，可以看作是选择排序的一种：将数组分为未排序和已排序两部分，然后在未排序部分寻找最大值，下次循环将其列入已排序部分。首先自下而上（从最后一个有孩子节点到根节点）建立大顶堆，然后迭代将堆顶（最大值）和堆的末位进行交换（同时将其视为已排序部分，不再算在堆内），自上而下调整堆（实质上第一步中对每一个节点也存在自上而下调整堆）。
<p align='center'>
<img src=Images/Sorting_heapsort_anim.gif>
</p>

- [counting sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L251-L269)，计数排序。计数排序不是基于比较的排序，是一种稳定的线性时间排序算法。其需要一个额外的数组来记录待排数组中从最小值至最大值间每个数字出现的次数，以空间来换取时间，最后遍历记录数组将待排数组元素排入相应位置。当整数的范围特别大的时候，空间占用太大，效率会降低。


- [bucket sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L272-L285)，桶排序。现申请一定数量的桶（数组），然后按照预设的映射函数，遍历待排数组将每个元素分配到相应的桶中，再对每个桶中的元素进行排序（快速排序、插入排序等），最后将各桶中的元素按序组合即可。其和下方的基数排序有一些类似。若要达到较高的效率，映射函数需要保证每个桶中的元素个数尽量相等。
<p align='center'>
<img src=Images/Bucket_sort_1.svg.png>
</p>
<p align='center'>
<img src=Images/Bucket_sort_2.svg.png>
</p>

- [radix sort](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sort.py#L288-L295)，基数排序。和桶排序同属于分布式排序，其历史可以追溯到1887年Herman Hollerith在打孔卡片制表机(Tabulation Machine)上的贡献。比如对于常见的十进制数据，其先遍历数组，按照个位数将每个元素分配到0-9十个桶中，然后将各桶中的元素按序组合，再遍历组合后的数组，按照十位数将每个元素分配到0-9十个桶中，然后将各桶中的元素按序组合...，到最高位后即完成排序。上述方法是最低位优先法（LSD, least significant digit），也可以从最高为开始：最高位优先法（MSD, most significant digit）。

- sorted (python3 build in Timsort)。Timsort是Tim Peters于2012年设计的排序算法，其源自归并排序和插入排序，python自2.3版本以来一直使用该算法作为其标准排序算法。该算法排序单位不是单个元素，而是数组中已排好序的子序列，称为run，先找到这些run，再按规则merge这些run并保存到栈中，直至成为一个run即完成排序，具体算法可参见[Timsort wikipedia](https://en.wikipedia.org/wiki/Timsort).
<p align='center'>
<img src=Images/560px-Selection_of_minrun_by_timsort.png height=150>
<img src=Images/Representation_of_stack_for_merge_memory_in_Timsort.svg.png height=150>
</p>


## 算法性能比较
> log: 2为底; n: 数组元素个数; p: 增量个数; k: 桶数目（基数排序中就是数字位数）

|  algotirhms  |average performance| best performance | worst performance | space complexity | in place? | stable?  |comparison based? |
| :----------: | :---------------: | :--------------: | :---------------: | :--------------: | :--------:| :------: | :--------------: |
|  bubble sort | O(n^2) | O(n) | O(n^2) | O(1) |  in place | stable | comparison |
| cocktail sort| O(n^2) | O(n) | O(n^2) | O(1) |  in place | stable | comparison |
|   comb sort  | O(n^2/(2^p)) | O(nlogn) | O(n^2) | O(1) | in place | unstable | comparison |
| selection sort | O(n^2) | O(n^2) | O(n^2) | O(1) | in place | unstable | comparison |
| doubleselection sort | O(n^2) | O(n^2) | O(n^2) | O(1) | in place | unstable | comparison |
| insertion sort | O(n^2) | O(n) | O(n^2) | O(1) | in place | stable | comparison |
| shell sort |depends on gap sequence | O(nlogn) |  O(n(logn)^2) | O(1) |  in place | unstable | comparison |
| gnome sort | O(n^2) | O(n) | O(n^2) | O(1) |  in place |  stable  | comparison |
| merge sort | O(nlogn) | O(nlogn) | O(nlogn) | O(n) | out place | stable | comparison |
| quick sort | O(nlogn) | O(nlogn) | O(n^2) | O(logn) | in place | unstable | comparison |
| heap sort | O(nlogn) | O(n) | O(nlogn) | O(1) | in place | unstable | comparison |
| counting sort | O(n+k) | O(n+k) | O(n+k) | O(k) | out place | stable  | no comparison  |
| bucket sort | O(n+k) | O(n+k) | O(n^2) | O(n+k) | out place | unstable | no comparison  |
| radix sort | O(n\*k) |  O(n\*k) | O(n\*k) | O(n+k) | out place | stable | no comparison |
| tim sort | O(nlogn) | O(n) | O(nlogn) | O(n) | out place | stable | comparison |


## 实际排序比较
如前所述，这里对比了一共15种排序算法，6种不同序列类型（随机、正序、几乎正序、逆序、密集、稀疏）（一直没有想好用什么词语定义这六种，以下暂以“序列类型”代指这六种分布），3种数量级（100、1000、10000）元素，每一次排序均运行5次取平均结果，即一共运行了15\*6\*3\*5=1350次排序；

在这里，参与排序的元素均取为从0开始的非负整数，默认最大值M等于参与排序元素数量N，“几乎正序”序列中乱序比例alpha为0.02，“密集”序列中最大值缩减系数beta为0.1，“稀疏”序列中最大值放大系数gamma为10，这些参数在程序中均可以直接调节；

算法运行在MSI笔记本上（GL62VR 7RFX-1017CN，WIN10系统，i5-7300HQ，2.5GHz）。

### 1. N=100
<p align='center'>
<img src=Images/100_elements.png>
</p>
由上图可以观察到：

1. 算法对比而言，鸡尾酒排序、双向选择排序最慢，其次是希尔排序、基数排序、堆排序、选择排序和冒泡排序，其余的耗时均可忽略（数值上=0，下同）；
2. 在序列类型上，稀疏最慢，其次是逆序、密集，再次是随机，其余的耗时均可忽略；
3. 值得注意的是，每次出现耗时>0的排序，耗时几乎一致（实际上都在3.120ms - 3.131ms之间）;
4. 另外，由于参与排序元素的个数较少，可能存在的偶然性比较大，这一组数据仅供参考。
  
 ### 2. N=1000
<p align='center'>
<img src=Images/1000_elements_bar.png>
</p>
由上图可以观察到：

1. 算法对比而言，地精排序、冒泡排序、鸡尾酒排序、选择排序、插入排序、双向选择排序都在100ms以上，其余在100ms以下；
2. 计数排序表现最优，在六种序列类型上均可忽略，参考[表格](https://github.com/seanyuner/Sorting-Algorithm/blob/master/sa_times_1000.csv)，归并排序、桶排序、梳排序、sorted排序、基数排序、希尔排序耗时累计都在10ms以下，快排在15ms左右，堆排序在50ms左右。

<p align='center'>
<img src=Images/1000_6_line.png>
</p>
<p align='center'>
<img src=Images/1000_6_bar.png>
</p>
<p align='center'>
<img src=Images/1000_6_bar2.png>
</p>
由上图可以看出：

1. 在序列类型上，总体而言，逆序是最慢的；正序和几乎正序最快且相差无几；剩下的随机、密集、稀疏居中，之间也相差无几；
2. 不同算法对序列类型有着不同的“敏感程度”，比如地精排序、鸡尾酒排序在正序和几乎正序的序列上表现和众多算法相差无几，但是在逆序时表现非常大，对于二者而言，这也是它们表现最差的情形；但是计数排序等累计耗时小于10ms的算法，对类型均并不太敏感；
3. 其中也存在其他有意思的点，比如一般算法逆序表现都会比几乎正序要差，但是双向选择排序却相反，这是由于...
  
### 3. N=10000
<p align='center'>
<img src=Images/10000_elements.png>
</p>
由上图可以看出：

1. 算法对比上，和1000元素的排序基本一致，地精排序、冒泡排序、鸡尾酒排序、插入排序、选择排序、双向选择排序最慢，在一个数量级，均在10000ms以上，其余排序时间均在500以下，其中100ms以下有三种，依次为：sorted排序（约16.3ms）、计数排序（约56.1ms）、基数排序（约94.7ms）；
2. python自带sorted排序的强大由此可见，10000个元素的五种排序时间和也仅仅只有16.3ms，并且其对于随机、正序、几乎正序三种序列类型耗时均可忽略，在逆序序列也仅耗时0.68ms，在稀疏序列耗时为10.41ms，基本为密集序列耗时5.22ms的两倍。

<p align='center'>
<img src=Images/10000_6_line.png>
<img src=Images/10000_6_pie.png>
<img src=Images/10000_6_pie2.png>
</p>
由上图可以看出：

1. 和1000元素情形基本相同，序列类型上，逆序最慢，随机、密集、稀疏其次，正序和几乎正序最快；
2. 相比于1000元素而言，由于数据量增大，我们对于各种算法在不同序列类型上的表现可以有更令人信服的比较，具体而言，如扇形图所示：选择排序、双向选择排序、基数排序对序列类型“敏感程度”最低，几乎完全一致，梳排序、希尔排序、归并排序、堆排序次之，冒泡排序、快速排序、桶排序再次之，鸡尾酒排序、插入排序、地精排序、计数排序、sorted排序对数据最“敏感”。（此处sorted排序、计数排序等由于耗时较短，其“敏感”程度结论只是基于以有数据得出，理论上应该进行对其更多元素的排序实验）

### 4. overall
<p align='center'>
<img src=Images/overall.png>
</p>
这正是本页最上面的一张图，每个数据点是六种排序的时间和，反映了15种排序算法分别在三种数量级下的综合表现对比。可以看到：

1. 地精排序、冒泡排序、鸡尾酒排序、插入排序、选择排序、双向选择排序最慢，10000元素耗时均在10000ms以上，1000元素耗时均在100ms以上，其次是快速排序、归并排序、希尔排序、堆排序、梳排序、桶排序，10000元素耗时在100ms - 500ms之间，sorted排序、计数排序、基数排序是最快的三种排序;
2. 由于三种数据量级是相邻的数量级，图片纵轴也是数量级，因此比较不同算法在纵向三个值之间的两个差值变化，可以将其作为算法对数量级的“敏感程度”的一个参考。比如，可以看到归并排序对数量级非常“敏感”，随着数量级的增大，耗时急剧增大，而冒泡排序、鸡尾酒排序、选择排序等则“敏感”程度较低，另外，对于堆排序、快速排序等，虽然对数量级也较为“敏感”，但其趋势是随着数量级的增大，耗时相对来说有所减少。
3. 更多详细的对比图表参见[ipynb文件](https://github.com/seanyuner/Sorting-Algorithm/blob/master/comparison_of_sorting_algos.ipynb)
