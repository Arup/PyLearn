import pdfkit
import requests
from bs4 import BeautifulSoup
import os

os.environ["LANG"] = "en_US.UTF-8"
#config=pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")

def lines():
    filename1="./leetcodedotcomProblems.txt"
    with open(filename1) as f:
        lines = f.readlines()
    return lines


def processLines(lines):
    i=0
    for l in lines:
        l = l.replace("\n", "")
        #resp = requests.get(l).text
        #page=BeautifulSoup(resp,"html.parser" )
        #print(resp)
        #t=str(i)+'.html'
        p=str(i)+'.pdf'
        #soup = BeautifulSoup(t, 'html.parser')
        #with open(t, 'w', encoding='utf-8') as f_out:
        #    f_out.write(page.prettify())
        #pdfkit.from_file(page, p)
        html_to_pdf(l, p)
        #pdfkit.from_file(l, p)
        # pw = PyPDF2(p)
        # pw.setFont("Courier", 10)
        # pw.setHeader("Conversion of HTML text to PDF")
        #
        # # Use method chaining this time.
        # for line in BeautifulSoup(page).get_text().split("\n"):
        #     pw.writeLine(line)
        # pw.savePage()
        # pw.close()
        i=i+1


def html_to_pdf(input,path):
    #pdfkit.from_string(data, "{}.pdf".format(link.split("chooseyourwords")[-1]))
    #pdfkit.from_url(input,path,configuration=config)
    pdfkit.from_url(input, path)


if __name__ == "__main__":
    processLines(lines())
    #eltija()
