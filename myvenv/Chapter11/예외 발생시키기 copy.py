class PoitiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 일력불가")
try:
    num = int(input("음수를 입력해주세요"))
    if num >=0:
        raise PoitiveNumberError
except ProcessLookupError as e:
    print("에러발샹!",e)
