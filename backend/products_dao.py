from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT * FROM `Electric Store`.Products")

    cursor.execute(query)
    
    response = []

    for (product_id, name, wattage, price_per_unit) in cursor:
        # print(product_id, name, wattage, price_per_unit)
        response.append({
            'product_id': product_id,
            'name': name,
            'wattage': wattage,
            'price_per_unit': price_per_unit
        })
    
    return response

def insert_new_products(connection,product):
    cursor = connection.cursor()
    
    query = ("INSERT INTO Products (name, wattage, price_per_unit) VALUES(%s, %s, %s)")
    
    data = (product['name'],product['wattage'],product['price_per_unit'])
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM Products WHERE products_id=" + str(product_id))
    
    cursor.execute(query)
    connection.commit()


if __name__=='__main__':
    connection = get_sql_connection()
    # print(insert_new_products(connection,{
    #     'name' : 'Tube Bulb',
    #     'wattage' : '9',
    #     'price_per_unit' : '300'
    # }))
    # print(delete_product(connection,7))
    print(get_all_products(connection))