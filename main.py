import re
import sys
import importlib
import os

sys.path.append(os.getcwd())

preorder_regex = re.compile(r"(\[)(?P<name>.*)(\])")
command = "[sa_bi_ru_sa]"
importer = {
    "sa_bi_ru_sa": "stack_saa",
    "ju_sae_no_bo": "stack_bot",
    "kkal_kkal_kki_kkol_kkal": "utility_kkal"
}
imported_modules = []

class ImportException(BaseException):
    pass

class UndefinedExecption(BaseException):
    pass


def prettify(content: list) -> list:
    # 빈 줄을 지우고 스택을 반전하여 돌려줍니다
    prettified_stack = [command for command in content if not command == ""]
    prettified_stack.append("") # EOF

    return prettified_stack

def make_stack(rawfile):
    # 실행 스택을 만들어 리턴합니다.
    # 사비루사어는 줄 단위로 실행됩니다.

    raw_stack = rawfile.split("\n")

    return prettify(raw_stack)

def initializer(utilities: list) -> None:
    global stack_saa, stack_bo, utility_kkal, imported_modules

    for utility in utilities:
        try:
            module_name = importer[utility]
        except KeyError:
            raise ImportError("{} is not defined.".format(utility))
        else:
            if module_name == "stack_saa":
                stack_saa = importlib.import_module(module_name)
                imported_modules.append(stack_saa)
            elif module_name == "stack_bo":
                stack_bo = importlib.import_module(module_name)
                imported_modules.append(stack_bo)
            elif module_name == "utility_kkal":
                utility_kkal = importlib.import_module(module_name)
                imported_modules.append(utility_kkal)

def execute(file):
    with open(file, 'r') as f:
        rawfile = f.read()
    
    stack = make_stack(rawfile)
    print(stack)

    # 코드를 전처리 과정과 후처리 과정으로 나눕니다.
    # 전처리 과정에서 예외가 발생가능합니다. 
    preorder = []
    code = []

    for command in stack:
        if command.startswith("["):
            # 전처리 부분의 명령입니다. 
            match = preorder_regex.match(command)
            import_name = match.group('name')
            preorder.append(import_name)
        else:
            code.append(command)
    
    initializer(preorder)

    code.reverse()
    for _ in range(len(code)):
        command = code.pop()
        for module in imported_modules:
            if command in module.commandset:
                exec(f"{module.__name__}.{command}()")



execute("first.sbrs")