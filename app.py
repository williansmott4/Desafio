from flask import Flask, render_template, url_for, request, jsonify
from flask_mysqldb import MySQL
from db import mysql, app
import routes

def create_app():
  routes.init_app(app)
  return app


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'contatos'
    
app.run()