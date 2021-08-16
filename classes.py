class order():
    def menu(self):
        '''
        contains whole menu. Each pizza is represented by a dictionary and tells us about its name,
        ingredients, price
        :param choice:
        :return:
        '''
        num0 = {
            "number": 0,
            "name": "focaccia",
            "price": 15
        }
        num1 = {
            "number": 1,
            "name": "margherita",
            "price": 19
        }
        num2 = {
            "number": 2,
            "name": "salami",
            "price": 23
        }
        num3 = {
            "number": 3,
            "name": "prosciutto",
            "price": 23
        }
        num4 = {
            "number": 4,
            "name": "capriciosa",
            "price": 24
        }
        num5 = {
            "number": 5,
            "name": "funghi",
            "price": 25
        }
        num6 = {
            "number": 6,
            "name": "siciliana",
            "price": 29
        }
        num7 = {
            "number": 7,
            "name": "chorizo",
            "price": 31
        }
        num8 = {
            "number": 8,
            "name": "frutti di mare",
            "price": 34
        }
        menu_list = [num0 ,num1, num2, num3, num4, num5, num6, num7, num8]
        return menu_list


    def disp_menu(self):
        menu = self.menu()
        for position in menu:
            print(f'{position["number"]}\t{position["name"]}\t{position["price"]}')


    def bill(self, order_list):
        menu = self.menu()  #list of dictionaries where key "price" is found by key "number"
        total_price = 0
        for order in order_list:
            price_of_single_dish = menu[order["dish"]]["price"]
            price_times_quantity = price_of_single_dish * order["quantity"]
            total_price += price_times_quantity
        return total_price



    def order(self):
        anything_else = 1
        order_list = []
        dish_and_quantity={
            "dish": 0,
            "quantity": 0
        }
        while anything_else == 1:
            dish = int(input(f'Choose dish\n'))
            quantity = int(input(f'choose quantity\n'))
            dish_and_quantity['dish'] = dish                #each time updated
            dish_and_quantity['quantity'] = quantity        #each time updated
            order_list.append(dish_and_quantity.copy())            #new position with its quantity in order
            anything_else = int(input(f'would you like anything else? \n(If no press 0, if yes press 1)\n'))
        return order_list

    def waiter(self):
        '''
        takes order from guest. Firstly greets them, then asks everyone seperately about their order.
        :return:
        '''
        self.num_of_guests = int(input(f'Hello, how many sits for You?\n'))
        print(f'You can sit here. \nHere is our menu.')
        self.disp_menu()
        order_list = self.order()
        print(f'Here is Your order {order_list}')
        total_price = self.bill(order_list)
        print(f'Here is your bill {total_price}')






