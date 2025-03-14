def solution(s):
    array = list(map(int,s.split(' ')))
    a = f'{min(array)} {max(array)}'
    return a