import textract
import timeit

start = timeit.timeit()
text = textract.process("test3.pdf")
print(text)
end = timeit.timeit()
print(end - start)
