import requests
import os
from dotenv import load_dotenv

class APIClient:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_token}",
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        })

    def login(self, username, password):
        url = f'{self.base_url}/api/login'
        data = {'username': username, 'password': password}
        response = self.session.post(url, json=data)
        if response.status_code != 200:
            return False
        return True

    def is_logged_in(self):
        check_url = f"{self.base_url}/api/is_logged_in"
        response = self.session.get(check_url)
        return response.json().get('result', False)

    def do_perma_ban(self, player, steam_id_64, reason, by):
        ban_url = f"{self.base_url}/api/do_perma_ban"
        payload = {
            'player': player,
            'steam_id_64': steam_id_64,
            'reason': reason,
            'by': by
        }
        try:
            response = self.session.post(ban_url, json=payload)
            print(f"do_perma_ban response: {response.status_code}, {response.text}")
            return response.ok
        except Exception as e:
            print(f"Fehler beim Aufrufen von do_perma_ban: {e}")
            return False

    def do_temp_ban(self, player, steam_id_64, duration_hours, reason, by):
        temp_ban_url = f"{self.base_url}/api/do_temp_ban"
        payload = {
            'player': player,
            'steam_id_64': steam_id_64,
            'duration_hours': duration_hours,
            'reason': reason,
            'by': by
        }
        try:
            response = self.session.post(temp_ban_url, json=payload)
            print(f"do_temp_ban response: {response.status_code}, {response.text}")
            return response.ok
        except Exception as e:
            print(f"Fehler beim Aufrufen von do_temp_ban: {e}")
            return False

    def do_unban(self, steam_id):
        unban_url = f"{self.base_url}/api/do_unban"
        response = self.session.post(unban_url, json={'steam_id_64': steam_id})
        return response.ok

    def unblacklist_player(self, steam_id):
        unban_url = f"{self.base_url}/api/unblacklist_player"
        response = self.session.post(unban_url, json={'steam_id_64': steam_id})
        return response.ok

    def do_blacklist_player(self, steam_id_64, name, reason, by):
        blacklist_url = f"{self.base_url}/api/blacklist_player"
        payload = {
            'steam_id_64': steam_id_64,
            'name': name,
            'reason': reason,
            'by': by
        }
        try:
            response = self.session.post(blacklist_url, json=payload)
            print(f"do_blacklist_player response: {response.status_code}, {response.text}")
            return response.ok
        except Exception as e:
            print(f"Fehler beim Aufrufen von do_blacklist_player: {e}")
            return False

    def do_watch_player(self, player, steam_id_64, reason):
        watchlist_url = f"{self.base_url}/api/do_watch_player"
        payload = {
            'player': player,
            'steam_id_64': steam_id_64,
            'reason': reason
        }
        try:
            response = self.session.post(watchlist_url, json=payload)
            print(f"do_watch_player response: {response.status_code}, {response.text}")
            return response.ok
        except Exception as e:
            print(f"Fehler beim Aufrufen von do_watch_player: {e}")
            return False

    def do_unwatch_player(self, player, steam_id_64):
        unwatch_url = f"{self.base_url}/api/do_unwatch_player"
        payload = {
            'player': player,
            'steam_id_64': steam_id_64
        }
        try:
            response = self.session.post(unwatch_url, json=payload)
            print(f"do_unwatch_player response: {response.status_code}, {response.text}")
            return response.ok
        except Exception as e:
            print(f"Fehler beim Aufrufen von do_unwatch_player: {e}")
            return False

    def post_player_comment(self, steam_id, comment):
        post_comment_url = f"{self.base_url}/api/post_player_comment"
        payload = {
            'steam_id_64': steam_id,
            'comment': comment  # Hier ändern wir message auf comment
        }
        try:
            response = self.session.post(post_comment_url, json=payload)
            print(f"post_player_comment response: {response.status_code}, {response.text}")
            if response.status_code == 200:
                response_data = response.json()
                if not response_data.get("failed", True):
                    return True
                else:
                    print(f"Fehler in der API-Antwort: {response_data}")
                    return False
            return False
        except Exception as e:
            print(f"Fehler beim Aufrufen von post_player_comment: {e}")
            return False