# Bcrypt
import bcrypt


def encrypt_password(password):
    """Encrypts the user's password to avoid
    dumping it as plain-text in the db."""

    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password, salt)
    return hash_password

def check_password(password):
    """Checks if the given password checks with
    the encripted password in the db."""

    user_pass = db.query(Uer)
    return bcrypt.checkpw()
    
