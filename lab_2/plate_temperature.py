c  = 2
p = 100
l = 20
uMean = 100
h = 0.2
s = 0.1 
n = 5
a = 50

array = [
    [20, 20, 20, 20, 20, 20],
    [20, 20, 20, 20, 20, 20],
    [20, 20, 20, 20, 20, 20],
    [20, 20, 20, 20, 20, 20],
    [20, 20, 20, 20, 20, 20],
    [20, 20, 20, 20, 20, 20]
]
u_arr = array.copy()

for i in range(5):

    for i in range(1, n):
        for j in range(1, n):
            array[i][j] = (l * s / (c * p * (h ** 2))) * u_arr[i+1][j] + u_arr[i-1][j] + u_arr[i][j+1] + u_arr[i][j-1] - 4 * u_arr[i][j] + u_arr[i][j]

    for j in range(n+1):
        array[0][j] = (a * h / l * uMean + array[1][j])/(1 + a * h / l)
        array[n][j] = (a * h / l * uMean + array[n-1][j])/(1 + a * h / l)

    for i in range(n+1):
        array[i][0] = (a * h / l * uMean + array[i][1])/(1 + a * h / l)
        array[i][n] = (a * h / l * uMean + array[i][n-1])/(1 + a * h / l)

    u_arr = array.copy() 
    array = u_arr.copy()   

