def levenstein(w1, w2):
    
    if len(w1) == 0 or len(w2) == 0:
        return max(len(w1), len(w2))
    
    else:
        cols = min(len(w1), len(w2))
        rows = max(len(w1), len(w2))
        if len(w1) <= len(w2):
            min_w, max_w = w1, w2
        else:
            min_w, max_w = w2, w1

        A = [x for x in range(cols + 1)]
        LEV = [[m] + [0] * (cols) if m !=0 else A for m in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if max_w[i] == min_w[j]:
                    m = 0
                else:
                    m = 1
                D = min(int(LEV[i + 1][j]) + 1, int(LEV[i][j + 1]) + 1, int(LEV[i][j]) + m)
                LEV[i + 1][j + 1] += D
        return LEV[rows - 1][cols - 1]

w1 = 'лабрадор'
w2 = 'гибралтар'
print(levenstein(w1, w2))

w1 = 'программирование'
w2 = 'лингвистика'
print(levenstein(w1, w2))

w1 = 'levenstein'
w2 = 'einstein'
print(levenstein(w1, w2))