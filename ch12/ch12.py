large = 1000
string = "这是一个字符串"
float = 1.0
broken_int = "这本应该是一个int"
assert large > 500
assert type(string) == type("")
assert type(float) != type(1)
# assert type(broken_int) == type(4)
try:
    assert type(broken_int)==type(4)
except AssertionError as error:
    print("有异常错误")
