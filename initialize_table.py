import psycopg2
from flask import Flask, jsonify,request
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

def create_tables():
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS bookingUser (
        "id" serial,
        "username" text,
        "email" text,
        PRIMARY KEY( id )
    );
        """,
        """
        CREATE TABLE IF NOT EXISTS pv_info (
        "id" serial,
        "name" VARCHAR(255),
        "address" VARCHAR(255),
        "description" TEXT,
        "imagePath" VARCHAR(255),
        "price" VARCHAR(255),
        "isAvailable" INT,
        PRIMARY KEY( id )
	);  
        """,
        """
        CREATE TABLE IF NOT EXISTS pv_booking_info (
        "id" serial,
        "firstName" VARCHAR(255),
        "lastName" VARCHAR(255),
        "email" VARCHAR(255),
        "mobileNo" VARCHAR(255),
        "poolVillaId" INT,
        "checkIn" DATE,
        "checkOut" DATE,
        "isPaid" INT,
        PRIMARY KEY( id )
	); 
        """)


    conn = None
    
    try:
     
        # connect to the PostgreSQL server
        print('migrating...')
        conn = psycopg2.connect(
        host=app.config["DB_HOST"],
        database=app.config["DB_NAME"],
        user=app.config["DB_USERNAME"],
        password=app.config["DB_PASSWORD"])


        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('done!')
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

        


if __name__ == '__main__':
    create_tables()