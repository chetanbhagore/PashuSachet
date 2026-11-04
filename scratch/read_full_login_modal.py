import sys
sys.stdout.reconfigure(encoding='utf-8')
f = open('index.html', encoding='utf-8').read()
idx = f.find('id="loginModal"')
print(f[idx:idx+2500])
