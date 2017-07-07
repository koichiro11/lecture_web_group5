# coding: utf-8
"""select from table and insert translated post into the same talbe"""

import mysql.connector
import pandas as pd
import sys
sys.path.append("../translation/")
from utils import * 

if __name__ == "__main__":
	con = mysql.connector.connect(user="root", password="c22h20o13",
								  host="localhost", database="wordpress", charset='utf8')
	select_sql = "SELECT `id`, `post_title`, `post_content` from `wp_posts` WHERE (`post_type` == 'topic' OR `post_type` == 'reply') AND `post_partner` IS NULL;"
	df = pd.read_sql(select_sql, con)
	for index, row in df.iterrows():
		print(row["id"])
		print(row["post_title"])
		print(row["post_content"])

		# 翻訳
		translated_title = tranalte_text_with_model(row["post_title"],"ja", "en")
		translated_content = translate_text_with_model(row["post_content"], "ja", "en")
		print(tralslated_title)

		# TODO(insert)

	
	con.commit()
	con.close()

