from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    @property
    def types_waiters(self):
        return {
            "FullTimeWaiter": FullTimeWaiter,
            "HalfTimeWaiter": HalfTimeWaiter
        }

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.types_waiters:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."

        waiter = self.types_waiters[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    @property
    def types_clients(self):
        return {
            "RegularClient": RegularClient,
            "VIPClient": VIPClient
        }

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.types_clients:
            return f"{client_type} is not a recognized client type."

        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."

        client = self.types_clients[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = [w for w in self.waiters if w.name == waiter_name][0]
            return waiter.report_shift()

        except IndexError:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = [c for c in self.clients if c.name == client_name][0]
            earned_points = client.earning_points(order_amount)
            return f"{client_name} earned {earned_points} points from the order."
        except IndexError:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        client = [c for c in self.clients if c.name == client_name]
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        client = client[0]
        discount = client.apply_discount()
        return f"{client_name} received a {discount[0]}% discount. Remaining points {client.points}"

    def generate_report(self):
        total_earnings = sum([c.calculate_earnings() for c in self.waiters])
        total_client_points = sum([c.points for c in self.clients])
        clients_count = len(self.clients)

        output = [f"""$$ Monthly Report $$
Total Earnings: ${total_earnings:.2f}
Total Clients Unused Points: {total_client_points}
Total Clients Count: {clients_count}
** Waiter Details **"""]

        for waiter in sorted(self.waiters, key=lambda x: x.calculate_earnings(), reverse=True):
            output.append(str(waiter))

        return "\n".join(output)
