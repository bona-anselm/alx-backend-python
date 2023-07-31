#!/usr/bin/env python3
""" Defines test class for utils.access_nested_map function """
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ Provides functionality for testing utils.access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]
                               ) -> None:
        """ Performs unit tests on utils.access_nested_map """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
