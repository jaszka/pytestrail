import openpyxl
from openpyxl import load_workbook

wb = load_workbook(filename = 'Web testrail pack XNET v1.9.xlsx', data_only=True)
sheet = wb['Sections']
premium = sheet['G2':'S53']
mapp = list()
for row in premium:
	try:
		int(row[12].value)
		mapp.append([row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value, row[7].value, row[8].value, row[9].value, row[10].value, row[11].value, row[12].value])
	except :
		continue

print len(mapp)

from testrail import *

client = APIClient('https://testrail')
client.user = 'username'
client.password = 'password'


for t in mapp:
	print "updating case %s"%t
	result = client.send_post(
		'update_case/%s'%(int(t[12])),
		{
			'custom_steps_separated': [
				{"content": "%s"%(t[0]), "expected": ""},
				{"content": "%s"%(t[1]), "expected": ""},
				{"content": "%s"%(t[2]), "expected": ""},
				{"content": "%s"%(t[3]), "expected": ""},
				{"content": "%s"%(t[4]), "expected": ""},
				{"content": "%s"%(t[5]), "expected": ""},
				{"content": "%s"%(t[6]), "expected": ""},
				{"content": "%s"%(t[7]), "expected": ""},
				{"content": "%s"%(t[8]), "expected": ""},
				{"content": "%s"%(t[9]), "expected": ""},
				{"content": "%s"%(t[10]), "expected": ""},
				{"content": "%s"%(t[11]), "expected": ""}
			]
		}
	)
