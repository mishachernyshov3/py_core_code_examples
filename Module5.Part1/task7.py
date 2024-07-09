# Реалізувати можливість переходити на попередні та наступні сторінки у веб-браузері.
from collections import deque


backward_history = deque(['New tab page'])
forward_history = deque()


def browse_to(website):
    backward_history.append(website)
    forward_history.clear()


def go_backward():
    if len(backward_history) > 1:
        last_visited_website = backward_history.pop()
        forward_history.append(last_visited_website)


def go_forward():
    if forward_history:
        last_visited_website = forward_history.pop()
        backward_history.append(last_visited_website)


def get_current_website():
    current_website = backward_history.pop()
    backward_history.append(current_website)
    return current_website


browse_to('https://docs.python.org/')
browse_to('https://example.com/')
browse_to('https://google.com/')

print(get_current_website())
