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
	select_sql = "SELECT `id`, `post_title`, `post_parent`, `post_content`, `post_type` from `wp_posts` WHERE (`post_type` = 'topic' OR `post_type` = 'reply') AND `post_partner` IS NULL ORDER BY `id` ASC;"
	df = pd.read_sql(select_sql, con)
	cursor = con.cursor()
	for index, row in df.iterrows():
		print(row["id"])
		print(row["post_title"])
		print(row["post_content"])

		# 翻訳
		translated_title = translate_text_with_model(row["post_title"],"ja", "en")
		translated_content = translate_text_with_model(row["post_content"], "ja", "en")
		translated_title = translated_title['data']['translations'][0]['translatedText']
		translated_content = translated_content['data']['translations'][0]['translatedText']
		#translated_title = "title"
		#translated_content = "content"
		print(translated_title)

		# TODO(insert)
		parent_sql = "SELECT `id`, `post_parent`, `post_type`, `post_partner` from `wp_posts` WHERE `id` = " + str(row["post_parent"]) + ";"
		df2 = pd.read_sql(parent_sql, con)
		parentpartner = str(df2.ix[0, "post_partner"])
		insert_sql = "INSERT into `wp_posts`(`post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_status`, `comment_status`, `ping_status`, `post_modified`, `post_modified_gmt`, `post_parent`, `post_partner`, `post_type`, `comment_count`) VALUES('2017-07-13 09:00:00', '2017-07-13 00:00:00', '" + str(translated_content) + "', '" + str(translated_title) + "', 'publish', 'closed', 'closed', '2017-07-13 09:00:00', '2017-07-13 00:00:00', " + parentpartner + ", " + str(row["id"]) + ", '" + str(row["post_type"]) + "', 0);"
		#print(insert_sql)
		cursor.execute(insert_sql)
		con.commit()
		partner_sql = "SELECT `id` from `wp_posts` WHERE `post_partner` = " + str(row["id"]) + ";"
		df3 = pd.read_sql(partner_sql, con)
		partner = str(df3.ix[0, "id"])
		update_sql = "UPDATE `wp_posts` SET `post_partner` = " + partner + " WHERE `id` = " + str(row["id"]) + ";"
		#print(update_sql)
		cursor.execute(update_sql)
		con.commit()

	cursor.close()
	con.commit()
	con.close()

