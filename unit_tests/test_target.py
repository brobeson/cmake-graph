"""A unit test for the cmake-graph.target.Target class."""

import unittest

from cmake_graph.target import Target, LIBRARY_TARGET


class TargetTest(unittest.TestCase):
    """The Target class unit test."""

    def test_init_failure(self):
        """Test that invalid constructor arguments fail to construct a Target
        object.
        """
        # pylint: disable=unused-variable
        with self.assertRaises(ValueError):
            p = Target(None, LIBRARY_TARGET)
        with self.assertRaises(ValueError):
            p = Target("", LIBRARY_TARGET)
        with self.assertRaises(ValueError):
            p = Target("foo", None)
        with self.assertRaises(ValueError):
            p = Target("foo", "")
        with self.assertRaises(ValueError):
            p = Target("foo", "not a target type")

    def test_name_property(self):
        """Ensure that Target.name provides the correct value."""
        p = Target("King Lear", LIBRARY_TARGET)
        self.assertEqual(p.name, "King Lear")

    def test_target_type_property(self):
        """Ensure that Target.target_type provides the correct value."""
        p = Target("King Lear", LIBRARY_TARGET)
        self.assertEqual(p.target_type, LIBRARY_TARGET)


if __name__ == "__main__":
    unittest.main()
