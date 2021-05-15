
def get_summ(one, two, delimiter='&'):
    summ = str(one)+str(delimiter)+str(two)
    return summ

assert get_summ('Learn', 'Python', delimiter=' ') == 'Learn Python'
assert get_summ('Learn', 'python', delimiter=' ') == 'Learn python'
assert get_summ('1', '1', delimiter='+') == '1+1'
assert get_summ('Batman', 'Robin') == 'Batman&Robin'

print(get_summ("learn","python", delimiter=' ').upper())


def format_price(price):
    return int(price)

real_price = format_price(56.54)
print(f"Цена: {real_price} руб.")