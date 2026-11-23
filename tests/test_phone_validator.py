import pytest

from src.phone_validator import is_valid_phone


# 每一行就是一个测试用例：左边是输入，右边是预期结果。
# 这些行不是随手写的，是按"等价类划分 + 边界值"选出来的：
#   有效等价类  -> 合法的 11 位正常号段
#   无效等价类  -> 长度不对、号段不对、含字母、空值
#   边界值      -> 长度临界（10 位 / 11 位 / 12 位）、空串
@pytest.mark.parametrize("phone, expected", [
    ("13800138000", True),    # 有效等价类
    ("19912345678", True),    # 有效等价类，另一个号段
    ("1380013800", False),    # 边界值：10 位，少一位
    ("138001380001", False),  # 边界值：12 位，多一位
    ("12800138000", False),   # 无效等价类：第二位不在 3-9
    ("23800138000", False),   # 无效等价类：不以 1 开头
    ("1380013800a", False),   # 无效等价类：含字母
    ("", False),              # 边界值：空串
])
def test_is_valid_phone(phone, expected):
    assert is_valid_phone(phone) == expected
