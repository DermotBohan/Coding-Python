import sys
from termcolor import colored, cprint

text = colored('Hello World!!!!', 'green', attrs = ['reverse','blink'])
print (text)
cprint('Hello Again world!!!', 'yellow', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello World!')
print_red_on_cyan('Hello Universe!')

for i in range(10):
  cprint(i, 'magenta', end = ' ')


cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
