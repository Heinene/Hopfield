import numpy as np


class Hopfild_Network:
    def __init__(self, size: int):
        self.size = size
        self.weight_matrix = np.zeros((size, size), dtype=int)

    def get_value(self, net: int, f_net: int):
        if net > 0:
            return 1
        elif net < 0:
            return -1
        else:
            return f_net

    def calculate_matrix_weights(self, vec_standards):
        for j in range(self.size):
            for k in range(self.size):
                if j == k:
                    self.weight_matrix[j][k] = 0
                else:
                    self.weight_matrix[j][k] = sum(
                        [vec_standards[l][j] * vec_standards[l][k] for l in range(len(vec_standards))])

    def recognition(self, vec_input):
        vec_y = [0 for _ in range(len(vec_input))]
        while not (np.array_equal(vec_y, vec_input)):
            for k in range(len(vec_input)):
                net = 0
                for j in range(k):
                    net += self.weight_matrix[j][k] * vec_y[j]
                for j in range(k + 1, len(vec_input)):
                    net += self.weight_matrix[j][k] * vec_input[j]
                vec_y[k] = self.get_value(net, vec_input[k])
            vec_input = vec_y
        return vec_y


def print_image(x):
    for i in range(5):
        s = ''
        if x[i] == -1:
            s += '   '
        else:
            s += ' * '
        if x[i + 5] == -1:
            s += '   '
        else:
            s += ' * '
        if x[i + 10] == -1:
            s += '   '
        else:
            s += ' * '
        print(s)
    print('\n')


if __name__ == '__main__':
    S = [1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1]
    T = [1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1]
    U = [1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]

    S_dis = [-1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1]
    T_dis = [-1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1]
    U_dis = [-1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1]

    network = Hopfild_Network(5 * 3)
    network.calculate_matrix_weights([S, T, U])
    print(network.weight_matrix)

    print_image(S)
    print_image(S_dis)
    print_image(network.recognition(S_dis))

    print_image(T)
    print_image(T_dis)
    print_image(network.recognition(T_dis))

    print_image(U)
    print_image(U_dis)
    print_image(network.recognition(U_dis))

