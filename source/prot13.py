import tabula

import timeit

start = timeit.timeit()
df = tabula.read_pdf('test3.pdf')

df
end = timeit.timeit()
print(end - start)
