### 🔐 **Lab 2 Summary — Hacking into a Misconfigured Database (Safely!)**

#### 🧰 Tools Used:
- **Kali Linux**: The hacker's playground  
- **nmap**: Finds open ports and services  
- **mysql-client**: Connects to the database  
- **hashid**: Identifies hash types  
- **John the Ripper**: Cracks password hashes  

---

### 🕵️‍♂️ **Part 1: Find and Access the Database**
- Used `nmap` to scan target for open ports and found **MySQL** (port 3306).
- Connected using `mysql` with **no password and no SSL** — big security flaw!

---

### 🔍 **Part 2: Look Inside the Database**
- Viewed databases and tables (like `dvwa.users`).
- Extracted usernames and their hashed passwords.

---

### 🧠 **Part 3: Identify the Hash**
- Used `hashid` to identify the hash type — it was **MD5**, a weak hash.

---

### 🔓 **Part 4: Crack the Password**
- Saved the hash and used **John the Ripper** with the `rockyou.txt` wordlist.
- Successfully cracked the password: `password` (very weak!).

---

### 🛡️ **Part 5: What Went Wrong & How to Fix It**
**Problems:**
- No auth to DB
- Weak/blank passwords
- Weak hash (MD5)
- No SSL

**Fixes:**
- Enforce strong password policies
- Use better hashing (bcrypt, Argon2)
- Enable SSL
- Restrict user access

---

### 🎉 **End Result**
You scanned, accessed, enumerated, cracked, and understood how insecure setups can be exploited — all in a safe, learning environment. Great job!
