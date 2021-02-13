import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

# vending machine

class MainWindow(QMainWindow):

    insert_money = 0  # 투입 금액
    choice_price = 0  # 선택한 음료수 값
    current_money = 0  # 현재 남은 금액
    return_money = 0  # 남은 돈 반환
    choice_drinks = ''  # 선택한 음료수
    btns = []  # 음료선택 버튼

    def __init__(self):
        super().__init__()
        loadUi('machine.ui', self)

        # 투입 할 금액 버튼
        self.btn_100.clicked.connect(self.put_money)
        self.btn_500.clicked.connect(self.put_money)
        self.btn_1000.clicked.connect(self.put_money)
        self.btn_10000.clicked.connect(self.put_money)

        # 음료선택 버튼
        self.btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4,
                     self.btn_5, self.btn_6, self.btn_7, self.btn_8]
        for btn in self.btns:
            btn.clicked.connect(self.choice)

        # 남은 돈 반환 버튼
        self.btn_return_money.clicked.connect(self.init)

    # 총 투입한 금액 합산
    def put_money(self):
        sender = self.sender()
        self.insert_money += int(sender.text())
        print(f'Total Money : {self.insert_money}')
        self.lbl_return_money.setText('반환 금: 0')  # 반환 금 초기화
        self.check_money()
        self.btn_on_off()

    # 선택한 음료와 총 가격 합산
    def choice(self):
        sender = self.sender()
        self.choice_price += int(sender.text()[:-1])
        print(f'Total Price : {self.choice_price}')
        self.choice_drinks += sender.toolTip() + " "  # 선택한 음료
        self.lbl_out.setText(self.choice_drinks)  # 선택한 음료 레이블에 표시
        self.check_money()
        self.btn_on_off()

    # 남은 금액 계산 & display
    def check_money(self):
        self.current_money = self.insert_money - self.choice_price
        self.lcdNumber.display(self.current_money)
        print(f'Current Money : {self.current_money}원')

    # 투입한 금액 또는 남은 돈으로 선택 할 수 있는 음료 on/off
    def btn_on_off(self):
        for btn in self.btns:
            if self.current_money >= int(btn.text()[:-1]):
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)

        # 남은 돈이 없으면 버튼 off
        if self.current_money > 0:
            self.btn_return_money.setEnabled(True)
        else:
            self.btn_return_money.setEnabled(False)

    # 남은 돈 반환 후 초기화
    def init(self):
        self.lbl_return_money.setText(f'반환 금: {self.current_money}원')
        print(f'Return Money : {self.current_money}')
        self.insert_money = 0
        self.choice_price = 0
        self.current_money = 0
        self.return_money = 0
        self.lcdNumber.display(self.current_money)
        self.choice_drinks = ''
        self.lbl_out.setText('')
        self.btn_on_off()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    app.exec_()
