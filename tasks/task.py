def get_longest_word( s: str) -> str:
    """
     Add your code here
    """
    max_str = ''
    for i in s.split(' '):
        if len(max_str) < len(i):
            max_str = i

    return max_str

get_longest_word('Python is simple and effective!')


