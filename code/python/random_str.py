import random
### Author WebSite
### http://18k.icu
### https://blog.csdn.net/OneCrab
### https://github.com/0x7556
def random_quote():
    quotes = [
        "生活就像骑自行车。要保持平衡，你必须不断前进。 - 阿尔伯特·爱因斯坦",
        "成功是从失败到失败，也不失去热情。 - 温斯顿·丘吉尔",
        "你必须成为你想要在这个世界上看到的变化。 - 甘地",
        "在你能做的事情中，做你能做的事情。 - 西奥多·罗斯福"
    ]
    print("随机名言：")
    print(random.choice(quotes))

random_quote()