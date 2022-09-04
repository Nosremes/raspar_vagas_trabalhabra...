import re
import utils
from dataclasses import dataclass

KEYS = ["Número De Vagas", "Empresa", "Salário", "Cidade/Estado:", 
    "Tipo De Vaga:", "Regime De Contrato", "Descrição", "URL"]

BASE_URL = 
RESULTS_PATH = "/vagas-empregos-em-"

#pagina resultados
a_tag_attrs = {"class": re.compile("job__vacancy.*")}

#pagina de uma vaga especifica
tag_label_attrs = {"class": re.compile(".*job-label.*", re.IGNORECASE)}
tag_text_attrs = {"class" : re.compile("job-plain-text|jobview__container__status.*")}

@dataclass
class Busca:
    cidade:str
    estado:str
    funcao:str

    def __post_init__(self):
        self.url = utils.url_results_page(self.cidade, self.estado, self.funcao) 
        self.title_re = re.compile(f".*{self.funcao}.*{self.cidade}.*{self.estado}", re.IGNORECASE)
        self.a_tag_attrs = a_tag_attrs
        self.a_tag_attrs["title"] = re.compile(
            f".*{self.funcao}.*{self.cidade}.*{self.estado}", re.IGNORECASE
        )
