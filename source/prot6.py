from pypdf import PdfReader
import timeit

start = timeit.timeit()
reader = PdfReader("test3.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"


print(text)
end = timeit.timeit()
print(end - start)
