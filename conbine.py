import os
import time
from PyPDF2 import PdfFileReader, PdfFileWriter
def getFileName(filedir):

     file_list = [os.path.join(root, filespath) \
                  for root, dirs, files in os.walk(filedir) \
                  for filespath in files \
                  if str(filespath).endswith('pdf')
                  ]
     return file_list if file_list else []

def MergePDF(filepath, outfile):

     output = PdfFileWriter()
     outputPages = 0
     pdf_fileName = getFileName(filepath)

     if pdf_fileName:
         for pdf_file in pdf_fileName:
             print("路径：%s"%pdf_file)

             # 读取源PDF文件
             input = PdfFileReader(open(pdf_file, "rb"))

            # 获得源PDF文件中页面总数
             pageCount = input.getNumPages()
             outputPages += pageCount
             print("页数：%d"%pageCount)

             # 分别将page添加到输出output中
             for iPage in range(pageCount):
                 output.addPage(input.getPage(iPage))

         print("合并后的总页数:%d."%outputPages)
         # 写入到目标PDF文件
         outputStream = open(os.path.join(filepath, outfile), "wb")
         output.write(outputStream)
         outputStream.close()
         print("PDF文件合并完成！")

     else:
         print("没有可以合并的PDF文件！")

 # 主函数
def main():
     file_dir = r'C:\Users\ASUS\Desktop\log' # 存放PDF的原文件夹
     outfile = "Cheat_Sheets.pdf" # 输出的PDF文件的名称
     MergePDF(file_dir, outfile)

main()
