from testrail import *

case_no = raw_input('Enter case no')
result = client.send_post(
	'update_case/%s'%(int(case_no)),
	{
		'custom_steps_separated': [[3]
			{ "content": "Premium Exc IPT: 200.00 \n Premium Inc IPT: 219.00", "expected": "Hey ho"}
		]
	}

)
