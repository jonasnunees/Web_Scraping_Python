import requests
from bs4 import BeautifulSoup as bs


github_user = input('Informe o nome de usuário GitHub.: ')


url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')


profile_image = soup.find('img', {'class' : 'avatar'})['src']
username = soup.find('span', {'class' : 'p-nickname'})
contributions = soup.find('h2', {'class' : 'f4 text-normal mb-2'})
repositories = soup.find('span', {'class' : 'Counter'})


print(f'Username.: {username.string.strip()}')
print(f'Link do perfil.: {url}')
print(f'Link da imagem do perfil.: {profile_image}')
print(f'Contribuições.: {' '.join(contributions.string.split())}')
print(f'Quantidade de repositórios.: {repositories.string}')