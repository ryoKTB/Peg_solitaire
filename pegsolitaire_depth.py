import copy
import sys
import time
import argparse
from collections import deque

# 盤面（問題）の情報が入った二次元配列
# problem_Aの七行目の[1]は、木の“深さ”を格納するものであり、深さが深くなるたびにここを更新することで、深さ（すなわち手数）を管理している。（他の問題でも同様である）
problem_A = [[0, 0, 0, 0, 0],
             [0, 0, 0, 'x', 0],
             [0, 0, 0, 0, 0],
             [0, "o", "o", "o", 0],
             [0, 0, 0, "o", 0],
             [0, 0, 0, 0, 0],
             [1]]

problem_B = [[0, 0, 0, "o", 0, 0, 0],
             [0, 0, 0, "o", 0, 0, 0],
             ["o", "o", 0, "x", 0, "o", "o"],
             [0, 0, 0, "o", 0, 0, 0],
             [0, 0, 0, "o", 0, 0, 0],
             [1]]

problem_C = [[0, 0, "x", 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             ["o", "o", "o", "o", "o"],
             [0, 0, "o", 0, 0],
             [0, 0, "o", 0, 0],
             [0, 0, "o", 0, 0],
             [1]]

problem_D = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, "x", 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0,"o","o","o","o","o","o","o",0],
             [0, 0,"o","o","o","o","o","o",0, 0],
             [0, 0,"o","o","o","o","o",0, 0, 0],
             [0, 0, 0, 0,"o", 0,"o", 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1]]


# 盤面を絵画するための関数
def draw(p_list, num):
    print(num, end=".\n")
    h = len(p_list) - 1
    w = len(p_list[0])
    for i in range(h):
        for _ in range(w):
            print("-", end = "")
        print("")
        for j in range(w):
            if p_list[i][j] == "o":
                print("o", end = "")
            elif p_list[i][j] == "x":
                print("x", end = "")
            else:
                print(" ", end = "")
        print("")
    for _ in range(w):
        print("-", end = "")
    print("\n")
    for _ in range(7 * w):
        print("_", end = "")
    print("\n")
    print("depth = ", end = "")
    print(p_list[h][0])
    print("\n\n")


def draw_tmp(p_list, num):
    h = len(p_list) - 1
    print(num, end=".  ")
    print("depth = ", end = "")
    print(p_list[h][0])
    print("\n\n")


# p_list[i][j]が駒である場合のみ呼び出される。この駒が前後左右に動けるかどうかを確認し、動ける場合にはそこからそのコマが移動した後の状態の盤面を返す。
def find_ways(p_list, i, j):
    h = len(p_list) - 1
    w = len(p_list[0])
    ways = []

    if j >= 2:
        if p_list[i][j-1] == "o" and p_list[i][j-2] != "o":
            p_way1 = copy.deepcopy(p_list)
            p_way1[i][j-2] = "o"
            p_way1[i][j-1] = 0
            p_way1[i][j] = 0
            ways.append(p_way1)

    if i >= 2:
        if p_list[i-1][j] == "o" and p_list[i-2][j] != "o":
            p_way2 = copy.deepcopy(p_list)
            p_way2[i-2][j] = "o"
            p_way2[i-1][j] = 0
            p_way2[i][j] = 0
            ways.append(p_way2)

    if j <= w - 3:
        if p_list[i][j+1] == "o" and p_list[i][j+2] != "o":
            p_way3 = copy.deepcopy(p_list)
            p_way3[i][j+2] = "o"
            p_way3[i][j+1] = 0
            p_way3[i][j] = 0
            ways.append(p_way3)

    if i <= h - 3:
        if p_list[i+1][j] == "o" and p_list[i+2][j] != "o":
            p_way4 = copy.deepcopy(p_list)
            p_way4[i+2][j] = "o"
            p_way4[i+1][j] = 0
            p_way4[i][j] = 0
            ways.append(p_way4)

    return ways

# 木を展開する関数。盤面の情報を一つずつ調べ、駒があれば先述のfind_ways関数を呼び出す。
def expand(p_list):
    h = len(p_list) - 1
    w = len(p_list[0])
    answers = []

    for i in range(h):
        for j in range(w):
            if p_list[i][j] != "o":
                continue
            else:
                p_lis_2 = copy.deepcopy(p_list)
                ways = find_ways(p_lis_2, i, j)
                for way in ways:
                    answers.append(way)

    return answers


def parse_cl_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, default='a', dest='problem', help='Choice the problem you want to solve(a ~ d)')

    args = parser.parse_args()
    return args


def main():
    args = parse_cl_args()
    problem = args.problem
    
    if problem == 'a':
        problem = problem_A
    elif problem == 'b':
        problem = problem_B
    elif problem == 'c':
        problem = problem_C
    else:
        problem = problem_D
    
    start = time.time()

    h = len(problem) - 1
    w = len(problem[0])

    number = 1


    x_h, x_w = 0, 0
    for i in range(h):
        for j in range(w):
            if problem[i][j] == "x":
                x_h, x_w = i, j
                break
    
    OPEN, CLOSED = [problem], []
    OPEN = deque([problem])
    CLOSED = deque()

    while len(OPEN) > 0:
        # 先頭を取り出す
        k = OPEN.popleft()
        depth = k[h][0]
        if k in CLOSED:
            continue

        # 解が得られた場合、終了
        if k[x_h][x_w] == "o":
            print("find the answer !")
            draw(k, number)
            print("\n")
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
            return

        if number < 10 or number % 1000 == 0:
            draw(k, number)
        else:
            draw_tmp(k, number)
        number += 1

        # ノードを展開
        answers = expand(k)

        # 探索済一覧に追加
        CLOSED.append(k)

        ct = 0

        for ans in answers:
            if ans in OPEN or ans in CLOSED:
                continue
            else:
                ans[h][0] = depth + 1
                # 先頭に追加
                if len(OPEN) == 0:
                    OPEN.append(ans)
                    ct += 1
                else:
                    OPEN_tmp = copy.deepcopy(OPEN)
                    OPEN = deque()
                    OPEN.append(ans)
                    for tmp in OPEN_tmp:
                        OPEN.append(tmp)
                    ct += 1

        if ct == 0:
            print("No more deep nodes. Moving on to other nodes.", end="\n\n\n\n")

    print("Cannot find the answers.")
    print("\n")
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    return 0

if __name__ == '__main__':
    main()
