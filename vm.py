# change = 0
#
# def init():
#     global change
#     change = 0
#
#
# def run(raw):
#     global change
#
#     tokens = raw.split(" ")
#     # cmd = tokens[0]
#     # params = tokens[1:]
#     cmd, params = tokens[0], tokens[1:]
#     if cmd == "잔액":
#         return "잔액은 " + str(change) + "원입니다."
#     elif cmd == "동전":
#         coin = params[0]
#         # change = int(change) + int(coin)
#         # 밑과 동일
#         change += int(params[0])
#         return coin + "원을 넣었습니다."
#     else:
#         return "알 수 없는 명령입니다."
    # if cmd not in ["동전", "잔액"]:
    #     return "알 수 없는 명령입니다."
    # else:
    #     if cmd == "잔액":
    #         return "잔액은 " + str(change) + "원입니다."
    #     else:
    #         coin = params[0]
    #         # change = int(change) + int(coin)
    #         # 밑과 동일
    #         change += int(params[0])
    #         return coin + "원을 넣었습니다."

class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self, raw):
        tokens = raw.split(" ")
        # cmd = tokens[0]
        # params = tokens[1:]
        cmd, params = tokens[0], tokens[1:]
        print(params)
        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다."
        elif cmd == "동전":
            coin = params[0]
            # change = int(change) + int(coin)
            # 밑과 동일
            self._change += int(params[0])
            return coin + "원을 넣었습니다."
        elif cmd == "음료":
            price = 150
            drink = params[0]
            if self._change >= price:
                self._change -= price
                return drink+"나옴"
            else:
                return "잔액부족"
        else:
            return "알 수 없는 명령입니다."
