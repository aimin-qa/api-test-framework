def is_valid_phone(phone: str) -> bool:
    """校验中国大陆 11 位手机号：必须是 11 位纯数字、1 开头、第二位 3-9。"""
    if not phone or len(phone) != 11:
        return False
    if not phone.isdigit():
        return False
    return phone[0] == "1" and phone[1] in "3456789"
