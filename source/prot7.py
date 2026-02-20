import fitz # install using: pip install PyMuPDF

import timeit

start = timeit.timeit()
with fitz.open("test3.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)
end = timeit.timeit()
print(end - start)
