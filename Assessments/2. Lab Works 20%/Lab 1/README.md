Here’s a **summary of what this lab does**:

### 🧪 **Goal**:  
Simulate how a hacker attacks a weak system to learn about **network security**.

### 💻 **Setup**:  
- Use **Kali Linux** (attacker)  
- Use **Metasploitable 2** (target)  
- Connect both in the same network

### 🔍 **What You’ll Do**:

1. **Scan for open ports** (with `nmap`)  
   → See which services are running: FTP, SSH, Telnet, HTTP

2. **Find usernames** (with `enum4linux`)  
   → Get a list of accounts on the target

3. **Discover hidden web pages** (with `gobuster`)  
   → Look for `/login`, `/admin`, etc.

4. **Brute force passwords**  
   → Use tools like `hydra`, `medusa`, and **Burp Suite**  
   → Try different username/password combos for FTP, Telnet, SSH, and websites

5. **Sniff data with Wireshark**  
   → See if credentials are sent in plain text  
   → Check how secure each protocol is

6. **Make a results table**  
   → Show which protocols leak info and which protect it

### 🔒 **Security Lessons**:

- **FTP & Telnet** are insecure — send data in plain text  
- **SSH** is encrypted — more secure  
- Use strong passwords and secure alternatives (e.g., HTTPS, SFTP, SSH with keys)

---

Basically, this lab teaches **how attackers find weaknesses**, and **how to defend against them** using basic tools.