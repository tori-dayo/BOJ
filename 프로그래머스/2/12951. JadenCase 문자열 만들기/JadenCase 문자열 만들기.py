def solution(s):
    array = s.split(' ')
    result = []
    
    for i in array:
        result.append(i.capitalize())
    
    return ' '.join(result)