from unittest import TestCase
import unittest
from parameterized import parameterized
from main import task_1, task_2, task_3
import parameters_task_1 as pt_1, parameters_task_2 as pt_2, parameters_task_3 as pt_3


class TestTaskFromLessonFour(TestCase):
    @parameterized.expand([(pt_1.test_data, pt_1.expected_data)])
    def test_task_1(self, test_data, expected_data):
        self.assertEqual(task_1(test_data), expected_data)

    @parameterized.expand([(pt_2.test_data, pt_2.expected_data)])
    def test_task_2(self, test_data, expected_data):
        result = task_2(test_data)
        result.sort()
        self.assertEqual(result, expected_data)

    @parameterized.expand([(pt_3.test_data, pt_3.expected_data)])
    def test_task_3(self, test_data, expected_data):
        self.assertEqual(task_3(test_data), expected_data)


if __name__ == '__main__':
    unittest.main()

