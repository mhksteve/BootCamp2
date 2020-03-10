List - []

word = 'Programming'

index

  P  r  o  g  r  a  m  m  i  n  g
  0  1  2  3  4  5  6  7  8  9  10
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

word[0]
word[-2]
word[3:5]
word[4:9]
word[:5]
word[8:]
word[5:-3]
word[:2] + word[3:]

len(word)

# Len = Length

square = 'Square'
len(square)
len(word) + len(square)


cube = [10, 20, 30, 45, 50]
cube[3] = 40
cube
cute[5] = 60 #error out of range
cube.append(60)
cube.append(4+10+20+36)
cube
cube.reverse()
cube
cube.sort() #to sort accendingly 
cube
cube.remove(20)
cube
cube.pop() #remove the last number from list
cube

cube1 = [10, 20, 30, 45, 50]
cube2 = [1, 2, 3, 4, 5]
cube.extend(cube2)
cube1 + cube2			#they don't have same result

del cube[3]
cube
del cube[1:3]
cube  
del cube[:]
cube  #nothing left

programA = ['A', 'B', 'C'. 'D', 'E']
programB = ['a', 'b', 'c', 'd', 'e']
ProgramC = programA + programB
ProgramC
len(ProgramC)


a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [110, 120, 130, 140, 150]
x = [a, b, c]
x   #[[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
 
x[1][2]    #80
x[1:2][1:2] #nothing
x[0][0] #10
x[1][1] #70

