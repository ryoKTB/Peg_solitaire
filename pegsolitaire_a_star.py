import copy
import sys
import time
import argparse
from collections import deque

problem_A = [[0, 0, 0, 0, 0],
             [0, 0, 0, 'x', 0],
             [0, 0, 0, 0, 0],
             [0, "o", "o", "o", 0],
             [0, 0, 0, "o", 0],
             [0, 0, 0, 0, 0],
             [1, 0]]

problem_B = [[0, 0, 0, "o", 0, 0, 0],
             [0, 0, 0, "o", 0, 0, 0],
             ["o", "o", 0, "x", 0, "o", "o"],
             [0, 0, 0, "o", 0, 0, 0],
             [0, 0, 0, "o", 0, 0, 0],
             [1, 0]]

problem_C = [[0, 0, "x", 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             ["o", "o", "o", "o", "o"],
             [0, 0, "o", 0, 0],
             [0, 0, "o", 0, 0],
             [0, 0, "o", 0, 0],
             [1, 0]]

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
             [1, 0]]

problem_A_GOAL = [[0, 0, 0, 0, 0],
             [0, 0, 0, 'o', 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0]]

problem_B_GOAL = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, "o", 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [1, 0]]

problem_C_GOAL = [[0, 0, "o", 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0]]

problem_D_GOAL = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, "o", 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0]]

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
    print(p_list[h][0], end = ",  ")
    print("f = ", end="")
    print(p_list[h][1])
    print("\n\n")

def draw_tmp(p_list, num):
    h = len(p_list) - 1
    print(num, end=".  ")
    print("depth = ", end = ", ")
    print(p_list[h][0])
    print("f = ", end="")
    print(p_list[h][1])
    print("\n\n")

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

# f値に応じて適切な箇所に挿入
def insert_ans(OPEN, ans):
    if len(OPEN) == 0:
        OPEN = deque([ans])
        return OPEN
    
    h = len(ans) - 1
    f_value = ans[h][1]
    
    n = len(OPEN)
    
    for i in range(n):
        tmp_k = OPEN[i]
        f = tmp_k[h][1]
        if f_value < f:
            OPEN.insert(i, ans)
            return OPEN
    
    OPEN.insert(n, ans)
    return OPEN


def calc_f_value(problem, p_ans):
    h = len(problem) - 1
    w = len(problem[0])

    s = 0

    for i in range(h):
        for j in range(w):
            if problem[i][j] != p_ans[i][j]:
                s += 1

    problem[h][1] = problem[h][0] + s


def calc_f_value_2(problem, p_ans, x_h, x_w):
    h = len(problem) - 1
    w = len(problem[0])

    s = 0

    for i in range(h):
        for j in range(w):
            if problem[i][j] != p_ans[i][j]:
                if (i == x_h and (j == x_w - 1 or j == x_w + 1)) or (j == x_w and (i == x_h - 1 or i == x_h + 1)):
                    s += 1
                else:
                    s += 2

    problem[h][1] = problem[h][0] + s


def calc_f_value_3(problem, p_ans, x_h, x_w):
    h = len(problem) - 1
    w = len(problem[0])

    s = 0
    if problem[x_h][x_w] == "o":
        s -= 1000

    for i in range(h):
        for j in range(w):
            if problem[i][j] != p_ans[i][j]:
                if problem[i][j] == "x":
                    continue
                else:
                    # マンハッタン距離の半分をf値に加える
                    s += (abs(x_h - i) + abs(x_w - j)) // 2

    problem[h][1] = problem[h][0] + s

def parse_cl_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, default='a', dest='problem', help='Choice the problem you want to solve(a ~ d)')

    args = parser.parse_args()
    return args


def main():
    args = parse_cl_args()
    problem = args.problem
    ans_problem = None
    
    if problem == 'a':
        problem = problem_A
        ans_problem = problem_A_GOAL
    elif problem == 'b':
        problem = problem_B
        ans_problem = problem_B_GOAL
    elif problem == 'c':
        problem = problem_C
        ans_problem = problem_C_GOAL
    else:
        problem = problem_D
        ans_problem = problem_D_GOAL

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
    
    #calc_f_value(problem, ans_problem)
    #calc_f_value_2(problem, ans_problem, x_h, x_w)
    calc_f_value_3(problem, ans_problem, x_h, x_w)

    OPEN, CLOSED = [problem], []
    OPEN = deque([problem])
    CLOSED = deque()
    


    while len(OPEN) > 0:
        # 先頭を取り出す
        k = OPEN.popleft()
        depth = k[h][0]
        tmp_k = copy.deepcopy(k)
        tmp_k[h][1] = 0

        if tmp_k in CLOSED:
            continue

        if k[x_h][x_w] == "o":
            print("find the answer !")
            draw(k, number)
            print("\n")
            elapsed_time = time.time() - start
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
            return

        draw(k, number)
        number += 1

        answers = expand(k)

        CLOSED.append(tmp_k)

        ct = 0

        for ans in answers:
            ans[h][0] = depth + 1
            calc_f_value_3(ans, ans_problem, x_h, x_w)
            tmp_ans = copy.deepcopy(ans)
            tmp_ans[h][1] = 0
            if ans in OPEN or tmp_ans in CLOSED:
                continue
            else:
                # f値に応じて適切な箇所に挿入
                OPEN = insert_ans(OPEN, ans)
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