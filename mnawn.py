import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"

print(f"                   ")

#print

try:

       os.system('clear')
       print(f" {B}[{U}×{B}] {T} SC INI SEDANG DALAM PROSSES PERBAIKAN {M}!!!")
       print(f"     ")
       print(f" {B}[{U}×{B}] {A} SILAHKAN TUNGGU UPDATE SELANJUTNYA ")
       print(f"     ")
       print(f" {B}[{U}×{B}] {J} SEKIAN TERIMAKASIH {Z}^_^")

       os.system('xdg-open https://wa.me/+6282277004825?text=Bg+Saya+Mau+Pre-Order+Next+Update+Sc+IG+Lu+Bg')
except:pass
