import hashlib
from datetime import datetime
from utils.encryption import DataEncryption


class UserAuthentication:
    def __init__(self):
        self.users = {}
        self.encryption = DataEncryption("secure-key-12345-chars")

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password, email):
        """Register a new user"""
        if username in self.users:
            return {"status": False, "message": "User already exists"}

        hashed_pwd = self.hash_password(password)
        self.users[username] = {
            "password": hashed_pwd,
            "email": email,
            "created_at": datetime.now().isoformat(),
            "mfa_enabled": False
        }
        return {"status": True, "message": "User registered successfully"}

    def login_user(self, username, password):
        """Authenticate user"""
        if username not in self.users:
            return {"status": False, "message": "User not found"}

        if self.users[username]["password"] != self.hash_password(password):
            return {"status": False, "message": "Incorrect password"}

        return {"status": True, "message": "Login successful", "user": username}
