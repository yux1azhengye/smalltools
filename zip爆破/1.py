import argparse

##第一步创建ArgumentParser() 对象
#创建该对象时的参数都是有默认值的，不过大多数对 ArgumentParser 构造方法的调用都会使用 description= 关键字参数。 这个参数简要描述这个程序做什么以及怎么做。
parser = argparse.ArgumentParser(description='Process some integers.')

#- 调用 add_argument() 方法添加参数

#第一个参数:参数名(属性名)
#metavar='N' :在 usage 说明中的参数名称
#type=int :参数的指定类型为int(不符合该类型会报错)
#nargs='+' :'+'所有当前命令行参数被聚集到一个列表中
#help :命令行-h获取帮助时的显示
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

#第一个参数:选项
#dest='accumulate':对于可选参数动作，dest 的值通常取自选项字符串，此处就是字符串'accumulate',此字符串会作为最后调用parse_args()返回的属性名
#当有action='store_const',就需要添加const属性对action做出补充
#'store_const' - 存储被 const 命名参数指定的值(一般),而此处是一个函数sum(在指定--sum时为sum,若未指定则为默认的max函数)

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

#parse_args() 解析添加的参数
args = parser.parse_args()
print(args.accumulate(args.integers))