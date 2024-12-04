import requests
from bs4 import BeautifulSoup
import logging
import time
import os 
import sys
import time

# Replace these values with your own
USERNAME = 'YOUR_USERNAME'
TOKEN = 'YOUR_ACCESS_TOKEN'

# URL for GitHub API
BASE_URL = 'https://api.github.com'

# Upload the ban list
GLOBAL_PATH = os.getcwd()
BAN_LIST_FILE_PATH_FOLLOWERS = f'{GLOBAL_PATH}/ban_list_followers.txt'  
BAN_LIST_FILE_PATH_FOLLOWING = f'{GLOBAL_PATH}/ban_list_following.txt' 

# Characters for process display
LOADING_CHAR = ['|', '/', '-', '\\']

# Configuring logging
logging.basicConfig(filename=f'{GLOBAL_PATH}/subscription_manager.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_ban_list(file_path:str) -> set:
    """Loads a ban list from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()

def get_users_list(ban_list: set, message:str, user_type:str='followers'):
    """
    Gets a list of users (subscribers or subscriptions) with support for paginated navigation,
    excluding users from the ban list.

    Args:
        ban_list (set): List of users to be excluded
        message (str): Message to be output in the process
        user_type (str): Type of users to receive (‘followers’ or ‘following’)
    Returns:
        list: User list
    """
    if user_type not in ['followers', 'following']:
        raise ValueError("user_type must be ‘followers’ or ‘following’")

    logging.info(f"Parsing {'followers' if user_type == 'followers' else 'following'}...") 
    users = []
    page = 1
    while True:
        sys.stdout.write(f'\r{message} {LOADING_CHAR[page % 4]}')
        sys.stdout.flush() 
        url = f'https://github.com/{USERNAME}?tab={user_type}&page={page}'
        try:
            response = requests.get(url)
            response.raise_for_status() # Checking for errors
            
            # Parsing the HTML code of a page
            soup = BeautifulSoup(response.text, 'html.parser')
            current_users = soup.find_all('img', class_='avatar')
            
            if not current_users: # If the current page is empty, exit the loop
                break
            
            # Filter users to exclude those on the ban list
            for user in current_users[1:]:
                username = user.get('alt')[1:]
                if username not in ban_list:
                    users.append(username)

            # If the number of current users is less than 2, exit the loop
            if len(current_users) < 2:
                break
            
            page += 1  # Go to the next page
            time.sleep(0.5) # Delay between requests to bypass error 429

        except requests.exceptions.HTTPError as e:
            logging.error(f'Ошибка HTTP: {e}')
            break

    return users

def print_logo() -> None:
    """Printing of the programme logo"""
    logo = r"""
  _____       _    ___  ___                                  
 /  ___|     | |   |  \/  |                                  
 \ `--. _   _| |__ | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
  `--. \ | | | '_ \| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 /\__/ / |_| | |_) | |  | | (_| | | | | (_| | (_| |  __/ |   
 \____/ \__,_|_.__/\_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                              __/ |          
                                             |___/           
_____________________________________________________________          
    """
    print(logo)


def update_subscription(username:str, isFollowing=False) -> None:
    """
    Manages the subscription for the user.
    Args:
        username (str): GitHub username
        isFollowing (bool): True if the user should be followed, False otherwise"""
    url = f'{BASE_URL}/user/following/{username}'
    try:
        response = requests.put(url, auth=(USERNAME, TOKEN)) if isFollowing else requests.delete(url, auth=(USERNAME, TOKEN))
        response.raise_for_status()
        message = f'{"Subscribed to" if isFollowing else "Unsubscribed from"} {username}'
        print(message)
        logging.info(message)
    except requests.exceptions.HTTPError as e:
        message = f'Failed {'subscribe' if isFollowing else 'unsubscribe'} from {username}: {e}'
        print(message)
        logging.error(message)
    except requests.exceptions.RequestException as e:
        message = f'Query error on {'subscriptions' if isFollowing else 'unsubscribes'} for {username}: {e}'
        print(message)
        logging.error(message)

def manage_subscriptions(ban_list_followers: set, ban_list_following: set) -> None:
    """
    Manages the user's subscriptions based on bins lists.

    Args:
        ban_list_followers (set): The set of users to be unsubscribed from the subscription list.
        ban_list_following (set): The set of users who should be excluded from the subscription list.
    """
    followers = get_users_list(ban_list_followers, message="Get a list of subscribers", user_type='followers')
    print("\nSubscription list received!")
    following = get_users_list(ban_list_following, message="Getting a list of subscriptions", user_type='following')
    print("\nSubscription list received!")

    # Subscribe to everyone who subscribes to you
    for follower in followers:
        if follower not in following:
            update_subscription(follower, isFollowing=True)

    # Unsubscribe from those who are not subscribed to you
    for followed in following:
        if followed not in followers:
            update_subscription(followed)

if __name__ == '__main__':
    print_logo()
    print("Script Started")
    logging.info("Script started") 

    ban_list_followers = load_ban_list(BAN_LIST_FILE_PATH_FOLLOWERS)  
    ban_list_following = load_ban_list(BAN_LIST_FILE_PATH_FOLLOWING)  
    
    manage_subscriptions(ban_list_followers, ban_list_following) 

    print("Script Finished")
