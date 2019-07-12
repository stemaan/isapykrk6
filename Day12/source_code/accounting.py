class Account:
    def __init__(self, holder_name, bank):
        self.account_holder = holder_name
        self.bank = bank
        self.funds = 0

    def withdraw(self, amount):
        if self.funds >= amount:
            self.funds -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.funds += amount

    def transfer_money(self, amount, other_account):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True, amount
        else:
            return False, amount

    def get_balance(self):
        return f'{self.funds}'


class AccountWithPromo(Account):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.FIXED_PROMO_RATE = 0.1

    def deposit(self, amount):
        extra_funds = amount * self.FIXED_PROMO_RATE
        super().deposit(amount + extra_funds)


class AccountWithFee(Account):
    WITHDRAW_FEE = 0.01

    def withdraw(self, amount):
        super().withdraw(amount)
        self.funds -= amount * self.WITHDRAW_FEE


class ATM:
    def __init__(self, account: Account):
        self.account = account

    def withdraw(self, amount):
        return self.account.withdraw(amount)

    def deposit(self, amount):
        self.account.deposit(amount)

    def get_balance(self):
        return self.account.get_balance()


if __name__ == '__main__':
    basic_account = Account('Jan kowalski', 'basic bank')
    promo_account = AccountWithPromo('Adam Nowak', 'promo bank')
    expensive_account = AccountWithFee('Adam Nowak', 'greedy bank')
    atm = ATM(basic_account)
    #
    # print(basic_account.get_balance())
    # print(promo_account.get_balance())
    #
    # amount_to_deposit = 100
    #
    # basic_account.deposit(amount_to_deposit)
    # promo_account.deposit(amount_to_deposit)
    #
    # print(basic_account.get_balance())
    # print(promo_account.get_balance())
    #
    # result = atm.withdraw(50)
    # print(result)
    # print(atm.get_balance())
    print(expensive_account.WITHDRAW_FEE)
    # TO NIE ZADZIALA!
    expensive_account.WITHDRAW_FEE = 10
    print(expensive_account.WITHDRAW_FEE)
