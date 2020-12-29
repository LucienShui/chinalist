import requests

china_list_url: str = 'https://raw.githubusercontent.com/pexcn/daily/gh-pages/chinalist/chinalist.txt'


def main():
    response: requests.Response = requests.api.get(china_list_url)
    china_list: str = response.content.decode('utf-8')

    omega_china_list: str = '\n'.join(map(lambda each: f'||{each}', china_list.split()))

    with open('chinalist.txt', 'w') as file:
        file.write(omega_china_list)


if __name__ == '__main__':
    main()
