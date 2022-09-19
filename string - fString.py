x = 42
y = 73
print('{} Hello World {}'.format(x, y))
print(f'Hello Universe {x}')

print('{xx} Hello World {bb}'.format(xx=x, bb=y))

print('{1} Hello World {0}'.format(x, y))  # positional arguments
print('{1} Hello World {0} {0} {1}'.format(x, y))


# Formatting Instructions are proceeded by a colon
# Left justified with 5 spaces, Right Justified with 5 spaces and leading zero
print('{1} Hello World {0:<5} {0:>05} {1}'.format(x, y))

# Formatting Instructions are proceeded by a colon
# Left justified with 5 spaces, Right Justified with 5 spaces and leading zero
print('{1} Hello World {0:<5} {0:+05} {1}'.format(x, y))


c = 42 * 747 * 1000
print('The number is  {:,}'.format(c).replace(',', '.'))


c = 42 * 747 * 1000
print('The number is  {:.3f}'.format(c))


# Specify different bases
x = 42
print('The number is {:x}'.format(x))  # hex
print('The number is {:o}'.format(x))  # octal
print('The number is {:b}'.format(x))  # binary
