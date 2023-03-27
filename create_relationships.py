"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    create_relationships_tbl_query =
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
cur.execute(create_relationships_tbl_query)
con.commit()
con.close()
return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    return 

if __name__ == '__main__':
   main()