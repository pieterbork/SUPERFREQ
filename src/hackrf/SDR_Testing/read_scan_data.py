import sqlite3

bt_out = "/tmp/bt_out.txt"
xbee_out = "/tmp/zb_out.txt"
wifi_out = "/tmp/out_frames"

bt_clean = "bt_clean.txt"
xbee_clean = "xbee_clean.txt"
wifi_clean = "wifi_clean.txt"

db_path = '../../infrastructure/database/SUPERFREQ.db'

#Reads wifi_out file, parses records, returns list
def parse_wifi_records(job_id):
	records = set()
	#Indexes in each record for ssid, mac1, mac2, mac3, freq
	items = [3,5,6,7,8]
	with open(wifi_out) as fh:
		lines = fh.readlines()
		for line in lines:
			record = [job_id]
			parts = line.split(",")
			if len(parts) != 9:
				continue
			for idx,item in enumerate(parts):
				if idx in items:
					val = item.split(": ")[1].strip()
					record.append(val)
			records.add(tuple(record))
	return records

#Reads bt_out file, parses records, returns list
def parse_bt_records(job_id):
	records = set()
	with open(bt_out, 'r') as fh:
		lines = fh.readlines()
	if lines:
		for line in lines:
			parts = line.split()
			if len(parts) != 11:
				continue
			channel = parts[2].replace("Ch", "")
			mac = parts[8].replace("AdvA:", "")
			records.add((job_id, channel, mac))
	return list(records)

#Reads zb_out file, parses records, returns list
def parse_zb_records(job_id):
	records = set()
	with open(xbee_out, 'r') as fh:
		lines = fh.readlines()
	if lines:
		for line in lines:
			parts = line.split()
			if len(parts) != 12:
				continue
			record = (job_id, parts[1], parts[3], parts[5], parts[7], parts[9], parts[11])
			records.add(record)
	return list(records)

#Insert list of wifi records with sqlite
def insert_wifi_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Wifi (job_id, ssid, mac1, mac2, mac3, freq) VALUES (?, ?, ?, ?, ?, ?)", records)

#Insert list of bluetooth records with sqlite
def insert_bt_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Bluetooth (job_id, channel, mac) VALUES (?, ?, ?)", records)

#Insert list of zigbee records with sqlite
def insert_zb_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Zigbee (job_id, src, dst, ext_src, ext_dst, sec_src, sec_dst) VALUES (?, ?, ?, ?, ?, ?, ?)", records)

def insert_job(name):
	if not get_job_id(name):
		with sqlite3.connect(db_path) as conn:
			cursor = conn.cursor()
			cursor.execute("INSERT INTO Jobs (name) VALUES (?)", (name,))

def create_wifi_table():
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Wifi(\
				job_id INTEGER,\
				ssid VARCHAR(120),\
				mac1 VARCHAR(120),\
				mac2 VARCHAR(120),\
				mac3 VARCHAR(120),\
				freq VARCHAR(10),\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_bt_table():
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Bluetooth(\
				job_id integer,\
				channel INT(2),\
				mac VARCHAR(120),\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_zb_table():
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Zigbee(\
				job_id INTEGER,\
				src INT(8),\
				dst INT(8),\
				ext_src VARCHAR(120),\
				ext_dst VARCHAR(120),\
				sec_src VARCHAR(120),\
				sec_dst VARCHAR(120),\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_job_table():
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
				Jobs(\
					id integer primary key,\
					name VARCHAR(120))")

def get_job_id(name):
	job_id = None
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		sql = "SELECT * FROM Jobs WHERE name='{}'".format(name)
		sql_records = cursor.execute(sql)
	records = [record for record in sql_records]
	if len(records) > 0:
		job_id = records[0][0]
	return job_id

#Reads records from table
def get_records_from_table(table):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		sql = "SELECT * FROM {}".format(table)
		sql_records = cursor.execute(sql)
	records = [record for record in sql_records]

	return records

def print_table_columns(table):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		names = list(map(lambda x: x[0], cursor.description))
		print(names)

#Deletes all records from table
def clear_table(table):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		sql = "DELETE FROM {}".format(table)
		cursor.execute(sql)

def delete_table(table):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		sql = "DROP TABLE {}".format(table)
		cursor.execute(sql)

create_job_table()
insert_job("CARLOS_SUCKS")
job_id = get_job_id("CARLOS_SUCKS")
print(job_id)

##Wifi##
create_wifi_table()
clear_table("Wifi")
records = parse_wifi_records(job_id)

insert_wifi_records(records)
records = get_records_from_table("Wifi")
for record in records:
	print(record)

##Bluetooth
create_bt_table()
clear_table("Bluetooth")
records = parse_bt_records(job_id)

insert_bt_records(records)
records = get_records_from_table("Bluetooth")
for record in records:
	print(record)


##Zigbee##
create_zb_table()
clear_table("Zigbee")
records = parse_zb_records(job_id)
insert_zb_records(records)
records = get_records_from_table("Zigbee")
for record in records:
	print(record)

