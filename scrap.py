import re
import httpx
import config
from headers import headers
from bs4 import BeautifulSoup

def pagina_resultados(info_busca) -> set:
    """Raspa os dados da pagina de resultados"""
    index = 1
    while True:
        if index > 1:
            request = httpx.get(info_busca.url, headers=headers) 
        else:
            request = httpx.get(info_busca.url, headers=headers)     
        
        soup = BeautifulSoup(request.text, "html.parser")
        vagas = soup.find_all("a", attrs=info_busca.a_tag_attrs)   
        vagas = [config.BASE_URL + x.get("href") for x in vagas]
        if index == 1:
            vagas_encontradas = set(vagas)
            index += 1
            continue
        #se tiver os mesmos resultados          
        elif set(vagas).issubset(vagas_encontradas):
            break
        elif not vagas:
            break
        vagas_encontradas.update(vagas)
        index += 1
    
    return vagas_encontradas

def pagina_vaga(url:str) -> list:
    """Raspa os dados da pagina de uma vaga especifica"""
    try:
        request = httpx.get(url)
    except Exception as e:
        print(e)
        print(url)
        return None

    soup = BeautifulSoup(request.text, "html.parser")       
    #O numero de labels tem que ser igual ao numero de texts senao da merda
    labels = soup.find_all(attrs=config.tag_label_attrs)
    texts = soup.find_all(attrs=config.tag_text_attrs)
    
    dados = []
    for k in config.KEYS:
        value = None
        for i, tag in enumerate(labels):
            label = tag.text.strip().title()
            if k in label:
                value = re.sub(r"\s{2,}", " ", texts[i].text.strip())
            elif k == "URL":
                value = str(request.url)
        dados.append(value)
    return dados

if __name__ == "__main__":
    pass