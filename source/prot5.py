from tika import parser # pip install tika
import timeit

#https://stackoverflow.com/questions/51514246/use-tika-with-python-runtimeerror-unable-to-start-tika-server/53174932#53174932
start = timeit.timeit()
raw = parser.from_file('test3.pdf')
print(raw['content'])
end = timeit.timeit()
print(end - start)
