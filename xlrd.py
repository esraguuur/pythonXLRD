
import xlrd

dosya="not.xlsx"

inputWorkbook=xlrd.open_workbook(dosya)
inputWorkSheet = inputWorkbook.sheet_by_index(0)

harfler =[]
notlar = []

for x in range(1,inputWorkSheet.nrows):
    harfler.append(inputWorkSheet.cell_value(x,0))
    notlar.append(int(inputWorkSheet.cell_value(x,1)))

print(harfler)
print(notlar)