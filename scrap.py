import requests
from bs4 import BeautifulSoup
import xlsxwriter

class DataScrapping():


    def __init__(self, url, excel_name):

        self.url = url
        self.excel_name = excel_name

    def excel_workbook(self):

        self.workbook1 = xlsxwriter.Workbook(self.excel_name)
        self.worksheet1 = self.workbook1.add_worksheet()

    def web_scrapper(self, query_range = 50):
        try:
            questions = []
            tags_final = []
            col=0
            for i in range(query_range):
                url_new = str(self.url)+str(i)
                response = requests.get(url_new)
                soup = BeautifulSoup(response.text, "html.parser")
                for data in soup.findAll('div',{'class':'question-summary'}):
                    for i in data.findAll('div',{'class':'summary'}):
                        tags = []
                        tags_xl = ""
                        col = col + 1
                        for j in (i.findAll('a', {'class':'post-tag'})):
                            tags_xl=tags_xl+"__label__" + str(j.text) + " "
                            tags.append(j.text)
                        self.worksheet1.write('A' + str(col), tags_xl)
                        self.worksheet1.write('B' + str(col), str(i.text.split("   ")[0]) + " ")
                        questions.append(i.text.split("   ")[0].encode("utf-8"))
                        tags_final.append(tags)
                print (questions)
        finally:
            self.workbook1.close()

obj = DataScrapping("https://quant.stackexchange.com/questions?tab=newest&page=", "test1.xlsx")
obj.excel_workbook()
obj.web_scrapper()