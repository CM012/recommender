# cli.py
import argparse
# 创建解析器
parser = argparse.ArgumentParser(description='Calc Add')

# 添加位置参数
parser.add_argument('a', type=int, help='variable a to add')
parser.add_argument('b', type=int, help='variable b to add')

# 解析参数
args = parser.parse_args()
# 使用参数
print( args.a, args.b)

