with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<link rel="stylesheet" href="css/style.css">'
replacement = '''<meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="theme-color" content="#fbfbfd">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/style.css">'''

if target in html:
    html = html.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Head tags updated successfully!")
else:
    print("Target not found in index.html")

