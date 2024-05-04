# LeetCode 1. Two Sum
*****

## 題目 :book:
題目給一個**整數**的list`nums`和一個**整數**`target`，找出list中哪兩個元素相加後，會等於`target`，回傳這兩個元素的索引位置  
> 這個問題假設每個輸入都會有一個**唯一**的解，且不允許重複使用同一個元素  

[完整題目](https://leetcode.com/problems/two-sum/description/)

## 解題想法 :bulb:
- **想法一 :**  
  使用兩個for迴圈，第一輪從第一個元素往後加，去判斷相加的結果是否為`target`，第二輪從第二個元素往後加，去判斷相加的結果是否為`target`，依此類推...
- **想法二 :**  
  先建立一個空的**hash_table**(即一個dictionary或list)，利用一個for迴圈去讀取`nums`中的元素，**將`target` - 目前的元素的值**後，判斷是否有在hash table中，若沒有的話，則把目前元素的值和索引位置存入hash_table中，若有的話，代表之前出現過可以跟目前元素的值相加後為`target`的數值，故回傳這兩個元素的索引位置
  > 例如 : nums = [2,7,11,15], target = 9   
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一輪(i=0)，因為`target` - 目前元素的值 = 9 - 2 = 7 不在hash_table中，因此將2與它的索引位置(0)存入hash_table中  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第二輪(i=1)，因為`target` - 目前元素的值 = 9 - 7 = 2 在hash_table中，因此回傳這兩個元素的索引位置(0和1)

## 範例 :mag:
- **範例1 :**  
  **輸入 :** nums = [2,7,11,15], target = 9  
  **輸出 :** [0,1]  
  **說明 :** 因為 nums[0] + nums[1] == 9, 所以回傳[0,1]

- **範例2 :**  
  **輸入 :** nums = [3,2,4], target = 6
  **輸出 :** [1,2]  
  **說明 :** 因為 nums[1] + nums[2] == 6, 所以回傳[1,2]

- **範例3 :**  
  **輸入 :** nums = [3,3], target = 6
  **輸出 :** [0,1]  
  **說明 :** 因為 nums[0] + nums[1] == 6, 所以回傳[0,1]
