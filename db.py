import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
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
CREATE TABLE IF NOT EXISTS `settings`(
user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
BTCUSDT INTEGER DEFAULT (1),
ETHUSDT INTEGER DEFAULT (0),
TONUSDT INTEGER DEFAULT (0),
SOLUSDT INTEGER DEFAULT (0),
ADAUSDT INTEGER DEFAULT (0),
DOGEUSDT INTEGER DEFAULT (0),
timezone TEXT
)
"""
            )
            self.cur.execute(
                """
CREATE TABLE IF NOT EXISTS `gpt`(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
user_id INTEGER UNIQUE NOT NULL,
version TEXT,
tokens INTEGER DEFAULT (0)
)
"""
            )
            print(self.cur.execute("SELECT * FROM `users`").fetchall(),
                  self.cur.execute("SELECT * FROM `settings`").fetchall(),
                  self.cur.execute("SELECT * FROM `gpt`").fetchall(), 
                  sep="\n")
            return

    def get_db(self):
        with self.conn:
            print(self.cur.execute("SELECT * FROM `users`").fetchall(),
                  self.cur.execute("SELECT * FROM `settings`").fetchall(),
                  self.cur.execute("SELECT * FROM `gpt`").fetchall(), 
                  sep="\n")
            return
    
    def custom(self):
        with self.conn:
            pass

    def user_exists(self, user_id: int):
        with self.conn:
            result = self.cur.execute(
                "SELECT * FROM `users` WHERE `user_id` = ?",
                (user_id,)).fetchmany(1)
            return bool(len(result))
    
    def add_user(self, user_id: int):
        with self.conn:
            self.cur.execute(
                "INSERT INTO `users` (user_id) VALUES (?)",
                (user_id,))
            self.cur.execute(
                "INSERT INTO `settings` (user_id) VALUES (?)",
                (user_id,))
            self.cur.execute(
                "INSERT INTO `gpt` (user_id, version) VALUES (?, ?)",
                (user_id, "gpt-3.5-turbo-0613",))
            return
    
    def get_selectedCryptos(self, user_id: int):
        with self.conn:
            return self.cur.execute(
                "SELECT `BTCUSDT`, `ETHUSDT`, `TONUSDT`, `SOLUSDT`, `ADAUSDT`, `DOGEUSDT` FROM `settings` WHERE `user_id` = ?",
                (user_id,)).fetchall()
    
    def edit_selectedCryptos(self, user_id: int, selCrpt: str, OnOff: bool):
        with self.conn:
            if selCrpt == "BTC" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `BTCUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "BTC" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `BTCUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "ETH" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `ETHUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "ETH" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `ETHUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "TON" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `TONUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "TON" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `TONUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "SOL" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `SOLUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "SOL" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `SOLUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "ADA" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `ADAUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "ADA" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `ADAUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))
            
            if selCrpt == "DOGE" and OnOff == True:
                return self.cur.execute("UPDATE `settings` SET `DOGEUSDT` = ? WHERE `user_id` = ?", ('1', user_id,))
            elif selCrpt == "DOGE" and OnOff == False:
                return self.cur.execute("UPDATE `settings` SET `DOGEUSDT` = ? WHERE `user_id` = ?", ('0', user_id,))

    def add_used_tokens(self, user_id: int, used_tokens: int):
        with self.conn:
            old_used_tokens = self.cur.execute(
                "SELECT `tokens` FROM `gpt` WHERE `user_id` = ?",
                (user_id,)).fetchmany(1)
            
            self.cur.execute(
                "UPDATE `gpt` SET `tokens` = ? WHERE `user_id` = ?",
                ((old_used_tokens[0][0] + used_tokens), user_id,))
            return
    
    def get_used_tokens(self, user_id: int):
        with self.conn:
            return self.cur.execute(
                "SELECT `tokens` FROM `gpt` WHERE `user_id` = ?",
                (user_id,)).fetchmany(1)
    
    def get_model(self, user_id: int):
        with self.conn:
            return self.cur.execute(
                "SELECT `version` FROM `gpt` WHERE `user_id` = ?",
                (user_id,)).fetchmany(1)
    
    def reset_limit(self):
        with self.conn:
            self.cur.execute(
                "UPDATE `gpt` SET `tokens` = 0"
                )
            return
    
    def total_tokens(self, loop_var: int):
        with self.conn:
            return self.cur.execute(
                "SELECT `tokens` FROM `gpt` WHERE `id` = ?",
                (loop_var,)).fetchmany(1)
    
    def total_users(self):
        with self.conn:
            return self.cur.execute(
                "SELECT `id` FROM `gpt`"
            ).fetchall()

    def add_tz(self, tz: str, user_id: int):
        with self.conn:
            try:
                self.cur.execute(
                    "INSERT INTO `settings` `timezone` VALUES (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            except:
                self.cur.execute(
                    "UPDATE `settings` SET `timezone` = (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            return