from testrail import *

run_no = raw_input('Enter run')
case_no = raw_input('Enter case no')
result = client.send_post(
	'add_result_for_case/%s/%s'%(int(run_no),int(case_no)),
	{ 'status_id': 4, 'comment': 'This test worked fine!' }
)
