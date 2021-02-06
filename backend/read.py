from .database import connection
from flask import render_template, request, redirect, url_for, flash

def read():
    try:
        conn = connection()

        curUSR = conn.cursor()
        curUSR.execute("SELECT `username` FROM `user`")
        curPWD = conn.cursor()
        curPWD.execute("SELECT `password` FROM `user`")
        rowUSR = curUSR.fetchall()
        rowPWD = curPWD.fetchall()
        print(f"fetch all: {rowUSR} AND {rowPWD}")
        print(f"len: {len(rowUSR)}")

        """" Check """
        # for row_usr in range(len(rowUSR)):
        #     print(f"db_username = {rowUSR[row_usr]}")
        # for row_pwd in range(len(rowPWD)):
        #     print(f"db_password = {rowPWD[row_pwd]}")
        """ END Check """

        if request.method == "POST":
            # get data from html
            details = request.form
            username = details['name']
            password = details['pass']
            print(f"get value from html: {username} ,{password}")

            for index in range(len(rowUSR)):
                if username in rowUSR[index] and password in rowPWD[index]:
                    return render_template('index.html')
                else:
                    flash("Username or Password Incorect")
                    return redirect(url_for('login'))

            # --- Stupid ---
            # if username == "alex" and password == "123456":
            #     return render_template('index.html')
            # elif username == "bel" and password == "0123456789":
            #     return render_template('index.html')
            # elif username == "carmel" and password == "753159":
            #     return render_template('index.html')
            # else:
            #     flash("Username or Password Incorect")
            #     return redirect(url_for('login'))
    # except Exception as e:
    #     return "Something was wrong! : " + str(e)
    finally:
        print("Database is closed.")
        conn.close()