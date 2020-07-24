#lists for even  numbers
even = [2, 4, 6, 8, 10]
for i in range(11): #outer loop
  print("outer loop | i = " + str(i))
  for j in range(11): #inner loop
    print("inner loop | i = " + str(i) + " | j = " + str(j)) 
    #check the lists to see if the values for i and j are even
    if i in even and j in even: 
      print("i and j are even")
    