import pymysql
import random, string
from app import app
from connector import mysql
from flask import jsonify
from flask import flash, request

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)


@app.route('/create', methods=['POST'])
def create_user():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        json = request.json
        name = json['Name']
        username = json['username']
        password = json['password']
        dob = json['dob']

        #conn = mysql.connect()
        #cursor = conn.cursor(pymysql.cursors.DictCursor)
        if name and username and password and dob and request.method == 'POST':
            #conn = mysql.connect()
            #cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO Users(Name, username, password, dob) VALUES(%s, %s, %s, %s)"
            Data = (name, username, password, dob)
            cursor.execute(sqlQuery, Data)
            conn.commit()
            response = jsonify('User added successfully!')
            response.status_code = 200
            return response
        else:
            return jsonify('Something went wrong')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users')
def users():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        #conn = mysql.connect()
        #cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, username, password, dob, status FROM Users")
        all_users = cursor.fetchall()
        response = jsonify(all_users)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/login', methods=['POST'])
def user_login():
    try:
        json = request.json
        username = json['username']
        password = json['password']
        if username and password:
            sql_query = "SELECT * FROM Users WHERE username ='%s' AND password ='%s'" % (username, password)
            cursor.execute(sql_query)
            user = cursor.fetchall()
            if user:
                acess_token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(128))

                refresh_token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
                sqlQuery = "INSERT INTO auth (user_id, acess_token, refresh_token) VALUES(%s, %s, %s)"
                Data = (user[0]["id"] , acess_token, refresh_token)
                cursor.execute(sqlQuery, Data)
                conn.commit()
                return jsonify({"acess_token":acess_token,'refresh_token':refresh_token})
            else:
                return jsonify({"message":"Invalid username or password0"})
        else:
            return jsonify({"message":"Invalid username or password1"})
    except Exception as e:
        print(e)
        return jsonify({"message":"Invalid username or password123"})
    # finally:
    #     cursor.close()
    #     conn.close()
    #     return jsonify({"message":"Invalid username or password123"})




if __name__ == "__main__":
    app.run()