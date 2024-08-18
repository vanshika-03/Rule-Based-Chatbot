#library for searching the string
import re

responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "hey": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I am a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome! If you have any other questions, feel free to ask.",
        "thankyou": "You're welcome! If you have any other questions, feel free to ask.",
        "opening hours": "Our store is open from 8 AM to 8 PM from Monday to Saturday, and from 9 AM to 6 PM on Sundays.",
        "whats up": "Hello! How can I help you today :)",
        "help": "What can I do for you?",
        "what do you have?":"Our menu consists of Beverages, Pastries, Snacks, Light Meals. To know the full menu type'menu",
        "beverages": "Espresso, Americano, Latte, Cappuccino, Tea,Hot Chocolate, Cold Coffee, Strawberry Smoothie, Pineapple, Banana Smoothie, Orange Juice, Apple Juice, Carrot Juice",
        "pastries": "Croissants, Blueberry Muffin, Chocolate Chip Muffin, Cookies",
        "light meals":"Sandwiches, Garden Salad, Tomato Soup, Sweet Corn Soup",
        "i want to order": "Sure, to get the menu type 'menu' and if you want to place an order 'order' ",
        "can i get your menu": "Sure, to get the menu type 'menu'",
        "default": "I'm sorry, I didn't understand that. Could you please rephrase?"
}

menu_items = {
    # Beverages
    "espresso": 100,
    "americano": 120,
    "latte": 150,
    "cappuccino": 150,
    "tea": 50,
    "hot chocolate": 120,
    "cold coffee": 130,
    "strawberry smoothie": 180,
    "pineapple banana smoothie": 180,
    "orange juice": 80,
    "apple juice": 80,
    "carrot juice": 80,

    # Pastries and Snacks
    "croissant": 60,
    "blueberry muffin": 70,
    "chocolate chip muffin": 70,
    "cookies": 50,

    # Light Meals
    "sandwiches": 150,
    "garden salad": 120,
    "tomato soup": 90,
    "sweet corn soup": 90,

    "default": "I'm sorry, I didn't understand that. Could you please ask about a specific item?"
}

# Regular expression patterns for menu items
menu_patterns={
    "espresso": re.compile(r'\b(espresso|espressos)\b', re.IGNORECASE),
    "americano": re.compile(r'\b(americano|americanos)\b', re.IGNORECASE),
    "latte": re.compile(r'\b(latte|lattes)\b', re.IGNORECASE),
    "cappuccino": re.compile(r'\b(cappuccino|cappuccinos)\b', re.IGNORECASE),
    "tea": re.compile(r'\b(tea|teas)\b', re.IGNORECASE),
    "hot chocolate": re.compile(r'\b(hot chocolate|hot chocolates)\b', re.IGNORECASE),
    "cold coffee": re.compile(r'\b(cold coffee|cold coffees)\b', re.IGNORECASE),
    "strawberry smoothie": re.compile(r'\b(strawberry smoothie|strawberry smoothies)\b', re.IGNORECASE),
    "pineapple banana smoothie": re.compile(r'\b(pineapple banana smoothie|pineapple banana smoothies)\b', re.IGNORECASE),
    "orange juice": re.compile(r'\b(orange juice|orange juices)\b', re.IGNORECASE),
    "apple juice": re.compile(r'\b(apple juice|apple juices)\b', re.IGNORECASE),
    "carrot juice": re.compile(r'\b(carrot juice|carrot juices)\b', re.IGNORECASE),
    "croissant": re.compile(r'\b(croissant|croissants)\b', re.IGNORECASE),
    "blueberry muffin": re.compile(r'\b(blueberry muffin|blueberry muffins)\b', re.IGNORECASE),
    "chocolate chip muffin": re.compile(r'\b(chocolate chip muffin|chocolate chip muffins)\b', re.IGNORECASE),
    "cookies": re.compile(r'\b(cookie|cookies)\b', re.IGNORECASE),
    "sandwiches": re.compile(r'\b(sandwich|sandwiches)\b', re.IGNORECASE),
    "garden salad": re.compile(r'\b(garden salad|garden salads)\b', re.IGNORECASE),
    "tomato soup": re.compile(r'\b(tomato soup|tomato soups)\b', re.IGNORECASE),
    "sweet corn soup": re.compile(r'\b(sweet corn soup|sweet corn soups)\b', re.IGNORECASE)
    # "coffee":
    # "juice":
    # ""
}

# Regular expression patterns for predefined responses
response_patterns={
    "hi": re.compile(r'\b(hi|hello|hey|helloo|hii)\b', re.IGNORECASE),
    "opening hours": re.compile(r'\b(opening hours|hours|time|store time|store timings|store hours)\b', re.IGNORECASE),
    "location": re.compile(r'\b(location|where are you|address)\b', re.IGNORECASE),
    "menu": re.compile(r'\b(menu|food|items|list of items|what do you have)\b', re.IGNORECASE),
    "thanks": re.compile(r'\b(thanks|thank you)\b', re.IGNORECASE),
    "beverages": re.compile(r'\b(beverages|beverage)\b',re.IGNORECASE),
    "pastries":re.compile(r'\b(pastry|pastries)\b',re.IGNORECASE),
    "light meals": re.compile(r'\b(light meal|light meals|meal|meals)\b', re.IGNORECASE)
}

def get_menu_items():
    menu="Here is our menu:\n"
    for item, price in menu_items.items():
        if item != "default":
            menu+=f"{item.replace('_',' ').title()}: Rs. {price}\n"
    return menu

def get_response(user_input):
    user_input=user_input.lower()
    try:
        for item, pattern in menu_patterns.items():
            if pattern.search(user_input):
                return f"The price of {item} is Rs{menu_items[item]}"

        for response,pattern in response_patterns.items():
            if pattern.search(user_input):
                if response=="menu":
                    return get_menu_items()
                return responses[response]
        if(user_input in responses):
            return responses[user_input]

        if re.search("order|buy",user_input,re.IGNORECASE):
            print("How many items would you like to order?")
            no_of_items = int(input())
            order_items = {}

            for i in range(1, no_of_items + 1):
                item = input("Enter your order one by one. For example: '2 cold coffee'\n")
                spl = item.split(" ")
                quantity = spl[0]
                spl.remove(spl[0])

                order_item = ""
                if len(spl) == 1:
                    order_item = spl[0].lower()
                    order_items[order_item] = quantity
                else:

                    for li in spl:
                        order_item += li.lower()
                        if spl.index(li)!=len(spl)-1:
                            order_item += " "
                    order_items[order_item] = quantity

            return order(order_items)

        return menu_items["default"]
    except:
        return "Something was wrong in your last input. Do you need help with something else."

def order(order_items):
    order_total=0
    for item in order_items:
        item_price = menu_items[item]
        total_price=int(order_items[item])*item_price
        order_total+=total_price

    return "Thank you for the order! Hope you enjoy your meal ;) \nYour total bill is Rs. " + str(order_total)

def main():
    print("Welcome to the Cafe! Type 'bye' to exit.")
    while True:
        user_input=input("You: ")

        if re.search(r'\b(bye|goodbye|see you|see you!|bye bye|later|seeya)\b', user_input, re.IGNORECASE):
            print("Goodbye! Have a great day :)")
            break
        response = get_response(user_input)
        print(response)

if __name__=="__main__":
    main()