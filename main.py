import webbrowser


url2 = ''
url3 = ''
url4 = ''
url5 = ''
url6 = ''
url7 = ''

url_list = [url2, url3, url4, url5, url6, url7]

user_choice = input('Which browser are you using? (f)irefox or (c)rhome?' )


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'


for url in url_list:
    if user_choice == 'c':
        webbrowser.get(chrome_path).open_new_tab(url)
    elif user_choice == 'f':
        webbrowser.get(firefox_path).open_new_tab(url)
