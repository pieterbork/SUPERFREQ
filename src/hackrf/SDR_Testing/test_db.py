import db_lib

def test_wifi_operations():
	db_lib.delete_table("Wifi")
	db_lib.create_wifi_table()
	records = db_lib.parse_wifi_records(0, "tmp/out_frames")
	db_lib.insert_wifi_records(records)
	db_records = db_lib.get_records_from_table("Wifi")
	
	
	#Pytest, Assert here
	out_msg = "Wifi: "
	if db_records == records:
		out_msg += "PASS"
	else:
		out_msg += "FAIL"
	print(out_msg)

def test_bt_operations():
	table = "Bluetooth"
	db_lib.delete_table(table)
	db_lib.create_bt_table()
	records = db_lib.parse_bt_records(0, "tmp/bt_out.txt")
	db_lib.insert_bt_records(records)
	db_records = db_lib.get_records_from_table(table)

	#Pytest, Assert here
	out_msg = "Bluetooth: "
	if len(db_records) == len(records):
		out_msg += "PASS"
	else:
		out_msg += "FAIL"
	print(out_msg)

def test_zb_operations():
	table = "Zigbee"
	db_lib.delete_table(table)
	db_lib.create_zb_table()
	records = db_lib.parse_zb_records(0, "tmp/zb_out.txt")
	db_lib.insert_zb_records(records)
	db_records = db_lib.get_records_from_table(table)
	
	out_msg = "Zigbee: "
	if db_records == records:
		out_msg += "PASS"
	else:
		out_msg += "FAIL"
	print(out_msg)
	

test_wifi_operations()	
test_bt_operations()
test_zb_operations()
