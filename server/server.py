#!/usr/bin/env python2

import sys
import time
import threading
import sqlite3
import json

def initialize_db():
	con = sqlite3.connect('chat.db')
	cur = con.cursor()
	cur.execute("""
	CREATE TABLE IF NOT EXISTS chat (
	  id INTEGER PRIMARY KEY,
	  message TEXT,
	  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
	)""")
	return con, cur

def input_thread():
	while True:
		con, cur = initialize_db()

		text = raw_input()

		cur.execute("INSERT INTO chat (message) VALUES (?)", (text,))
		con.commit()

		con.close()

		time.sleep(0.1)

def output_thread():
	last_seen_id = -1
	while True:
		con, cur = initialize_db()

		cur.execute("SELECT id, message FROM chat WHERE id > ? ORDER BY id", (last_seen_id,))
		records = cur.fetchall()

		if records:
			last_seen_id = records[-1][0]
			messages = [rec[1] for rec in records]

			print json.dumps(messages)
			sys.stdout.flush()

		con.close()

		time.sleep(0.1)

t_input = threading.Thread(target=input_thread)
t_output = threading.Thread(target=output_thread)

t_input.start()
t_output.start()

t_input.join()
t_output.join()
