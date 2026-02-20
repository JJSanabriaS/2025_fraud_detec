import pypdf
import timeit

start = timeit.timeit()
reader = PyPDF2.PdfReader('test3.pdf')
for page in reader.pages:
    print(page.extract_text())

end = timeit.timeit()
print(end - start)
