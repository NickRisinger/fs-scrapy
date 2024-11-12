import sys
import re

'''
https://www.flashscorekz.com/match/8IDNpdqo/#/match-summary
https://www.flashscorekz.com/match/lYWjjILN/#/match-summary
https://www.flashscorekz.com/match/2HYrhviB/#/match-summary
https://www.flashscorekz.com/match/rZxSmhvo/#/match-summary
https://www.flashscorekz.com/match/j1TMbSQH/#/match-summary
'''

def validate_link(link):
    regexp = re.compile(r"^https://www\.flashscorekz\.com/match/[A-Za-z0-9]+/#/match-summary$")

    if regexp.match(link):
        return True
    else:
        return False


def get_links():
    print("Введите ссылки, после каждой ссылки нужно нажать 'Enter'.\nДля того чтобы закончить ввод 'break'\n")

    links = []

    while True:
        link = input(f"Введите ссылку №{len(links) + 1}: ")

        if link == 'break':
            print("Ввод закончен, все ссылки приняты\n")
            break

        if link in links:
            print("Ссылка уже была введена!\n")
        elif validate_link(link):
            links.append(link)
        else:
            print("Вы ввели не коректную ссылку: ссылка должна содержать проокол (https) и домен (www.flashscorekz.com)\n")

    return links


if __name__ == '__main__':
    links = get_links()

    if not links:
        print("Вы не ввели не одной ссылки. Программа остановлена.")
        sys.exit()

    print("Начинаю парсинг страниц....\n")
