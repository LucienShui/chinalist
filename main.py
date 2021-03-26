import requests
import typing
from datetime import datetime

china_list_url: str = 'https://raw.githubusercontent.com/pexcn/daily/gh-pages/chinalist/chinalist.txt'


def get_lucien_list() -> typing.List[str]:
    with open('lucien.txt') as lucien_file:
        lucien_list: typing.List[str] = lucien_file.read().split()

    return lucien_list


def main():
    response: requests.Response = requests.api.get(china_list_url)
    china_list: typing.List[str] = response.content.decode('utf-8').split()
    lucien_list: typing.List[str] = get_lucien_list()

    omega_china_list: typing.List[str] = [*map(lambda each: f'||{each}', lucien_list + china_list)]

    header: typing.List[str] = [
        f'! Last Modified: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    ]

    content = '\n'.join(header + sorted(omega_china_list))

    with open('chinalist.txt', 'w') as file:
        file.write(content)


if __name__ == '__main__':
    main()
