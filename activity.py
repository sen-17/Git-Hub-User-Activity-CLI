import requests

def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data for user '{username}'. Status code: {response.status_code}")
        return None
    
def main():
    username = input("Enter GitHub username: ")
    activity = get_user_activity(username)

    if activity:
        print(f"Recent activity for user '{username}':")
        for event in activity:
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            created_at = event["created_at"]
            print(f"- {event_type} in {repo_name} at {created_at}")
        
    else:
        print("No activity found or an error occurred.")

if __name__ == "__main__":
    main()