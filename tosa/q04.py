def graph_matrix_to_list(m):
    result = []
    for line in m:
        print(line)
        line_result = []
        for index, elem in enumerate(line):
            if elem:
                line_result.append(index)
        result.append(line_result)
    return result
    # [ [1] , []  ]

def graph_matrix_to_list_v2(m):
    result = []
    for line in m:
        line_result = [i for i, elem in enumerate(line) if elem]
        result.append(line_result)
    return result

test1 = [[False, True],
         [False, False]]

test2 = [[False, True, True],
         [True, False, False],
         [True, True, False]]

print(graph_matrix_to_list_v2(test2))
