import scrap
import utils
import config

def Scrap(cidade, estado, funcao):
	info_busca = config.Busca(cidade, estado, funcao)
	#url = utils.url_results_page(cidade, estado, funcao)
	vagas_url = scrap.pagina_resultados(info_busca)
	vagas_infos = []
	for url in vagas_url:
		info = scrap.pagina_vaga(url)
		vagas_infos.append(info)
	
	return vagas_infos


if __name__ == "__main__":
	data = Scrap("rio grande", "rs", "Estoque")
	df = utils.write_excel(data, "me_contrata.xlsx")
