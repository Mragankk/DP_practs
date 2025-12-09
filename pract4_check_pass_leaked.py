# input file - as 'users.txt'

# user1,password123
# riya,844riat
# admin,admin123



import hashlib   # SHA1
import requests  # To make HTTP requests to the HIBP API.

def check_pwned(password: str) -> int:
    # SHA1 hash of password
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1[:5]     # first 5 chars
    suffix = sha1[5:]     # rest of the chars

    # Query Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError("Error fetching from API")

    # Search if suffix exists in API response
    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0  # password NOT found in breaches


def main():
    filename = "users.txt"
    print("Checking passwords from file:", filename)
    print("------------------------------------")

    with open(filename, "r") as file:
        for line in file:
            username, password = line.strip().split(",")

            count = check_pwned(password)

            if count > 0:
                print(f"[LEAKED]  User: {username} | Password found {count} times!")
            else:
                print(f"[SAFE]    User: {username} | Password NOT found.")


if __name__ == "__main__":
    main()