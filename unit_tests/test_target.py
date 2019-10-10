"""A unit test for the cmake-graph.target.Target class."""

import unittest

from cmake_graph.target import Target


class TargetTest(unittest.TestCase):
    """The Target class unit test."""

    def test_init_failure(self):
        """Test that invalid constructor arguments fail to construct a Target
        object.
        """
        # pylint: disable=unused-variable
        with self.assertRaises(ValueError):
            p = Target(None)
        with self.assertRaises(ValueError):
            p = Target("")

    def test_name_property(self):
        """Ensure that Target.name provides the correct value."""
        p = Target("King Lear")
        self.assertEqual(p.name, "King Lear")


if __name__ == "__main__":
    unittest.main()
