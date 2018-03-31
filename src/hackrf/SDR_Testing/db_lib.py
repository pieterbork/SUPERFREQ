import sqlite3
import six
from collections import Counter
from sqlalchemy import Column, Integer, String, ForeignKey

bt_out = "/tmp/bt_out.txt"
xbee_out = "/tmp/zb_out.txt"
wifi_out = "/tmp/out_frames"

db_path = '../../infrastructure/database/SUPERFREQ.db'

class Job(Base):
	__tablename__ = 'jobs'
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	
	def __repr__(self):
		return "<Job(id='{}', name='{}')>".format(self.id, self.name)

class WifiRecord(Base):
	__tablename__ = 'wifi'

	job_id = Column(Integer, ForeignKey('jobs.id'))
	ssid = Column(String)
	mac1 = Column(String)
	mac2 = Column(String)
	mac3 = Column(String)
	freq = Column(String)
	count = Column(Integer)
	
	def __repr__(self):
		return "<WifiRecord(job_id='{}', ssid='{}', mac1='{}', mac2='{}', mac3='{}', freq='{}', count='{}')>".format(self.job_id, self.ssid, self.mac1, self.mac2, self.mac3, self.freq, self.count)

class BTRecord(Base):
	__tablename__ = "bluetooth"
	
	job_id = Column(Integer, ForeignKey('jobs.id'))
	channel = Column(Integer)
	mac = Column(String)
	count = Column(Integer)

	def __repr__(self):
		return "<BTRecord(job_id='{}', channel='{}', mac='{}', count='{}')>".format(self.job_id, self.channel, self.mac, self.count)

class ZBRecord(Base):
	__tablename__ = "zigbee"	
	
	job_id = Column(Integer, ForeignKey('jobs.id'))
	src = Column(Integer)
	dst = Column(Integer)
	ext_src = Column(String)
	ext_dst = Column(String)
	sec_src = Column(String)
	sec_dst = Column(String)
	count = Column(Integer)

	def __repr__(self):
		return "<ZBRecord(job_id='{}', src='{}', dst='{}', ext_src='{}', ext_dst='{}', sec_src='{}', sec_dst='{}', count='{}')>".format(self.job_id, self.src, self.dst, self.ext_src, self.ext_dst, self.sec_src, self.sec_dst, self.count)
	

#Reads wifi_out file, parses records, returns list
def parse_wifi_records(job_id):
	records = []
	#Indexes in each record for ssid, mac1, mac2, mac3, freq
	items = [3,5,6,7,8]
	fields = ["ssid", "mac1", "mac2", "mac3", "freq"]
	with open(wifi_out) as fh:
		lines = fh.readlines()
		for line in lines:
			record = {"job_id": job_id}
			parts = line.split(",")
			if len(parts) != 9:
				continue
			for key, value in parts:
				key = key.strip().lower().replace(" ", "")
				if key in fields:
					record[key] = value
			records.append(record)
	counts = Counter(records)
	print(counts)
	return [record.update({"count": "1"}) for record in set(records)]

#Reads bt_out file, parses records, returns list
def parse_bt_records(job_id):
	records = []
	with open(bt_out, 'r') as fh:
		lines = fh.readlines()
	if lines:
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
def parse_zb_records(job_id):
	records = []
	with open(xbee_out, 'r') as fh:
		lines = fh.readlines()
	if lines:
		for line in lines:
			parts = line.split()
			if len(parts) != 12:
				continue
			record = (job_id, parts[1], parts[3], parts[5], parts[7], parts[9], parts[11])
			records.append(record)
	counts = Counter(records)
	return [tuple(list(record) + [counts[record]]) for record in set(records)]

#Insert list of wifi records with sqlite
def insert_wifi_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Wifi (job_id, ssid, mac1, mac2, mac3, freq, count) VALUES (?, ?, ?, ?, ?, ?, ?)", records)

#Insert list of bluetooth records with sqlite
def insert_bt_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Bluetooth (job_id, channel, mac, count) VALUES (?, ?, ?, ?)", records)

#Insert list of zigbee records with sqlite
def insert_zb_records(records):
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.executemany("INSERT INTO Zigbee (job_id, src, dst, ext_src, ext_dst, sec_src, sec_dst, count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", records)

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
				count INTEGER,\
				FOREIGN KEY(job_id) REFERENCES Jobs(id))")

def create_bt_table():
	with sqlite3.connect(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS\
			Bluetooth(\
				job_id INTEGER,\
				channel INT(2),\
				mac VARCHAR(120),\
				count INTEGER,\
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
				count INTEGER,\
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

records = parse_wifi_records(1)
print(records)
