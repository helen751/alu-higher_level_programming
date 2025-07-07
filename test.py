import os

files = {
    "1-my_list.py": '''#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        print(sorted(self))
''',

    "2-is_same_class.py": '''#!/usr/bin/python3
def is_same_class(obj, a_class):
    return type(obj) is a_class
''',

    "3-is_kind_of_class.py": '''#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
''',

    "4-inherits_from.py": '''#!/usr/bin/python3
def inherits_from(obj, a_class):
    return type(obj) is not a_class and isinstance(obj, a_class)
''',

    "5-base_geometry.py": '''#!/usr/bin/python3
class BaseGeometry:
    pass
''',

    "6-base_geometry.py": '''#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
''',

    "7-base_geometry.py": '''#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
''',

    "8-rectangle.py": '''#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
''',

    "9-rectangle.py": '''#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
''',

    "10-square.py": '''#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
''',

    "11-square.py": '''#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
''',

    "100-my_int.py": '''#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, other):
        return int(self) != other
    def __ne__(self, other):
        return int(self) == other
''',

    "101-add_attribute.py": '''#!/usr/bin/python3
def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
''',

    "README.md": "# Python Inheritance Tasks\n\nThis folder contains solutions to the ALX Python Inheritance project tasks.\n\n## Files\n- 1-my_list.py\n- 2-is_same_class.py\n- 3-is_kind_of_class.py\n- 4-inherits_from.py\n- 5-base_geometry.py\n- 6-base_geometry.py\n- 7-base_geometry.py\n- 8-rectangle.py\n- 9-rectangle.py\n- 10-square.py\n- 11-square.py\n- 100-my_int.py\n- 101-add_attribute.py\n"
}

os.makedirs("python-inheritance", exist_ok=True)
for name, code in files.items():
    with open(os.path.join("python-inheritance", name), "w") as f:
        f.write(code)
print("All files created in python-inheritance/")
