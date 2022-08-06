def longest_oscillation(L):
    """
    :param L: list
    :return: length output and index
    time complexity: O(n)
    space complexity: O(n)
    L[i] > L[i+1] < L[i+2]
    L[i] < L[i+1] > L[i+2]
    this functions just pass the input to other function
    """
    if len(L) == 0:             # if the input is empty
        return (len(L), [])
    if len(L) == 1:             # if the input only contains a value
        return (len(L), [0])
    m, up, fin, done = oscillation_aux(L)
    if m == up:                 # if the sequence == up
        ans = find_index(fin, done)         # pass fin and done (to make sure the correct array has been given)
    else:
        ans = find_index(done, fin)         # vice versa
    return (len(ans), ans)
def oscillation_aux(L):
    """
    :param L: original list
    :return: max(up, down), up, output
    time complexity: O(n) loop once
    space complexity: O(n) -> output, output2
    this function is to keep track the sequence that goes up and down
    if the sequence is current < next, the next sequence should be added up else the same sequence will still give the
    same number, same goes to current > next
    """
    up = 0  # keep track the sequence
    down = 0
    output = []
    output2 = []
    for i in range(len(L)):
        if L[i - 1] < L[i]:             # if current - 1 < current
            down = up + 1               # down = previous recorded up that sums up the relation L[i] > L[i+1] < L[i+2]
        elif L[i - 1] > L[i]:           # if current -1 > current
            up = down + 1               # up = previous recorded up that sums up the relation L[i] < L[i+1] > L[i+2]
        output.append(up)
        output2.append(down)            # both output will keep track of the sequence
    return (max(up, down), up, output, output2)
def find_index(i, j):
    """
    :param i: array containing the turning points (the main)
    :param j: array containing the turning points
    :return: the index of the oscillation
    time complexity: O(n)
    space complexity: O(n)
    the function will find the turning point in the i array, in the array if current < next then append the index
    the second array is also doing the same thing except the last element in the array will be append in the second last
    index
    """
    output = [-1] * (len(i))            # O(n)

    if i == j:                          # O(n) compare two array
        return [0]

    for k in range(0, len(i)):          # O(n)
        if len(i) - 1 == k:             # if reach the last element
            output[k] = k               # add the last element
        elif i[k + 1] > i[k]:           # if the current < next
            output[k] = k

    for z in range(0, len(j)):          # j array
        if len(i) - 1 == z:             # if reach the last element
            if j[z - 1] == j[0]:        # check edge case if the number for the first to the current is the same
                output[z - 1] = -1      # let it be -1 (will get rid after that)
            output[z] = z               # append the last element
        elif j[z + 1] > j[z]:
            output[z] = z               # append the index
    output[0] = 0                       # initialise the first element as the start point
    output = [x for x in output if x >= 0]  # O(N) deal with all the negative values
    return output

def longest_walk(M):
    """
    :param M: n x m matrix
    :return: the longest possible walk
    time complexity: O(nm) n = rows, m = col
    space complexity: O(nm) where the the dp array is the major space and other space complexity will be lesser
    than O(nm)
    """
    if len(M) == 0 or len(M[0]) == 0:       # if the Matrix is empty
        return (0, [])                      # return
    n = len(M)                              # n = row
    m = len(M[0])                           # m = col
    dp = [[0 for _ in range(m)] for _ in range(n)]
    output = []                             # O(n) ->  for the path

    def seek(i, j):
        """
        :param i: ith row
        :param j: jth column
        :return: the dp[i][j] = length of the path taken
        time complexity: O(n) for each call it will loop once
        space complexity: O(1) not using space, uses the outer function array or Matrix
        this function will move in every direction within the matrix
        it will find the sub-optimal path till the end of the matrix that has been call in the outer function
        """
        if dp[i][j] != 0:
            return dp[i][j]
        opt = 0  # initialize the optimal to 0
        directions = [(0, -1), (1, 1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1)]
        for k in range(len(directions)):        # loop in direction
            x = i+directions[k][0]              # adds the index to its correspondent
            y = j+directions[k][1]
            if n > x >= 0 and m > y >= 0 and M[i][j] < M[x][y]:         # check the boundary and current < next element
                opt = max(opt, seek(x, y))       # recursive call to find the walk
        dp[i][j] = opt+1                         # after the loop then assign the dp[i][j] to the optimal+1
        if len(output) <= opt:  # this is to add the path taken if the optimal path >= the length output
            output.append((i, j))
        return dp[i][j]                         # return a number

    opt = 0                             # set optimal to 0
    for i in range(n):                  # loop in row and col
        for j in range(m):
            opt = max(opt, seek(i, j))   # find the max between opt and the return value from seek function

    done = []
    for i in range(len(output)-1, -1, -1):      # reverse the array
        done.append(output[i])

    return (opt, done)


