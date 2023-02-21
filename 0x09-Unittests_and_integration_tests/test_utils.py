#!/usr/bin/env python3
"""
Unit test for generic utilities of github org client.
"""

from typing import Any, Dict, Mapping, Sequence
from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """
    Test class to 'access_nested_map' util function

    Args:
        TestCase (TestCase): Unittest TestCase
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        Test the function access_nested_map

        Args:
            nested_map (Mapping): Nested map to test
            path (Sequence): path to test
            expected (Any): Expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test the exceptions of the function access_nested_map

        Args:
            nested_map (Mapping): Nested map to test
            path (Sequence): path to test
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """
    Test class to 'get_json' util function

    Args:
        TestCase (TestCase): Unittest TestCase
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Test get_json util function

        Args:
            test_url (str): Url to test
            test_payload (Dict[str, bool]): Response payload
        """
        with patch('requests.get') as mock_res:
            mock_res.return_value.json = lambda: test_payload
            self.assertEqual(test_payload, get_json(test_url))
            mock_res.assert_called_once()


class TestMemoize(TestCase):
    """
    Test class to 'memoize' util decorator

    Args:
        TestCase (TestCase): Unittest TestCase
    """

    def test_memoize(self) -> None:
        """
        Test memoize functionality of utils
        """
        class TestClass:
            """
            A test class
            """

            def a_method(self) -> int:
                """
                Retrieve a value

                Returns:
                    int: 42
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                'Getter' of a_method using memoization

                Returns:
                    int: 42
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as _mock:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, _mock.return_value)
            self.assertEqual(test_obj.a_property, _mock.return_value)
            _mock.assert_called_once()
