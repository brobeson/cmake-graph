"""Provides the Target class."""


LIBRARY_TARGET = "library"
EXECUTABLE_TARGET = "executable"
TARGET_TYPES = [LIBRARY_TARGET, EXECUTABLE_TARGET]


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
        if name is None or not name:
            raise ValueError("A target must have a name.")
        if target_type is None or not target_type:
            raise ValueError("A target must have a target type.")
        if target_type not in TARGET_TYPES:
            raise ValueError(f"'{target_type}' is not a valid target type.")
        self.__name = name
        self.__target_type = target_type

    @property
    def name(self):
        """Get the name of this target."""
        return self.__name

    @property
    def target_type(self):
        """Get the type of this target."""
        return self.__target_type
