"""This code implements an algorithim that performs  the shaker sort method """
""" 
Step 1: 
    assign variable left to 0 representing the lowest index. 
    assign variable right to the length of the array -1 
    representing highest index.
Step 2: 
   nested for loop with counter i in range right to left moving by -1
       first for loop comparing the values from index to the left moving by -1
       second for loop comparing the lowest value to the highest and comparing 
       while incrementing by +1 
Step 3 : 
    Print the list 
    
    
 """
l = [4,90,1,3,5,2,-1,-90]

left = 0 # representing the lowest index 
right = len(l)-1 # representing the highest index
# nested for loop itterating from right to the left of the array
for i in range(right ,left,-1):
   #for loop that will move the lowest value to the left
    for j in range(i, left,-1):
       if (l[j]<l[j-1]):
           l[j],l[j-1] = l[j-1],l[j] 
   #for loop that will move the highes value to the right
    for k in range(i):
        if (l[k]>l[k+1]):
            l[k],l[k+1] = l[k+1],l[k]

print(*l)
            