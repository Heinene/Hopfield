import numpy as np


class Hopfield:
    def __init__(self, size: int):
        self.size = size
        self.we_ma = np.zeros((size, size), dtype=int)

    def val(self, net: int, f_net: int):
        if net > 0:
            return 1
        elif net < 0:
            return -1
        else:
            return f_net

    def matr_ves(self, vec_standards):
        for j in range(self.size):
            for k in range(self.size):
                if j == k:
                    self.we_ma[j][k] = 0
                else:
                    self.we_ma[j][k] = sum(
                        [vec_standards[l][j] * vec_standards[l][k] for l in range(len(vec_standards))])

    def rasp(self, vec_input):
        vec_y = [0 for _ in range(len(vec_input))]
        while not (np.array_equal(vec_y, vec_input)):
            for k in range(len(vec_input)):
                net = 0
                for j in range(k):
                    net += self.we_ma[j][k] * vec_y[j]
                for j in range(k + 1, len(vec_input)):
                    net += self.we_ma[j][k] * vec_input[j]
                vec_y[k] = self.val(net, vec_input[k])
            vec_input = vec_y
        return vec_y


def prin(x):
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
    S = [+1, +1, +1,
         -1, +1, +1,
         -1, +1, -1, 
         +1, +1, -1, 
         +1, +1, +1]

    T = [+1, -1, -1, 
         -1, -1, +1,
         +1, +1, +1, 
         +1, +1, -1,
         -1, -1, -1]

    U = [+1, +1, +1,
         +1, +1, -1,
         -1, -1, -1,
         +1, +1, +1, 
         +1, +1, +1]

    SS = [-1, +1, +1,
          -1, +1, +1,
          -1, +1, +1,
          +1, -1, -1,
          +1, +1, -1]

    TT =[-1, +1, -1,
         -1, -1, +1,
         +1, +1, -1,
         +1, +1, +1,
         -1, -1, -1]

    UU =[-1, +1, +1,
         +1, -1, -1,
         -1, -1, +1,
         +1, +1, -1,
         +1, +1, +1]

    network = Hopfield(5 * 3)
    network.matr_ves([S, T, U])
    print(network.we_ma)

    prin(S)
    prin(SS)
    prin(network.rasp(SS))

    prin(T)
    prin(TT)
    prin(network.rasp(TT))

    prin(U)
    prin(UU)
    prin(network.rasp(UU))

