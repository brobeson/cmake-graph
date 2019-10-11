"""A unit test for the cmake-graph.target.Target class."""

import unittest

import cmake_graph.cmake_graph


class CMakeGraphTest(unittest.TestCase):
    """Test cmake_graph main module functions."""

    def test_get_cmake_files(self):
        """Test the function get_cmake_files()."""
        files = cmake_graph.cmake_graph.get_cmake_files("test_project")
        self.assertEqual(sorted(files), ["CMakeLists.txt", "a_script.cmake"])


if __name__ == "__main__":
    unittest.main()
