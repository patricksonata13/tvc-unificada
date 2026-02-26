from database import get_connection

def get_all(table):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_by_id(table, id_field, id_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE {id_field} = %s", (id_value,))
    row = cursor.fetchone()
    conn.close()
    return row

def create_item(table, data, id_field='id'):
    # Remove o id se presente (para auto increment)
    if id_field in data:
        del data[id_field]
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    values = tuple(data.values())
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders}) RETURNING {id_field}", values)
    new_id = cursor.fetchone()[id_field]
    conn.commit()
    conn.close()
    return new_id

def update_item(table, id_field, id_value, data):
    if id_field in data:
        del data[id_field]
    set_clause = ', '.join([f"{k} = %s" for k in data.keys()])
    values = tuple(data.values()) + (id_value,)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {id_field} = %s", values)
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    return affected

def delete_item(table, id_field, id_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {id_field} = %s", (id_value,))
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    return affected
