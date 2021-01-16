# 脚本里面调用时，还得传3个参数
def assertListSize(listEntry,expect_value):
    length = len(listEntry)
    print(listEntry,"list长度",length)
    assert length == expect_value

if __name__ == "__main__":
    list = list(['physics', 'chemistry', 1997, 2000])
    assertListSize(*list,4)