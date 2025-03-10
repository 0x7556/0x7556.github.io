import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("欢迎来到猜数字游戏！")
    print("我已经选择了一个 1 到 100 之间的数字。你有 10 次机会来猜它。")

    while attempts < max_attempts:
        guess = int(input("请输入你的猜测："))
        attempts += 1

        if guess < number_to_guess:
            print("太小了！")
        elif guess > number_to_guess:
            print("太大了！")
        else:
            print(f"恭喜你！你猜对了，数字是 {number_to_guess}。")
            break
    else:
        print(f"很遗憾，你没有猜对。正确的数字是 {number_to_guess}。")

guess_number()