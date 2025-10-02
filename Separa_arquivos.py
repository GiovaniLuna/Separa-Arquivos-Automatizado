import os
from tkinter.filedialog import askdirectory

def palavra_chave_esta_no_arquivo(chave,arquivo,pasta):
    palavra_chave = chave.lower()
    nome_arquivo = arquivo.lower()
    if palavra_chave in nome_arquivo:
        return True  
    elif arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(pasta,arquivo)
        with open(caminho_arquivo,"r", encoding="utf-8", errors="ignore") as texto:
            conteudo = texto.read().lower()
            for palavra_chave in nomes_pastas_separadas[chave]:
                if palavra_chave in conteudo:
                    return True
    
            
    return False



pasta_com_arquivos = askdirectory(title="Pasta Origem")
pasta_destino_arquivos = askdirectory(title="Pasta Destino")

nomes_pastas_separadas = {
    "Adriana":["adriana","nutrição"],
    "Giovani":["giovani","programação"],
    "Osmario":["osmario","contabilidade"],
    "Zuleide":["zuleide","medicina"]
}

lista_de_arquivos = os.listdir(pasta_com_arquivos)

for nome_arquivo in lista_de_arquivos:
    nome_completo_original = os.path.join(pasta_com_arquivos,nome_arquivo)
    if not os.path.isfile(nome_completo_original):
        continue

    for chave in nomes_pastas_separadas.keys():
        if palavra_chave_esta_no_arquivo(chave,nome_arquivo,pasta_com_arquivos):
            nova_pasta = chave
            caminho_nova_pasta = os.path.join(pasta_destino_arquivos,nova_pasta)
            if not os.path.exists(caminho_nova_pasta):
                os.mkdir(caminho_nova_pasta)
            nome_completo_final = os.path.join(pasta_destino_arquivos,nova_pasta,nome_arquivo)    

            os.rename(nome_completo_original,nome_completo_final)
            break
            
