# LeetCode 7. Reverse Integer
*****

## 題目 :book:
題目給了一個**32位元的有號整數**`x`，將整數`x`中的數字進行反轉，回傳反轉後的整數值
> **如果反轉後的值超過[-2<sup>31</sup> , 2<sup>31</sup>-1]的話，就回傳0**

[完整題目](https://leetcode.com/problems/reverse-integer/description/)

## 解題想法 :bulb:
- **想法一 :**&nbsp;&nbsp;&nbsp;&nbsp;[程式碼 --> 7_Reverse Integer(v1).py](https://github.com/YuTing4906/LeetCode/blob/main/0007/7_Reverse%20Integer(v1).py "想法一的程式碼")  
  - 先去判斷整數`x`是正數或是負數，將其轉成list的格式  
  - 若`x`是正數，就從list的最後一個元素(也就是整數x的最後一個位數)開始，依序往前處理每個數字，每個數字都會乘以相應的10的次方，並累加結果；  
    若`x`是負數，進行類似的處理，差別在過程中是累減 且 只會處理到list的第二個元素而已，因為list的第一個元素是負號(-)  
  - 計算完成後，檢查反轉後的數字是否在32位元整數範圍 [-2<sup>31</sup> , 2<sup>31</sup>-1] 內。如果超出範圍，則回傳 0；否則回傳反轉後的值  
  <br/>

  > 例如 :  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 1203，反轉後的值 = 0 + 3x10<sup>3</sup> + 0x10<sup>2</sup> + 2x10<sup>1</sup> + 1x10<sup>0</sup> = 0 + 3000 + 0 + 20 + 1 = 3021  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = -9876，反轉後的值 = 0 - 6x10<sup>3</sup> - 7x10<sup>2</sup> - 8x10<sup>1</sup> - 9x10<sup>0</sup> = 0 - 6000 - 700 - 80 - 9 = -6789
- **想法二 :**&nbsp;&nbsp;&nbsp;&nbsp;[程式碼 --> 7_Reverse Integer(v2).py](https://github.com/YuTing4906/LeetCode/blob/main/0007/7_Reverse%20Integer(v2).py "想法二的程式碼")  
  - 先去判斷整數`x`是正數或是負數，無論`x`是正數或是負數，**一律將`x`轉成正數**，以便進行後續處理，**因為負數除法和取餘數運算在python中與一般的運算不太一樣**  
  - 接著使用一個while迴圈來逐位處理`x`的數字，在每次迴圈中，將整數`x`的最後一位數提取出來，並將其加到暫時儲存反轉數字變數的尾端，然後通過整數除法去掉`x`的最後一位數，再進到下一回合，直到`x`變成0就結束while迴圈  
  - 然後將反轉後的數字乘以1(當`x`是正數時) 或是 -1(當`x`是負數時)，來恢復原本的符號  
  - 最後檢查反轉後的數字是否在32位元整數範圍 [-2<sup>31</sup> , 2<sup>31</sup>-1] 內。如果超出範圍，則回傳 0；否則回傳反轉後的值  
  <br/>
  
  **注意 :**  
  1. 在python中做除法運算的時候，  
     使用單斜線(/)的除法時，計算結果會**帶有**小數點，例如: 123/10 = 12.3  、  -123/10 = -12.3  
     使用雙斜線(//)的除法時，計算結果會**捨棄**小數點，例如: 123//10 = 12  、  -123//10 = -13 (會取floor)  
  2. 在做取餘數的時候，  
     大部分的程式語言使用的是『**Truncated Division**』，例如: -123%10 = -3，因為-123 = -12x10 + (-3)  
     但python使用的是『**Floor Division**』，例如: -123%10 = 7，因為-123 = -13x10 + 7

  <br/>
  
  > 例如 : x = 1203  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一輪 --> 反轉後的值 = 0x10 + 1203%10 = 3  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 1203//10 = 120  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第二輪 --> 反轉後的值 = 3x10 + 120%10 = 30  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 120//10 = 12  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第三輪 --> 反轉後的值 = 30x10 + 12%10 = 302  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 12//10 = 1  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第四輪 --> 反轉後的值 = 302x10 + 1%10 = 3021  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 1//10 = 0  
- **想法三 :**&nbsp;&nbsp;&nbsp;&nbsp;[程式碼 --> 7_Reverse Integer(v3).py](https://github.com/YuTing4906/LeetCode/blob/main/0007/7_Reverse%20Integer(v3).py "想法三的程式碼")  
  - 先去判斷整數`x`是正數或是負數
  - 若`x`是正數，先將`x`轉成字串(也就是list的格式)，**利用[::-1]反轉list**，再轉成int的格式
    若`x`是負數，先轉成正數，進行與當`x`是正數時相同的處理，最後再乘以-1，來恢復原本的符號
  - 最後檢查反轉後的數字是否在32位元整數範圍 [-2<sup>31</sup> , 2<sup>31</sup>-1] 內。如果超出範圍，則回傳 0；否則回傳反轉後的值
  <br/>
  
  **Note :**  
  - 在python中，list的[]中有3個參數，用冒號分割 --> list[參數1 : 參數2 : 參數3]
    <br/>
    
    |參數  |說明    |
    |-----|--------|
    |參數1 |相當於start_index，可以為空，預設是0|
    |參數2 |相當於end_index，可以為空，預設是list.size|
    |參數3 |步長，預設為1。步長為-1時，回傳倒序原序列|
  - list的幾種用法:
    <br/>
    
    範例: li = [a,b,c,d,e]
    <br/>
    
    |編號   |輸入    |輸出    |註解    |
    |------|--------|--------|--------|
    | 1. |  li[1:]   |  [b,c,d,e]   |  start_index = 1；index的range為[1,5)                                |
    | 2. |  li[1:4]  |  [b,c,d]     |  start_index = 1，end_index = 4；index的range為[1,4)                 |
    | 3. | li[1:4:2] |  [b,d]       |  start_index = 1，end_index = 4，步長 = 2；index的range為[1,4)        |
    | 4. | li[:4]    |  [a,b,c,d]   |  start_index = 0，end_index = 4；index的range為[0,4)                 |
    | 5. | li[::2]   |  [a,c,e]     |  start_index = 0，end_index = list.size，步長 = 2；index的range為[0,5)|
    | 6. | li[-1]    |  e           |  start_index = -1；-1表示倒數第一個                                   |
    | 7. | li[:-1]   |  [a,b,c,d]   |  start_index = 0，end_index = -1；index的range為[0,4)                |
    | 8. | li[::-1]  |  [e,d,c,b,a] |  start_index = 0，end_index = list.size，步長 = -1；作用是反轉原list  |
    

    [參考網址](https://blog.csdn.net/weixin_39630880/article/details/110397646)
## 範例 :mag:
- **範例1 :**  
  **輸入 :** x = 123  
  **輸出 :** 321  
- **範例2 :**  
  **輸入 :** x = -123   
  **輸出 :** -321  
- **範例3 :**  
  **輸入 :** x = 120   
  **輸出 :** 21  
- **範例4 :**  
  **輸入 :** x = 1534236469   
  **輸出 :** 0  
  **說明 :** 因為反轉後的數值為9646324351, 超過32位元整數範圍 [-2<sup>31</sup> , 2<sup>31</sup>-1] = [-2147483648 , 2147483647], 所以回傳0 
