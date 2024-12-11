import requests

def get_google_info(access_token: str):
    try:
        url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_info = response.json()
        return user_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user info: {e}")
        return None