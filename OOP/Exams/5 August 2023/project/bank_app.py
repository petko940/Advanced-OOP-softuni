from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    @property
    def loan_types(self):
        return {
            'StudentLoan': StudentLoan,
            'MortgageLoan': MortgageLoan,
        }

    def add_loan(self, loan_type: str):
        if loan_type not in self.loan_types:
            raise Exception("Invalid loan type!")

        loan = self.loan_types[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    @property
    def client_types(self):
        return {
            'Student': Student,
            'Adult': Adult,
        }

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.client_types:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client = self.client_types[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id][0]

        if (loan_type.startswith('S') and client.__class__.__name__ != 'Student' or
                loan_type.startswith('M') and client.__class__.__name__ != 'Adult'):
            raise Exception("Inappropriate loan type!")

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                client.loans.append(loan)
                self.loans.remove(loan)
                break

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} number_of_changed_loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_income = sum(client.income for client in self.clients)
        loans_count_granted_to_clients = sum(1 for client in self.clients for loan in client.loans)
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = sum(
            client.interest for client in self.clients) / active_clients if active_clients > 0 else 0

        return (f"Active Clients: {active_clients}\n"
                f"Total Income: {total_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
