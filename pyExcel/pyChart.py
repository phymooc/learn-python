import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1,11):
  sheet['A'+str(i)] = i


# create reference obj
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# create series obj
seriesObj = openpyxl.chart.Series(refObj, title='chart title')

# create chart obj
chartObj = openpyxl.chart.BarChart()

chartObj.title = 'my chart'

# append seriesObj to chartObj
chartObj.append(seriesObj)

# add chart Obj to worksheet obj
sheet.add_chart(chartObj,'C3')
wb.save('sampleChart.xlsx')
