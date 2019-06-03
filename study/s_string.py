'''
字符串常用操作
python 中字符串的标示方式 是以 ''  "" 或者 """""" 包裹起来的


'''
import time
# 字符串的声明
s1= 'hello'
s2 = "hello"
s3 = """hello"""
print(s1==s2==s3) # True
# 字符串常用操作 python 中字符串支持索引 切片 和 索引 像列表一样 但python字符串是不可变的
print(s1[0])
print(s1[1:3])
for s in s1:
    print(s)
# 字符串操作优化
s = 'H' + s[1:]
s = s.replace('h', 'H')
# 上边的两种方式 其实都是创建了一个新的字符串出来

s2 += s1
# 上边这种方式 在python新版本中 会原地扩展 s2 的大小 不会创建新的内存 这种效率更高

# 字符串的split操作 strip操作
s5 = 'a v d e r'
s_l = s5.split(' ') # 得到数组 按空格分割
s6 = ' asd sad '
s6 = s6.strip()
print (s6)  # 去掉两端空格 同时还有lstrip rstrip 只去掉左边或者右边的空格
# 字符串的格式化 string.format()
s = 'today weather is {} today is'.format('sunday', 'wonday')
print (s)  # today weather is sunday today is

t1 = time.perf_counter()
s = ''
for i in range(0,1000000):
    s += str(i)
t2 = time.perf_counter()
print ('方式一耗费时间 {}'.format(t2-t1))  # 0.4358797559980303

t1 = time.perf_counter()
s = []
for i in range(0,1000000):
    s.append(str(i))
s1 = ''.join(s)
t2 = time.perf_counter()
print ('方式二耗费时间 {}'.format(t2-t1))  # 0.37377301102969795

t1 = time.perf_counter()
s1 = ''.join(map(str, range(0, 1000000)))
t2 = time.perf_counter()
print ('方式三耗费时间 {}'.format(t2-t1))  # 0.2560606470797211

### python I/O 操作

# 文件的输入和输出 r rw w 文件打开的权限设置 分别为 读 可读可写 写 三种权限

words = {}
with open('./test.txt', 'r') as f:  # 这种方式打开文件不需要考虑 关闭 更方便
    lines = f.readlines()  # 读出所有行
    for line in lines:
        if line != '':
            ls = line.split(' ')
            for w in ls:
                if w not in words:
                    words[w] = 1
                else:
                    words[w] += 1  # 统计词频
sort_words = sorted(words.items(), key=lambda kv:kv[1], reverse=True)
print (sort_words)
with open('./test1.txt','w') as f:  # 文件权限
    for k,v in sort_words:
        f.write('{} {}\n'.format(k, v))

# JSON 序列化
import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

s = json.dumps(params)
print (type(s))
s = json.loads(s)
print (type(s))

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
