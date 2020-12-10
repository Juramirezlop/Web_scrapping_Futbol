def web_scrap():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    url = "https://www.colombia.com/futbol/liga-colombiana/tabla-de-posiciones"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    titulares = soup.find_all(True, {'class':['d-none d-md-inline']})
    nombres = list(titulares)
    cad = ''
    limit = 0
    acum = ''
    for i in range(len(nombres)):
      cad += str(nombres[i])
    for i in range(len(cad)):
      if i == 0:
        continue
      elif ord(cad[i]) == 62:
        limit += 1
      elif ord(cad[i]) == 60:
        limit -= 1
        acum += ' '
      elif limit == 1:
        acum += str(cad[i])
    return acum
def main():
    print(web_scrap())
main() 
