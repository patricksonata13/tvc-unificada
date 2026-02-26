import sqlite3
from database import DB_PATH, get_connection, registrar_log

def get_all(table):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_by_id(table, id_field, id_value):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE {id_field}=?", (id_value,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def create_item(table, data, id_field='id'):
    if id_field in data:
        del data[id_field]
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?' for _ in data])
    values = tuple(data.values())
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values)
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

def update_item(table, id_field, id_value, data):
    if id_field in data:
        del data[id_field]
    set_clause = ', '.join([f"{k}=?" for k in data.keys()])
    values = tuple(data.values()) + (id_value,)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {id_field}=?", values)
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    return affected

def delete_item(table, id_field, id_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {id_field}=?", (id_value,))
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    return affected
