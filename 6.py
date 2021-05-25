import pdfkit
#pdfkit.from_url('http://google.com', 'out.pdf')



def url_to_pdf():
    url = input("Enter url to download into pdf: ")
    pdf_name = input("Enter name for pdf file: ")
    pdfkit.from_url(url, pdf_name)




   
url_to_pdf()
