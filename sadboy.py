#!/usr/bin/env python3
import re
import sys

banner = """
███████╗ █████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝
███████╗███████║██║  ██║██████╔╝██║   ██║ ╚████╔╝ 
╚════██║██╔══██║██║  ██║██╔══██╗██║   ██║  ╚██╔╝  
███████║██║  ██║██████╔╝██████╔╝╚██████╔╝   ██║   
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   

Tool: sadboy
Creator: ionutivan21
Purpose: Educational / Anti-Phishing
"""

print(banner)

url = input("Introdu URL-ul pentru analiză: ")

score = 0

if "@" in url:
    print("[!] Conține '@' – tehnică de phishing")
    score += 1

if url.count("//") > 1:
    print("[!] Redirecționare suspectă")
    score += 1

if len(url) > 75:
    print("[!] URL prea lung")
    score += 1

if re.search(r"\d+\.\d+\.\d+\.\d+", url):
    print("[!] Folosește adresă IP")
    score += 1

if not url.startswith("https://"):
    print("[!] Lipsă HTTPS")
    score += 1

print("\nScor final:", score)

if score >= 3:
    print("⚠️ POSIBIL PHISHING")
else:
    print("✅ URL probabil sigur (nu garantat)")
