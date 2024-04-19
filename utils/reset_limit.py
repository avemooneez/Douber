from db import Database
import pymysql
from utils.tokens import host_stat, username, db_name, password
from datetime import datetime
from db import Database

db = Database("./database.db")

def main():
    try:
        conn = pymysql.connect(
            host=host_stat,
            port=3306,
            user=username,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with conn.cursor() as cursor:
                create_template = "CREATE TABLE IF NOT EXISTS `statistics_{}`(id int AUTO_INCREMENT, total_spent int, average_spent int, PRIMARY KEY (id));"

                cursor.execute(
                    create_template.format(
                        datetime.date(datetime.now())
                        )
                )
                total_users = db.total_users()
                total = 0
                for i in range(len(total_users)):
                    total_tokens = db.total_tokens(i+1)
                    total += total_tokens[0][0]
                average = total // len(total_users)
                insert_template = "INSERT INTO `statistics_{date}` (total_spent, average_spent) VALUES ({total}, {average});"
                cursor.execute(insert_template.format(
                    date=datetime.date(datetime.now()),
                    total=total,
                    average=average
                    )
                )                        

        finally:
            conn.commit()
            conn.close()        
    except Exception as e:
        print("ERROR!!", e)

    # reseting limit
    db.reset_limit()
