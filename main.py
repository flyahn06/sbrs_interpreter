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

class ImportException(BaseException):
    pass


def prettify(content: list) -> list:
    # 빈 줄을 지우고 스택을 반전하여 돌려줍니다
    prettified_stack = [command for command in content if not command == ""]
    prettified_stack.append("") # EOF
    prettified_stack.reverse()

    return prettified_stack

def make_stack(rawfile):
    # 실행 스택을 만들어 리턴합니다.
    # 사비루사어는 줄 단위로 실행됩니다.

    raw_stack = rawfile.split("\n")

    return prettify(raw_stack)

def initializer(utilities: list) -> None:
    global saa, bo, util_kkal

    for utility in utilities:
        try:
            module_name = importer[utility]
        except KeyError:
            raise ImportError("{} is not defined.".format(utility))
        else:
            if module_name == "stack_saa":
                saa = importlib.import_module(module_name)
            elif module_name == "stack_bo":
                bo = importlib.import_module(module_name)
            elif module_name == "utility_kkal":
                util_kkal = importlib.import_module(module_name)


def execute(file):
    with open(file, 'r') as f:
        rawfile = f.read()
    
    stack = make_stack(rawfile)
    print(stack)

    # 코드를 전처리 과정과 후처리 과정으로 나눕니다.
    # 전처리 과정에서 예외가 발생가능합니다. 
    preorder = []
    postorder = []

    for command in stack:
        if command.startswith("["):
            match = preorder_regex.match(command)
            import_name = match.group('name')
            preorder.append(import_name)
        else:
            # TODO: 명령은 나중에
            pass
    
    initializer(preorder)


execute("first.sbrs")