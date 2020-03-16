#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county

import openpyxl
import pprint

print('opening the workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active

countyData = {}

print('reading rows...')
for row in range(2, sheet.max_row+1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('writing results...')

resultFile = open('census2010.py', 'w')
resultFile.write('allData=' + pprint.pformat(countyData))
resultFile.close()
print('Done')

jsonFile = open('census2010.json', 'w')
jsonFile.write(pprint.pformat(countyData))
jsonFile.close()
print('Json Done')
