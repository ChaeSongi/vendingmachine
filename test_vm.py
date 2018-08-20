#
# def test_plus():
#     assert 3 == 1 + 2
#
# # def test_plus():
# #     assert 3 == 1 + 2
#
# from vm import run
# from vm import init

from vm import VendingMachine

def test_insert_coin_and_coffee():
    m = VendingMachine()
    m.run("동전 200")
    assert "커피나옴" == m.run("음료 커피")

def test_next_change_should_be_fifty():
    m = VendingMachine()
    m.run("동전 200")
    m.run("음료 커피")
    assert "잔액은 50원입니다." == m.run("잔액")

def test_next_error():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액부족" == m.run("음료 커피")

#
# # 처음 돌렸을 때 잔액이 0인지 테스트
# def test_initial_change_should_be_zero():
#     m = VendingMachine()
#     assert "잔액은 0원입니다." == run("잔액")
#
#
# #동전을 넣으면 잔액이 잘 뜨는지
# def test_insert_coin_and_check():
#     m = VendingMachine()
#     m.run("동전100")
#     m.run("동전 100")
#     assert "잔액은 200원입니다." == run("잔액")
#
#
# # 누적 금액이 잔액으로 잘 읽히는지
# def test_accumulation_of_change():
#     m = VendingMachine()
#     run("동전 100")
#     run("동전 100")
#     assert "잔액은 200원입니다." == run("잔액")
#
#
#
# def test_command_not_exist_i_dont_know():
#     assert "알 수 없는 명령입니다." == run("콜라 100")
#
# def test_initial_change_should_be_zero():
#     m = VendingMachine()
#     assert "잔액은 0원입니다." == m.run("잔액")
