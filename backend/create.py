from .database import connection
from flask import Flask, render_template, request, redirect, url_for, flash

# @app.route("/create")
def create():
    try:
        conn = connection()
        if request.method == "POST":
            # get data from html
            details = request.form
            username = details['name']
            email = details['email']
            password = details['pass']

            # push data to db
            with conn.cursor() as cur:
                insert = "INSERT INTO `user`(`username`, `password`, `email`) VALUES (%s, %s, %s)"
                cur.execute(insert, (username, password, email))
                conn.commit()
                print("Insert complete")
    # except Exception as e:
    #     return str(e)
    finally:
        print("Database is closed.")
        conn.close()
        flash("Create user is completed!")
        return redirect(url_for('login'))   # return to 'login' function in main.py