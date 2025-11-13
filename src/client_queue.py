def insert_client(queue, id_client, money):
    if id_client in queue.keys():
        return False
    queue[id_client] = money
    return True

def buys(queue, id_client, price):
    if price > queue[id_client]:
        return False, queue[id_client]
    queue[id_client] -= price
    return True, queue[id_client]

def main():
    queue = {}
    id_client = 0
    money = 10

    insert_success = insert_client(queue, id_client, money)
    if insert_success:
        print("Client inserted successfully")
    else:
        print("Failure on inserting the new client to the database. There's already a client with this id.")
    
    price = 4
    success, qnty_left = buys(queue, id_client, price)
    
    if success:
        print(f"The purchase was a success and the client of id {id_client} still has {qnty_left} dollars.")

if __name__ == "__main__":
    main()