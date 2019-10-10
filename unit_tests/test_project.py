"""A unit test for the cmake-graph.project.Project class."""

import unittest

from cmake_graph.project import Project


class ProjectTest(unittest.TestCase):
    """The Project class unit test."""

    def test_init_failure(self):
        """Test that invalid constructor arguments fail to construct a Project
        object.
        """
        # pylint: disable=invalid-name, unused-variable
        with self.assertRaises(ValueError):
            p = Project(None)
        with self.assertRaises(ValueError):
            p = Project("")

    def test_name_property(self):
        """Ensure that Project.name provides the correct value."""
        p = Project("King Lear")
        self.assertEqual(p.name, "King Lear")


if __name__ == "__main__":
    unittest.main()
