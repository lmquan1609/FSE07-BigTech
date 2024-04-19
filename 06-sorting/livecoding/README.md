# Sorting - Live Coding Solutions

Lecturer: Truong Quy Quynh

## 1. Selection sort
Link problem: lecture slides
```java
class Solution {
    public static void selectionSort(int[] nums) {
        int n = nums.length;
        int currentIndex = 0;
        while(currentIndex < n) {
            int minIndex = currentIndex;
            for(int i = minIndex + 1; i < n; i++) {
                if (nums[i] < nums[minIndex]) {
                    minIndex = i;
                }
            }
            swap(nums, currentIndex, minIndex);
            currentIndex++;
        }
    }

    public static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

```
Complexity:

- Time: `O(N^2)` where `N` is length of the array
- Space: `O(1)`

## 2. Pankae sorting

Link problem: https://leetcode.com/problems/pancake-sorting/

```java
class Solution {
    public List<Integer> pancakeSort(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>();
        int count = n - 1;
        while(count >= 0) {
            int maxIndex = count;
            for(int i = maxIndex - 1; i >= 0; i--) {
                if (nums[i] > nums[maxIndex]) {
                    maxIndex = i;
                }
            }
            //buoc 1: move phan tu maxIndex ve dau tien bang viec flip   
            result.add(maxIndex + 1);
            flip(nums, maxIndex + 1);
            //buoc 2: flip 1 lan nua de move phan tu maxIndex ve dung vi tri
            result.add(count + 1);
            flip(nums, count + 1);
            count--;
        }
        return result;
    }

    public void flip(int[] nums, int k) {
        int left = 0, right = k - 1;
        while(left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

Complexity:

- Time: `O(N^2)` where `N` is length of the array
- Space: `O(1)`


## 3.   Merge Sorted Array

Link problem: https://leetcode.com/problems/merge-sorted-array/

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] result = new int[m + n];
        int i = 0, j = 0, count = 0;
        while(i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                result[count++] = nums1[i++];
            } else {
                result[count++] = nums2[j++];
            }
        }
        //day 1 con thua phan tu
        while(i < m) {
            result[count++] = nums1[i++];
        }
        //day 2 con thua phan tu
        while(j < n) {
            result[count++] = nums2[j++];
        }
        System.arraycopy(result, 0, nums1, 0, result.length);
    }
}

```

Complexity:

- Time: `O(M + N)` where `M` is the  length of `nums1`,  `N` is the length of `nums2`
- Space: `O(N)`



## 4.    Sort an Array

Link problem: https://leetcode.com/problems/sort-an-array/

**Solution: using merge sort**

```java

class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, nums.length);
        return nums;
    }

    //sort day nums co do dai n
    public void mergeSort(int[] nums, int n) {
        if (n == 1) {
            return;
        }
        //chia day ra lam 2 day
        int mid = n / 2;
        //clone day ben trai
        int[] left = new int[mid];
        for(int i = 0; i < mid; i++) {
            left[i] = nums[i];
        }
        //clone day ben phai
        int[] right = new int[n - mid];
        for(int i = 0; i < n - mid; i++) {
            right[i] = nums[i + mid];
        }
        mergeSort(left, mid);
        mergeSort(right, n - mid);        
        merge(left, mid, right, n - mid, nums);
    }

    /*  
        merge day left va right (2 day da duoc sort) vao day nums
    */
    public void merge(int[] left, int m, int[] right, int n, int[] nums) {
        int i = 0, j = 0, count = 0;
        while(i < m && j < n) {
            if (left[i] < right[j]) {
                nums[count++] = left[i++];
            } else {
                nums[count++] = right[j++];
            }
        }
        while(i < m) {
            nums[count++] = left[i++];
        }
        while(j < n) {
            nums[count++] = right[j++];
        }
    }
}
```

Complexity:
- Time: `O(N*LogN)` where `N` is length of the array.
- Space: `O(N*LogN)`

**Solution: using quick sort**

```java
class Solution {
    Random rand = new Random();

    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    //sort sub-array tu nums[start]...nums[end]
    public void quickSort(int[] nums, int start, int end) {
        if (start >= end) {
            return;
        }
        //buoc 1: chon so x
        int randomPos = rand.nextInt(end - start + 1) + start;
        swap(nums, randomPos, end);
        int x = nums[end];
        //buoc 2: nem tat ca cac phan tu nho hon x sang ben trai
        int count = start;
        for(int i = count; i < end; i++) {
            if (nums[i] < x) {
                swap(nums, count, i);
                count++;
            }
        }
        //nem x ve dung vi tri
        swap(nums, count, end);
        quickSort(nums, start, count - 1);
        quickSort(nums, count+ 1, end);
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```
Complexity:
- Time: `O(N*LogN)` where `N` is length of the array (on average).
- Space: `O(1)`

## 5.    Sort Colors

Problem link: https://leetcode.com/problems/sort-colors/

**Solution: quick sort-like solution**

```java
class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        //nem cac phan tu 0 sang ben trai
        int count = 0;
        for(int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                swap(nums, count, i);
                count++;
            }
        }
        //nem cac phan tu 2 sang ben phai
        count = n - 1;
        for(int i = n-1; i >= 0; i--) {
            if (nums[i] == 2) {
                swap(nums, count, i);
                count--;
            }
        }        
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

Complexity:

- Time: `O(N)` where `N` is length of the array.
- Space: `O(1)`
