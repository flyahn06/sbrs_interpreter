import re

preorder_regex = re.compile("([)(?P<name>.*)(])")
command = "[sa_bi_ru_sa]"
match = preorder_regex.search(command)
print(match.group())
exit()

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
            print(preorder_regex.match(command))
        
        
        


execute("first.sbrs")