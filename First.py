age = 10

if age>18:
    #如果条件满足,那么下面的4行代码一定执行
    print("----0-----")
    print("----1-----")
    print("----1-----")
    print("----1-----")
else:
    #如果第3行的代码,条件不满足,那么就执行接下来的4行代码
    print("----1-----")
    print("----1-----")
    print("----1-----")
    print("----1-----")

#下面的这行代码,与上面的if没有任何的关系,即第3行的条件是否满足 与这里执行没有任何的影响
print("----9-----阿斯顿")