# pylint: skip-file
def count_paths(corridor):
    W = len(corridor[0])
    H = len(corridor)

    a = []
    for row in range(H):
        b = []
        for j in range(W):
            b.append(corridor[row][j])
        a.append(b)

    counter = []
    dict_ = {}
    for i in range(H):
        b = []
        for j in range(W):
            b.append(0)
            dict_.update({a[i][j]: 0})
        counter.append(b)

    for row in range(H):
        counter[row][0] = 1
        dict_.update({a[row][0]: dict_.get(a[row][0]) + 1})

    for col in range(1, W):
        row_dict = {}
        for row in range(H):
            counter[row][col] += dict_.get(a[row][col])
            if a[row][col] != a[row][col - 1]:
                counter[row][col] += counter[row][col - 1]

            if not (a[row][col] in row_dict.keys()):
                row_dict.update({a[row][col]: dict_.get(a[row][col]) + counter[row][col]})
            else:
                row_dict.update({a[row][col]: row_dict.get(a[row][col]) + counter[row][col]})

        for key in row_dict.keys():
            dict_.update({key: row_dict.get(key)})

    total_sum = counter[0][W - 1]
    if H > 1:
        total_sum += counter[H - 1][W - 1]

    return total_sum
