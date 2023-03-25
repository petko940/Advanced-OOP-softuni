class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Petko", 800, 10)

    def test_worker_init(self):
        self.assertEqual(self.worker.name, "Petko")
        self.assertEqual(self.worker.salary, 800)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_worker_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_error_with_raise(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ar:
            self.worker.work()
        self.assertEqual(str(ar.exception), 'Not enough energy.')

    def test_money_increase_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 800)

    def test_energy_decrease_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_method(self):
        result = self.worker.get_info()
        expected = 'Petko has saved 0 money.'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
