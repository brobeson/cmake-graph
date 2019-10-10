"""Provides the Target class."""


LIBRARY_TARGET = "library"
EXECUTABLE_TARGET = "executable"

class Target:
    """Encapsulates a target and its dependencies."""

    def __init__(self, name: str, target_type: str):
        """Construct a Target object.

        :param str name: The target's name. This should not be the alias name
            for a target created within the project, but the actual target name.
        :param str target_type: The type of target. See :ref:TARGET_TYPES for
            acceptable values.
        :raises ValueError: if any of the positional arguments are ``None`` or
            empty strings.
        """

    @property
    def name(self):
        """Get the name of this target."""

    @property
    def target_type(self):
        """Get the type of this target."""
