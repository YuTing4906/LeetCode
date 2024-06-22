# LeetCode 14. Longest Common Prefix
*****

## 題目 :book:
題目給一個**字串**的list `strs`，寫一個function來找到`strs`中的**最長公共前綴(Longest Common Prefix)**，最後回傳這個最長公共前綴(Longest Common Prefix)，**如果沒有公共前綴，則返回空字串 ""**  
> 限制條件: 1 <= strs.length <= 200  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 <= strs[i].length <= 200  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; strs[i] 僅由小寫英文字母組成  

[完整題目](https://leetcode.com/problems/longest-common-prefix/description/)

## 解題想法 :bulb:
- **想法一 :**&nbsp;&nbsp;&nbsp;&nbsp;[程式碼 --> 14_Longest Common Prefix(v1).py](https://github.com/YuTing4906/LeetCode/blob/main/0014/14_Longest%20Common%20Prefix(v1).py "想法一的程式碼")
  <br/>
  
  - 先找出`strs`中最短字串的長度`shortest_str`，這樣可以確保在比較前綴時不會超出任何字串的長度  
  - 然後跑兩個for迴圈，依序比較每個字串在相同位置上的字元  
    如果在某個位置發現字元不匹配，則回傳當前的最長公共前綴`long_common`  
    如果所有字串在某個位置上的字元都匹配，則將該字元加到`long_common`中  
  <br/>

  > 例如 :  strs = ["flower", "flow", "flight"]  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`strs`中的最短字串為"flow"，所以`shortest_str` = 4，代表最長公共前綴的長度最多只有4而已~  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一輪 -> 拿`strs`中的第一個字串"flower"的第一個字元f，與"flow"和"flight"的第一個字元相同  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此目前`long_common` = f  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第二輪 -> 拿`strs`中的第一個字串"flower"的第二個字元l，與"flow"和"flight"的第二個字元相同  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此目前`long_common` = fl  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第三輪 -> 拿`strs`中的第一個字串"flower"的第三個字元o，與"flow"的第三個字元相同，但與"flight"不同    
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此結束迴圈，回傳當前的最長公共前綴(`long_common` = fl)  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第四輪 -> 不會run到  
- **想法二 :**&nbsp;&nbsp;&nbsp;&nbsp;[程式碼 --> 14_Longest Common Prefix(v2).py](https://github.com/YuTing4906/LeetCode/blob/main/0014/14_Longest%20Common%20Prefix(v2).py "想法二的程式碼") 
  <br/>
  
  - 先對`strs`按照英文字母的先後順序(a~z)進行排序，**利用.sort()來實現**  
  - 然後**比較排序後的第一個字串和最後一個字串**，因為排序後的第一個和最後一個字串具有最大的差異，所以只需要比較這兩個字串就能找到公共前綴
  - 迴圈最多只會跑「`strs`中最短字串的長度」次
  <br/>
  
  **Note :** .sort() vs sorted
  <br/>
    
  |指令名稱  |說明    |
  |-----|--------|
  |.sort() |直接在原list中進行排序(也就是**直接更改原List**中的順序，所以沒有回傳)|
  |sorted() |會先**複製一份再進行排序**，所以不會更動到原List中的順序，會回傳排序後的List|

  <br/>

  > 例如 :  strs = ["flower", "flow", "flight"]  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;排序後`strs` = ["flight", "flow", "flower"]，然後比較"flight"和"flower"即可  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一輪 -> 比較"flight"的第一個字元f，與"flower"的第一個字元相同，因此目前`long_common` = f  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第二輪 -> 比較"flight"的第二個字元l，與"flower"的第二個字元相同，因此目前`long_common` = fl  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第三輪 -> 比較"flight"的第三個字元i，與"flower"的第三個字元不同  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此結束迴圈，回傳當前的最長公共前綴(`long_common` = fl)  
  > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第四輪 -> 不會run到  
  ## 範例 :mag:
- **範例1 :**  
  **輸入 :** strs = ["flower","flow","flight"]  
  **輸出 :** "fl"
- **範例2 :**  
  **輸入 :** strs = ["dog","racecar","car"]   
  **輸出 :** ""  
  **說明 :** 因為這些字串並沒有共同的Prefix, 所以回傳空字串  
