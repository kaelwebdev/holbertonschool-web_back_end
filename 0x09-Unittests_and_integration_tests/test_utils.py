#!/usr/bin/env python3
"""
Tests for utils
"""

from unittest import TestCase
from parameterized import parameterized
from utils import requests, get_json, access_nested_map, memoize


class TestAccessNestedMap(TestCase):
    """ Test cases for utils.test_access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, values, path, expected):
        """
        Testing return
        """
        r = access_nested_map(values, path)
        self.assertEqual(r, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, values, path, expected):
        """
        Testing errors
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(values, path)
            self.assertEqual(expected, str(e.exception))
