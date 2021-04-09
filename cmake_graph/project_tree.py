"""Provide a project tree of CMake targets."""

import cmakeast

class Project:
    def __init__(self, name: str):
        _validate_string_input("name", name)
        self.__name = name

    @property
    def name(self) -> str:
        return __name


def _validate_string_input(variable_name: str, string: str):
    if string is None:
        raise ValueError(f"{variable_name} may not be None")
    if not isinstance(string, str):
        raise TypeError(f"{variable_name} must be a string")
    if string == "":
        raise ValueError(f"{variable_name} may not be an empty string")


class ProjectStack():
    def __init__(self):
        self.__target_stack = []

    def push_project(project_name: str):
        self.__target_stack.append(project_name)

    def pop_project():
        self.__target_stack.pop()

    @property
    def is_empty() -> bool:
        return bool(self.__target_stack)

    @property
    def current_project() -> str:
        return self.__target_stack[-1]


class Parser():
    def __init__(self):
        self.project_stack = ProjectStack()

    def _handle_function_call(name, node, depth):
        name = name.tolower()
        if name == "project":
            self.project_stack.push_project()
        if name == "add_library":
            pass
        elif name == "add_executable":
            pass
        elif name == "add_subdirectory":
            pass
        elif name == "include":
            pass

def parse_project(project_root: str):
    """Read and parse CMake files for a project.

    :param str project_root: The root directory of the project. This directory must contain the
        project's root CMakeLists.txt file.
    """
    project_root = os.path.abspath(os.path.expanduser(project_root))
    ast = _make_ast_from_file(os.path.join(project_root, "CMakeLists.txt"))
    project_stack = ProjectStack()


def _make_ast_from_file(filename: str):
    with open(filename) as cmake_file:
        lines = cmake_file.readlines()
    return cmakeast.ast.parse(lines)


