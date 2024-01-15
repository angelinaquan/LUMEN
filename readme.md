## README

### 代码结构

```
test.py --------------------------- 用于统计多次测试的平均结果
main.py --------------------------- 调用下述.py文件实现算法
ZK_setup.py
PIOPprotocol.py
ZK_RecursiveProtocol.py
ZK_commit.py
ZK_open.py
Crypto_func.py -------------------- 包含常用密码学函数
ZK_VeriftEval.py 
ZK_VerifyPoly.py
Decision.py
fig_poly_bit.py ------------------- 用于统计Byte

其他test_setup.py等以test_开头文件用于测试对应.py文件功能

共16个.py文件，包括test.py fig_poly_bit.py + 10个算法文件(包括main.py) + 3个测试功能文件 + 1个副本(备份) 

```



### 参数修改

**alpha** ：群`G`中元素个数，建议1600，在`main.py`中第21行

**d**：`setup`模块中生成多项式的最高次数，在`main.py`中第22行

**p**：`setup`中用于生成大素数的参数，我给定为64，在`main.py`中第23行

**k**：`PIOPprotocol`中的元组数据，当前给定32，不建议超过256，严重影响`PIOPprotocol`运行效率

，在`main.py`中第59行

**N**，**m**：`PIOPprotocol`中`Online Phase`阶段需要的参数，我在保证运行效率前提下分别给定512、256，保证密码学安全性，在`main.py`中第60~61行