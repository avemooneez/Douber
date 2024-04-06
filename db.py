import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def start(self):
        with self.conn:
            self.cur.execute(
                """
CREATE TABLE IF NOT EXISTS `users`(
user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
IsAdmin INTEGER DEFAULT (0),
IsActive INTEGER DEFAULT (1)
)
"""
            )
            self.cur.execute(
                """
CREATE TABLE IF NOT EXISTS `cryptos`(
user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
BTCUSDT INTEGER DEFAULT (1),
ETHUSDT INTEGER DEFAULT (0),
TONUSDT INTEGER DEFAULT (0),
SOLUSDT INTEGER DEFAULT (0),
ADAUSDT INTEGER DEFAULT (0),
DOGEUSDT INTEGER DEFAULT (0)
)
"""
            )
            print(self.cur.execute("SELECT * FROM `users`").fetchall(), self.cur.execute("SELECT * FROM `cryptos`").fetchall(), sep="\n")
            return

    def get_db(self):
        with self.conn:
            print(self.cur.execute("SELECT * FROM `users`").fetchall(), self.cur.execute("SELECT * FROM `cryptos`").fetchall(), sep="\n")
            return
    
    def user_exists(self, user_id):
        with self.conn:
            result = self.cur.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
    
    def add_user(self, user_id):
        with self.conn:
            self.cur.execute("INSERT INTO `users` (user_id) VALUES (?)", (user_id,))
            self.cur.execute("INSERT INTO `cryptos` (user_id) VALUES (?)", (user_id,))
            return
    
    def get_selectedCryptos(self, user_id):
        with self.conn:
            return self.cur.execute("SELECT `BTCUSDT`, `ETHUSDT`, `TONUSDT`, `SOLUSDT`, `ADAUSDT`, `DOGEUSDT` FROM `cryptos` WHERE `user_id` = ?", (user_id,)).fetchall()
    
    def edit_selectedCryptos(self, user_id, selCrpt: str, OnOff: bool):
        with self.conn:
            if selCrpt == "BTC" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `BTCUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "BTC" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `BTCUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "ETH" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `ETHUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "ETH" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `ETHUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "TON" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `TONUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "TON" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `TONUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "SOL" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `SOLUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "SOL" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `SOLUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "ADA" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `ADAUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "ADA" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `ADAUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "DOGE" and OnOff == True:
                return self.cur.execute("UPDATE `cryptos` SET `DOGEUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "DOGE" and OnOff == False:
                return self.cur.execute("UPDATE `cryptos` SET `DOGEUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
