import unittest
from name_function import get_formatted_name
from name_function2 import get_formatted_name2

class NamesTestCase(unittest.TestCase):
    def test(self):
        format_name=get_formatted_name("zhangsan","lisi")
        print(format_name)
unittest.main()

