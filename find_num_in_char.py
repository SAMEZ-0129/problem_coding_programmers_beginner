words = 'asds123lk1n2424k2242lllksd'
word_list = list(words)
a = int(''.join(word_list[4:7]))
print(a, type(a))

import re
x = [int(s) for s in re.findall(r'\d+', "aAb1B2cC34oOp")]
print(x)