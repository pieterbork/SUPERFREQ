import sqlite3
import six
from collections import Counter

bt_out = "/tmp/bt_out.txt"
zb_out = "/tmp/zb_out.txt"
wifi_out = "/tmp/out_frames"

db_path = 'SUPERFREQ.db'

#Reads wifi_out file, parses records, returns list
def parse_wifi_records(job_id, fp=None):
	records = []
	fp = wifi_out if fp is None else fp
	try:
		with open(fp) as fh:
			lines = fh.readlines()
	except:
		return []
	#Indexes in each record for ssid, mac1, mac2, mac3, freq
	items = [3,5,6,7,8]
	for line in lines:
		record = [job_id]
		parts = line.split(",")
		if len(parts) != 9:
			continue
		for idx,item in enumerate(parts):
			if idx in items:
				val = item.split(": ")[1].strip()
				record.append(val)
		records.append(tuple(record))
	counts = Counter(records)
	return [tuple(list(record) + [counts[record]]) for record in set(records)]

#Reads bt_out file, parses records, returns list
def parse_bt_records(job_id, fp=None):
	records = []
	fp = bt_out if fp is None else fp
	try:
		with open(fp, 'r') as fh:
			lines = fh.readlines()
	except:
		return []
	for line in lines:
		parts = line.split()
		if len(parts) != 11:
			continue
		channel = parts[2].replace("Ch", "")
		mac = parts[8].replace("AdvA:", "")
		records.append((job_id, channel, mac))
	counts = Counter(records)
	return [tuple(list(record) + [counts[record]]) for record in set(records)]

#Reads zb_out file, parses records, returns list
def parse_zb_records(job_id, fp=None):
	records = []
	fp = zb_out if fp is None else fp
	try:
		with open(fp, 'r') as fh:
			lines = fh.readlines()
	except:
		return []
	for line in lines:
		parts = [part.strip(",") for part in line.split() if "src" not in part and "dst" not in part]
		if len(parts) != 6:
			continue
		record = tuple([job_id] + parts)
		records.append(record)
	counts = Counter(records)
	return [tuple(list(record) + [counts[record]]) for record in set(records)]

def get_db_conn():
	return sqlite3.connect(db_path)

#Insert list of wifi records with sqlite
def insert_wifi_records(records):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Wifi (job_id, ssid, mac1, mac2, mac3, freq, count) VALUES (?, ?, ?, ?, ?, ?, ?)", records)

#Insert list of bluetooth records with sqlite
def insert_bt_records(records):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Bluetooth (job_id, channel, mac, count) VALUES (?, ?, ?, ?)", records)

#Insert list of zigbee records with sqlite
def insert_zb_records(records):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Zigbee (job_id, src, dst, ext_src, ext_dst, sec_src, sec_dst, count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", records)

def insert_job(name):
	if not get_job_id(name):
		with get_db_conn() as conn:
			cursor = conn.cursor()
			cursor.execute("INSERT INTO Jobs (name) VALUES (?)", (name,))

def create_wifi_table():
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Wifi(\
				job_id INTEGER,\
				ssid VARCHAR,\
				mac1 VARCHAR,\
				mac2 VARCHAR,\
				mac3 VARCHAR,\
				freq VARCHAR,\
				count INTEGER,\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_bt_table():
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Bluetooth(\
				job_id INTEGER,\
				channel INTEGER,\
				mac VARCHAR,\
				count INTEGER,\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_zb_table():
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Zigbee(\
				job_id INTEGER,\
				src INTEGER,\
				dst INTEGER,\
				ext_src VARCHAR,\
				ext_dst VARCHAR,\
				sec_src VARCHAR,\
				sec_dst VARCHAR,\
				count INTEGER,\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_job_table():
	with get_db_conn() as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
				Jobs(\
					id integer primary key,\
					name VARCHAR)")

def get_job_id(name):
	job_id = None
	with get_db_conn() as conn:
		cursor = conn.cursor()
		sql = "SELECT * FROM Jobs WHERE name='{}'".format(name)
		sql_records = cursor.execute(sql)
	records = [record for record in sql_records]
	if len(records) > 0:
		job_id = records[0][0]
	return job_id

#Reads records from table
def get_records_from_table(table, job_id=None):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		sql = "SELECT * FROM {}".format(table)
		if job_id:
			sql += " WHERE job_id={}".format(job_id)
		try:
			sql_records = cursor.execute(sql)
		except:
			return []
	records = [record for record in sql_records]

	return records

def print_table_columns(table):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		names = list(map(lambda x: x[0], cursor.description))
		print(names)

#Deletes all records from table
def clear_table(table):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		sql = "DELETE FROM {}".format(table)
		cursor.execute(sql)

def delete_table(table):
	with get_db_conn() as conn:
		cursor = conn.cursor()
		sql = "DROP TABLE IF EXISTS {}".format(table)
		cursor.execute(sql)

