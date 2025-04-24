Here’s a **summary of what this lab does**:

---

### 🔐 **Lab 1 Summary: Cryptographic Attacks – Brute Force & Traffic Analysis**

**Objective:**  
Explore the weaknesses in common network protocols (FTP, TELNET, SSH, HTTP) by:
- Performing brute force attacks to recover passwords.
- Using captured credentials to analyze network traffic.
- Evaluating the security of each protocol and recommending fixes.

---

### 🛠️ **Tasks Overview:**

1. **User Enumeration**  
   - Identify usernames on the vulnerable virtual machine for use in brute force attacks.

2. **Brute Force Attacks**  
   - Use tools like Hydra, Medusa, or NetExec for attacking FTP, TELNET, and SSH.
   - Use Burp Suite’s Intruder for brute force on HTTP login pages.

3. **Traffic Sniffing**  
   - Use recovered credentials to log in and capture traffic with Wireshark or tcpdump.
   - Analyze which protocols are secure (encrypted) or insecure (plaintext).

4. **Problem Analysis**  
   - Document any issues (e.g., rate limiting) faced during attacks and how they were handled.

5. **Mitigation Proposals**  
   - Suggest secure alternatives (e.g., using SSH instead of TELNET).
   - Explain how these alternatives improve security.

---

Basically, this lab teaches **how attackers find weaknesses**, and **how to defend against them** using basic tools.