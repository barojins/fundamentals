class Bank:
    def __init__(self):
        self.balance = {}

    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.balance:
            return False
        self.balance[account_id] = 0
        pass

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        pass

    def transfer(self, timestamp: int, source_id: str, target_id: str, amount: int) -> bool:
        pass

    def schedule_payment(self, timestamp: int, source_id: str, target_id: str, amount: int, delay: int) -> str | None:
        pass

    def cancel_payment(self, timestamp: int, account_id: str, payment_id: str) -> bool:
        pass

    def get_top_spenders(self, timestamp: int, n: int) -> list[str]:
        pass