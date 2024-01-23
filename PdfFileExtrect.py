import PyPDF2
a=PyPDF2.PdfReader('Check.pdf')

#print(a.getDocumentInfo())
print(a.metadata)

#print(a.getNumPages())
print(len(a.pages))

#print(a.pages[2].extract_text())

str=" "
for i in range(0,len(a.pages)):
    str+=(a.pages[i].extract_text())

with open("Check_Doc.txt","w") as file:
    file.write(str)
