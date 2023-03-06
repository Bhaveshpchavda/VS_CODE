def prac5_3(matrix):
    m = len(matrix)
    n = len(matrix[1])
    flag = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0 and matrix[i][j] != 1:
                flag = 0
                break
        if not flag:
            break
    if flag:
        print("YES, It is a binary matrix")
    else:
        print("NO, It is not a binary matrix")

        
twodarray = [[1,0,1,1],
[1,0,0,1],
[0,0,1,0]]

prac5_3(twodarray)