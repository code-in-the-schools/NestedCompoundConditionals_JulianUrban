#lists for even and odd numbers
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
for i in range(11): #outer loop
  print("outer loop | i = " + str(i))
  for j in range(11): #inner loop
    print("inner loop | i = " + str(i) + " | j = " + str(j)) 
    #check the lists to see if the values for i and j are even
    if i in even and j in even: 
      print("i and j are even")
    #check the lists to see if the values for i and j are even
    elif i in odd and j in odd:
      print("i and j are odd")

    