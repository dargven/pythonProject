import numpy as np

N = int(input('n = '))
M = int(input('m = '))
matr = np.zeros((N, M))
for ik in range(len(matr)):
    for jk in range(len(matr[ik])):
        i = ik + 1  # [1...N];
        j = jk + 1
        D = i + j - 1  # Номер диагонали
        # Ma = (D * D + D) // 2#Максимальное значение до "центральной диагонали"
        # Mb = (N * N + N) // 2 + ((3 * N - D - 1) * (D - N)) // 2#Максимальное значение после
        # Ca = abs(D//(N + 1) - 1)#Определитель сектора до центральной диагонали
        # Cb = D // (N + 1)
        # Co = D%2#Определитель нечетной диагонали
        # Ce = (D+1)%2#Определитель четной диагонали
        # matr[ik][jk] = Ca*((Ma-j+1)*Ce+(Ma-i+1)*Co)+Cb*((Mb-(N-i))*Ce+(Mb-(N-j))*Co)
        R = (i + j - 2) * (i + j - 1) // 2 + (i + j) % 2 * (j - i) + i+ (1 - N * N + 2 * N * (i + j - 1) - i - j - (i + j - 2) * (i + j - 1)) * ((i + j - 1) // N)
        matr[ik][jk]=R
print(matr)
