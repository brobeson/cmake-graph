"""A unit test for the cmake_graph.target.Target class."""

import os.path
import unittest

import cmake_graph.target as target


class TargetTest(unittest.TestCase):
    """The Target class unit test."""

    def test_init_failure(self):
        """Test that invalid constructor arguments fail to construct a Target
        object.
        """
        # pylint: disable=unused-variable
        with self.assertRaises(ValueError):
            p = target.Target(None, target.LIBRARY_TARGET)
        with self.assertRaises(ValueError):
            p = target.Target("", target.LIBRARY_TARGET)
        with self.assertRaises(ValueError):
            p = target.Target("foo", None)
        with self.assertRaises(ValueError):
            p = target.Target("foo", "")
        with self.assertRaises(ValueError):
            p = target.Target("foo", "not a target type")

    def test_name_property(self):
        """Ensure that Target.name provides the correct value."""
        p = target.Target("King Lear", target.LIBRARY_TARGET)
        self.assertEqual(p.name, "King Lear")

    def test_target_type_property(self):
        """Ensure that Target.target_type provides the correct value."""
        p = target.Target("King Lear", target.LIBRARY_TARGET)
        self.assertEqual(p.target_type, target.LIBRARY_TARGET)


class BuildTargetListTest(unittest.TestCase):
    """The unit tests for cmake_graph.target.build_target_list()."""

    def test_none_input(self):
        """Ensure that None input raises."""
        with self.assertRaises(ValueError):
            target.build_target_list(None)

    def test_empty_input(self):
        """Ensure that an empty list as input raises."""
        with self.assertRaises(ValueError):
            target.build_target_list([])

    def test_nonlist_input(self):
        """Ensure that a non-list input raises."""
        with self.assertRaises(TypeError):
            target.build_target_list("CMakeLists.txt")

    def test_nonstring_input(self):
        """Ensure that a non-string in the input raises."""
        with self.assertRaises(TypeError):
            target.build_target_list(["CMakeLists.txt", 1])

    def test_valid_input(self):
        """Test the function with valid input."""
        pth = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../test_project")
        )
        targets = target.build_target_list([os.path.join(pth, "CMakeLists.txt")])
        self.assertEqual(
            targets,
            [
                target.Target("libFoo", target.LIBRARY_TARGET),
                target.Target("foo", target.EXECUTABLE_TARGET),
            ],
        )
