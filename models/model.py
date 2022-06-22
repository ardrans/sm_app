import pymysql
from connector import mysql

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)


def match_credentials(username, password):
    sql_query = "SELECT * FROM Users WHERE username ='%s' AND password ='%s'" % (username, password)
    cursor.execute(sql_query)
    return cursor.fetchone()


def insert_token(user_id, access_token, refresh_token):
    retry_count = 0
    while True:
        try:
            sql_query = "INSERT INTO auth (user_id, access_token, refresh_token) VALUES(%s, %s, %s)"
            data = (user_id, access_token, refresh_token)
            cursor.execute(sql_query, data)
            conn.commit()
            return True
        except Exception as err:
            retry_count = retry_count + 1
            if retry_count > 3:
                raise Exception('Token insertion failed')
            print(err)

# def users():
#     try:
#         cursor.execute("SELECT email FROM Users")
#         emails = cursor.fetchall()
#         response = jsonify(emails)
#         return response
#     except Exception as e:
#         print(e)

def create_user(name,email,password, confirm_password, dob):
    try:
        sqlQuery = "INSERT INTO Users(Name, email, password,confirm_password, dob) VALUES(%s, %s, %s, %s, %s)"
        Data = (name, email, password, confirm_password, dob)
        cursor.execute(sqlQuery, Data)
        conn.commit()
    except Exception as e:
        print(e)
def status_update(id):
    sql_query = "UPDATE `Users` SET `status` = '1' WHERE `Users`.`id` = %s" % (id)
    cursor.execute(sql_query)
    conn.commit()
    return True








