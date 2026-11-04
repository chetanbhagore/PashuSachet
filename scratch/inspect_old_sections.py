import subprocess, re

proc = subprocess.run(['git', 'show', '7f3a336:index.html'], capture_output=True, text=True, encoding='utf-8')
old_html = proc.stdout

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', old_html)
print("Sections in 7f3a336:", sections)

headers = re.findall(r'<header[^>]*class=["\']([^"\']+)["\']', old_html)
print("Headers in 7f3a336:", headers)

roles = re.findall(r'activatePersona\([\'"]([^\'"]+)[\'"]\)', old_html)
print("activatePersona calls in 7f3a336:", set(roles))
