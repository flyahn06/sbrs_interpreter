import re
import sys
import importlib
import os

# 현재 디랙터리에 있는 파일을 임포트하기 위함입니다.
sys.path.append(os.getcwd())

# 전처리 부분에서 임포트할 모듈 이름을 찾기 위한 정규식입니다.
preorder_regex = re.compile(r"(\[)(?P<name>.*)(])")
parse_regex = re.compile(r"(?P<statement>[a-z]*) (?P<paramenter>.+)")

# 임포된 모듈 객체가 들어갈 딕셔너리입니다.
# 모듈 이름 (str) : 모듈 객체
modules_dict = {}

# 없는 모듈이 임포트될 때 일어날 예외입니다.
class ImportException(BaseException):
    pass

# 정의되지 않은 명령이 생길 때 일어날 예외입니다.
class UndefinedExecption(BaseException):
    pass

# 빈 줄을 지우는 등 필요없는 요소들을 처리합니다.
def prettify(content: list) -> list:
    # print("prettify called.")
    prettified_stack = [command for command in content if not command == ""]
    # print("Generated prettified_stack:\n{}".format(prettified_stack))

    # print("Returning with prettified_stack.")
    return prettified_stack

# 읽어들인 파일을 기반으로 실행 스택을 만듧니다.
# 사비루사어는 줄 단위로 실행됩니다.
def make_stack(raw_file):
    # print("make_stack called.")
    raw_stack = raw_file.split("\n")
    # print("Generated raw_stack:\n{}".format(raw_stack))

    # print("Returning with prettify with parameter raw_stack.")
    return prettify(raw_stack)

# 전처리 과정으로, 필요한 모듈을 임포트하여 딕셔너리에 집어넣습니다.
def initializer(utilities: list) -> None:
    global modules_dict

    for utility in utilities:
        # print("Getting module {}.".format(utility))
        try:
            module = importlib.import_module(utility)
        except ModuleNotFoundError:
            raise ImportError("{} is not defined.".format(utility))
        else:
            # print("Appending module: key {} value {}.".format(utility, module))
            modules_dict[utility] = module

def parse(stack: list) -> tuple:
    # print("parse called.")
    preprocess = []
    code = []

    for command in stack:
        # print("Command: {}".format(command))
        if command.startswith(";"):
            continue
        if command.startswith("["):
            # print("Starting with [, assuming that it's preprocess step.")
            # 전처리 부분의 명령입니다.
            match = preorder_regex.match(command)
            import_name = match.group('name')
            # print("Appending module {}".format(import_name))
            preprocess.append(import_name)
        else:
            # 일반 구문
            # print("General command.")
            temp = command.split(" ")
            statement = temp[0]

            # 파라미터 있음
            if len(temp) >= 2:
                parameter = tuple(temp[1:])
            else:
                parameter = ""

            # print("Appending command {} with parameter {}.".format(statement, parameter))
            code.append((statement, parameter))

    return preprocess, code

# 메인 실행 함수입니다. 파일이름은 str 형식으로 들어옵니다.
def execute(file: str) -> None:
    # *.sbrs 사비루사어를 읽어들입니다.
    with open(file, 'r') as f:
        rawfile = f.read()

    # print("File content:\n"+rawfile)

    # print("Generating stack, call make_stack with parameter rawfile.")
    # 실행 스택을 만듧니다.
    stack = make_stack(rawfile)

    # 코드를 전처리 과정과 후처리 과정으로 나눕니다.
    # 전처리 과정에서 예외가 발생가능합니다.
    # print("Getting preprocess, code from parse with parameter stack.")
    preprocess, code = parse(stack)

    # 전처리 과정에서 불러와야 하는 모듈을 모두 불러옵니다.
    # print("Initializing...")
    initializer(preprocess)

    # 실제 코드 스택을 반전합니다.
    # code.reverse()
    # ("Reversed code stack.")

    for line in code:
        md = None
        statement = line[0]
        if line[1]:
            parameter = line[1]
        else:
            parameter = ()

        for modulename, realmodule in modules_dict.items():
            # print(modulename)
            # print(realmodule.commandset)
            # print(statement)
            if statement in realmodule.commandset:
                md = realmodule
                # print("command found in the external file {} that has been imported to main.".format(md))
                break
        else:
            raise UndefinedExecption("Interpreter cannot find {}.".format(statement))

        if not parameter:
            # print(f"module.{statement}()")
            exec(f"module.{statement}()", {"module": md})
        else:
            # print(f"module.{statement}(*{parameter})")
            exec(f"module.{statement}(*{parameter})", {"module": md})


execute("first.sbrs")
