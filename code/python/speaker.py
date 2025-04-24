import time
import sys
### Author WebSite
### http://18k.icu
### https://blog.csdn.net/OneCrab
### https://github.com/0x7556
def type_out(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # 刷新输出缓冲区
        time.sleep(delay)  # 等待指定的延迟
    print()  # 打印换行

# 对话内容
dialogue = [
    ("A", "你是谁啊!"),
    ("B", "我是你爸!"),
    ("A", "爸啊，我是你好大儿!"),
    ("C", "你们在聊什么呢?"),
    ("A", "我们在讨论家庭关系。"),
    ("B", "对啊，家庭是最重要的。"),
    ("C", "我同意，家人永远是支持我们的。"),
    ("A", "那我们一起去吃饭吧!"),
    ("B", "好主意，我请客!"),
    ("C", "太好了，我最喜欢吃饭了!")
]

# 输出对话
for speaker, text in dialogue:
    type_out(f"{speaker}: {text}")
    time.sleep(1)  # 每次对话后等待1秒
