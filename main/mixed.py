import os
import inspect
import traceback
import re
import sys

__filename__ = os.path.abspath(inspect.getframeinfo(inspect.stack()[-1][0])[0])
using_name = sys.argv[1]
code_list = []


class MixedError:
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
        self.variables = {}

    def print(self, *args):
        """print string or others."""
        print(*args)

    def scan(self, prompt):
        """Scan user input"""
        usr = input(prompt)
        return usr

    def parse_mixed_code(self, code: str):
        new_code = code.replace("function", "def")
        new_code = new_code.replace("//", "#")
        new_code = new_code.replace("{", "")
        new_code = new_code.replace("}", "")
        pattern = r'def\s+\w+\s*\(\s*.*?\s*\)'
        new_code = re.sub(pattern, lambda x: x.group(0)[:-1] + "): ", new_code)
        print(new_code)
        code_list.append(new_code)
        return new_code

    def execute_code(self, code):
        exec(code, globals(), self.variables)

    def execute_function(self, func_name):
        if func_name in self.variables:
            self.variables[func_name]()
        else:
            raise MixedError(f"Function '{func_name}' not found", self.file)

    def execute_mixed_code(self, code):
        self.build(using_name.replace(".mixed", ".py"))

    def build(self, fp):
        try:
            os.remove(fp)
        except:
            pass
        with open(fp, "w", encoding="utf-8") as pf:
            pf.write(code_list[0])
        # 使用Pyinstaller进行打包（Mixed编译）
        os.system(f'pyinstaller -F --log-level=ERROR -i icon.png {fp}')


def main(code):
    f = open(code, encoding="utf-8")
    data = f.read()
    try:
        mixed.execute_mixed_code(data)
    except (NameError, AttributeError) as e:
        tb = traceback.extract_tb(e.__traceback__)[-1]
        error_file = os.path.abspath(__filename__)
        return MixedError("Unknown Error", error_file)
    finally:
        f.close()


mixed = Mixed(__filename__)

if __name__ == "__main__":  # test
    code = open(using_name, encoding="utf-8")
    f = code.read()
    result = main(using_name)
    if isinstance(result, MixedError):
        mixed.print(result)
    code.close()
