# bcrypt
import bcrypt


def encrypt_password(password):
    """Encrypts the user's password to avoid
    dumping it as plain-text in the db."""

    salt = bcrypt.gensalt()
    password = password.encode("utf-8")
    hash_password = bcrypt.hashpw(password, salt)
    return hash_password
