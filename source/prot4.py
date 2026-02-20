from tika import parser # pip install tika

import timeit
start = timeit.timeit()
raw = parser.from_file('test3.pdf')
print(raw['content'])
end = timeit.timeit()
print(end - start)
