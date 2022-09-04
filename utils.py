import config
import pandas as pd

def url_results_page(cidade:str, estado:str, funcao:str="") -> str:
    """Retorna o url para a pagina de resultados"""
    url = config.BASE_URL + config.RESULTS_PATH
    url += f"{cidade.strip().replace(' ', '-')}-{estado}/{funcao}"
    return url

def write_excel(data, path):
    if data:
        df = pd.DataFrame(data=data, columns=config.KEYS)
        df.to_excel(path, index=False)
        return df
    else:
        return None