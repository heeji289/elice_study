import re


def solution(files):
    def mysplit(x):
        # 소문자로 변경
        x = str.lower(x)
        # 정규식으로 HEAD, NUMBER, TAIL쪼갬
        r = re.compile(r"[0-9]+")
        result = re.search(r, x)
        return [x[:result.start()], x[result.start():result.end()], x[result.end():]]

    # 소문자로 변경 및 HEAD, NUMBER, TAIL로 쪼갬
    change_files = list(enumerate(map(lambda x: mysplit(x), files)))

    # 먼저 HEAD부분으로 사전 순 정렬 => NUMBER순으로 정렬 => 주어진 순서대로 정렬
    sorted_files = sorted(change_files, key=lambda x: (x[1][0], int(x[1][1])))
    # 정렬한 파일에서 index만 뽑아와 files에서 찾아옴.
    answer = list(map(lambda x: files[x[0]], sorted_files))

    return answer
