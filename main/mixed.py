"""

# Multi-Information X Enhanced Dynamic Language


## Introducing MIXED Language

**MIXED Language (Multi-Information X Enhanced Dynamic Language)** is a new programming language which contains features from every programming language that existed today. The MIXED Language allows you to make your programm dynamically. 

The MIXED Language compiler is based on Python 3, which makes it much easier to maintain.

## To Get Started

It is easy to get started with MIXED Lang in case you are specialized in all of the fields listed below:

- Python developing
- C/C++ developing
- Java developing
- HTML developing
- js developing
- PHP developing

If not, you can get started with MIXED Lang with a little bit preparation. You will have to learn some basic stuff by following these steps:

1. Open [Google](https://google.com/) in your browser. (If you're not able to open it, use Bing instead is also OK.)
2. Find an input box in the middle of your screen.
3. Type `How to learn 6 programming languages in a month` and press <kbd>Enter</kbd>
4. Look at the first result and take actions. No matter it seems helpful or not.
5. If you're still looking at this line, please continue learning the listed language. Once you finish learning them, you can continue getting started with MIXED Lang.

### Too busy to prepare by learning 6 languages?

Click [HERE](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Get started with MIXED Lang in only 5 minutes! - YouTube") and get a faster way to get started.

## Usage

As we have told, MIXED Lang's compiler is based on Python 3. So you should use Python 3 to compile your MIXED Lang code with the following command:

```bash
<python | python3> mixed.py <<filename>.mixed>
```


"""

# import types
import os
import inspect
import re
import sys
from typing import SupportsIndex
from typing_extensions import Literal

__filename__ = os.path.abspath(inspect.getframeinfo(inspect.stack()[-1][0])[0])
try:
    using_name = sys.argv[1]
except:
    using_name = None
code_list = []
type_code = '''

class new Type() {
    """Mixed Type"""

    function INIT(cls) {
        cls.__all__ = ['integer', 'string', 'list', 'dictionary']
        cls.__type__ = None
    }

    function type(cls) {
        return print(cls.__type__)
    }
}

class new integer(Type, int) {
    """Integer Type"""

    function INIT(cls) {
        super().INIT()
        cls.__type__ = "<class new type: integer at " + str(id(cls)) + ">"
    }

    function delete(cls) {
        del cls
        return None
    }

    function tobyte(cls) {
        return super().to_bytes()
    }


class new string(Type, str) {
    """String Type"""

    function INIT(cls) {
        super().INIT()
        cls.__type__ = "<class new type: string at " + str(id(cls)) + ">"
    }


class new List(Type, list) {
    """List Type"""

    function INIT(cls) {
        super().INIT()
        cls.__type__ = "<class new type: List at " + str(id(cls)) + ">"
    }
}


class new Tuple(Type, tuple) {
    """Tuple Type"""

    function INIT(cls) {
        super().INIT()
        cls.__type__ = "<class new type: Tuple at " + str(id(cls)) + ">"
    }
}

'''


class MixedError():
    """Call Error"""

    def __init__(self, info, file):
        self.info = info
        self.file = file

    def __str__(self):
        return f"Error in '{self.file}' :\nMixedError: {self.info}"


class Mixed:
    """Mixed language"""

    def __init__(self, file):
        self.file = file
        self.ret_code = ""
        self.variables = {}

    def print(self, *args):
        """print string or others."""
        print(*args)

    def scan(self, prompt):
        """Scan user input"""
        usr = input(prompt)
        return usr

    def parse_mixed_code(self, code: str):
        new_code = type_code
        new_code += code

        new_code = re.sub(r"\bfunction\b", "def", new_code,
                          flags=re.IGNORECASE)  # "function" -> "def"
        new_code = re.sub(r"\bscan\b", "input", new_code,
                          flags=re.IGNORECASE)  # "scan" -> "input"
        new_code = re.sub(r"//", "#", new_code,
                          flags=re.IGNORECASE)  # "//" -> "#"
        new_code = re.sub(r"/\*", "\"\"\"", new_code,
                          flags=re.IGNORECASE)  # "/*" -> """""
        new_code = re.sub(r"\*/", "\"\"\"", new_code,
                          flags=re.IGNORECASE)  # "*/" -> """""
        new_code = re.sub(r"{", "", new_code, flags=re.IGNORECASE)  # "{" -> ""
        new_code = re.sub(r"}", "", new_code, flags=re.IGNORECASE)  # "}" -> ""
        new_code = re.sub(r"\bclass new\b", "class", new_code,
                          flags=re.IGNORECASE)  # "class new" -> "class"
        new_code = re.sub(r"\bINIT\b", "__init__", new_code,
                          flags=re.IGNORECASE)  # "INIT" -> "__init__"
        new_code = re.sub(r"\bcls\b", "self", new_code,
                          flags=re.IGNORECASE)  # "cls" -> "self"
        new_code = re.sub(r"\btrue\b", "True", new_code,
                          flags=re.IGNORECASE)  # "true" -> "True"
        new_code = re.sub(r"\bfalse\b", "False", new_code,
                          flags=re.IGNORECASE)  # "false" -> "False"
        new_code = re.sub(r"\bnone\b", "None", new_code,
                          flags=re.IGNORECASE)  # "none" -> "None"

        # 函数和类定义放在单独的一行中
        pattern_function = r'def\s+(\w+)\s*\(\s*(.*?)\s*\)'
        pattern_class = r'class\s+(\w+)\s*\(\s*(.*?)\s*\)'

        def replace_function(match):
            return f'def {match.group(1)}({match.group(2)}):\n'

        def replace_class(match):
            return f'class {match.group(1)}({match.group(2)}):\n'

        new_code = re.sub(pattern_function, replace_function, new_code)
        new_code = re.sub(pattern_class, replace_class, new_code)

        return new_code

    def execute_mixed_code(self, code):
        """Execute Mixed Code"""
        self.ret_code = self.parse_mixed_code(code)
        code_list.append(self.ret_code)
        self.build(using_name.replace(".mixed", ".py"))

    def execute_mixed_command(self, code):
        """Execute Mixed Code"""
        self.ret_code = self.parse_mixed_code(code)
        return exec(self.ret_code)

    def build(self, fp):
        """Build Code   """
        try:
            os.remove(fp)
        except:
            pass
        with open(fp, "w", encoding="utf-8") as pf:
            pf.write(code_list[0])
        # 使用Pyinstaller进行打包（Mixed“编译”）
        os.system(f'pyinstaller -F --log-level=ERROR -i icon.png {fp}')


mixed = Mixed(__filename__)


def main_file(encode):
    """Main Mixed Build (Open File)"""
    with open(encode, "r", encoding="utf-8") as f:
        code = f.read()
        mixed.execute_mixed_code(code)
    return 0


def main_code(code):
    """Main Mixed Build (Code)"""
    try:
        return mixed.execute_mixed_command(code)
    except Exception as e:
        return e


if __name__ == "__main__":
    main_file(using_name)
