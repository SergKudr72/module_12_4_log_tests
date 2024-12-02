import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            rw = Runner("man", -6)
            for i in range(10):
                rw.walk()
            self.assertEqual(rw.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            rr = Runner(213, 3)
            for i in range(10):
                rr.run()
            self.assertEqual(rr.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)



if __name__ == "__main__":
     unittest.main()