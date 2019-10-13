"""Provides the Target class and related functionality."""


EXECUTABLE_TARGET = "executable"
"""Represents a CMake executable target, created by the ``add_executable()`` command."""

LIBRARY_TARGET = "library"
"""Represents a CMake library target, created by the ``add_library()`` command."""

TARGET_TYPES = [LIBRARY_TARGET, EXECUTABLE_TARGET]
"""A list of valid target types.

This is a convenience to determine if a target type variable is valid.

.. code-block:: python

    tt = "alias"
    tt in cmake_graph.target.TARGET_TYPES

"""


class Target:
    """Encapsulates a target and its dependencies."""

    def __init__(self, name: str, target_type: str):
        """
        :param str name: The target's name. This should not be the alias name
            for a target created within the project, but the actual target name.
        :param str target_type: The type of target. See `Module Data`_ for
            acceptable values.
        :raises ValueError: if any of the positional arguments are ``None`` or
            empty strings.
        """
        if name is None or not name:
            raise ValueError("A target must have a name.")
        if target_type is None or not target_type:
            raise ValueError("A target must have a target type.")
        if target_type not in TARGET_TYPES:
            raise ValueError(f"'{target_type}' is not a valid target type.")
        self.__name = name
        self.__target_type = target_type

    @property
    def name(self) -> str:
        """
        :property:
        :returns: The name of this target.
        :rtype: str
        """
        return self.__name

    @property
    def target_type(self) -> str:
        """
        :property:
        :returns: The type of this target.
        :rtype: str
        """
        return self.__target_type
