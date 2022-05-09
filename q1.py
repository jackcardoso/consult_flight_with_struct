
import struct

dados = struct.Struct("20s 50s 50s 100s")



def codifica(nomeArquivo):
    txt = nomeArquivo.replace("bin","txt")
    with open(txt, "r", encoding="utf-8") as arquivoTxt:
        with open(nomeArquivo,"wb") as arquivoBin:

            linha = arquivoTxt.readline()
            arquivoTxt.seek(0)

            while linha != "":
                linha = arquivoTxt.readline()
                separadas = linha.split("#")

                if len(separadas) > 1:
                    pais = separadas[0]
                    city = separadas[1]
                    aero = separadas[2]
                    cias = separadas[3]

                    bloco = dados.pack(pais.encode("utf-8"), city.encode("utf-8"), aero.encode("utf-8"), cias.encode("utf-8"))
                    arquivoBin.write(bloco)





def decodificaDados(bloco):
    campos =  dados.unpack(bloco)


    pais = campos[0].decode("utf-8").rstrip(chr(0))
    city = campos[1].decode("utf-8").rstrip(chr(0))
    aero = campos[2].decode("utf-8").rstrip(chr(0))
    cias = campos[3].decode("utf-8").rstrip(chr(0))


    return pais, city, aero, cias


def buscaPais(busca, NomeArquivo):
    existe = False
    dicionario = {"pais":None, "city": [], "aero": [], "cias": None}
    with open(nomeArquivo,"rb") as file:
        while True:
             
            bloco = file.read(dados.size)
            if not bloco:
                break
            pais, city, aero, cias = decodificaDados(bloco)


            if pais ==  busca:
                dicionario["aero"].append(aero)
                dicionario["city"].append(city)
                dicionario["pais"] = pais
                existe = True

    file.close()    

    if not existe:
        print(busca, "não é um país listado na nossa base.")
    else:
        print(f'Os aeroportos de {dicionario["pais"]} são:')
        for i in range(len(dicionario["aero"])):
            print(f'{dicionario["aero"][i]}, {dicionario["city"][i]}')




def buscaAero(busca, nomeArquivo):
    dicionario = {"pais":None, "city": None, "aero": None, "cias": []}
    existe = False
    with open(nomeArquivo,"rb") as file:
        while True:
             
            bloco = file.read(dados.size)
            if not bloco:
                break
            pais, city, aero, cias = decodificaDados(bloco)

            if aero ==  busca:
                existe = True
                cia = cias.split("&")
                dicionario["pais"] = pais
                dicionario["city"] = city
                dicionario["aero"] = aero
                for i in cia:
                    dicionario["cias"].append(i)
                
    file.close()    

    if not existe:
        print(busca, "não é um aeroporto listado na nossa base.")
    else:
        print(f'As cias aéreas que operam para {dicionario["aero"]}, {dicionario["city"]} - {dicionario["pais"]}, são:')
        for i in dicionario["cias"]:
            print(f'{i}')




def buscaCia(busca, nomeArquivo):
    dicionario = {"pais":[], "city": [], "aero": [], "cias": None}
    existe = False
    with open(nomeArquivo,"rb") as file:
        while True:
             
            bloco = file.read(dados.size)
            if not bloco:
                break
            pais, city, aero, cias = decodificaDados(bloco)
            
            for i in cias.split("&"):
                if i.replace("\0","").strip() == busca:
                    existe = True
                    dicionario["cias"] = busca
                    dicionario["aero"].append(aero)
                    dicionario["city"].append(city)
                    dicionario["pais"].append(pais)
                
    file.close()    

    if not existe:
        print(f'A companhia aérea {busca} não opera para nenhum dos aeroportos da base ou digitou errado.')
    else:
        print(f'A companhia aérea {dicionario["cias"]} opera para os aeroportos:')
        for i in range(len(dicionario["aero"])):
            print(f'{dicionario["aero"][i]}, {dicionario["city"][i]}, {dicionario["pais"][i]}')




nomeArquivo = input()
entrada = input()
busca = input()
entrada = entrada.lower()

try:
    codifica(nomeArquivo)
    if entrada == "país":
        buscaPais(busca, nomeArquivo)

    if entrada == "aeroporto":
        buscaAero(busca, nomeArquivo)

    if entrada == "cia":
        buscaCia(busca, nomeArquivo)
except IOError:
    print("Um dos arquivos não foi encontrado ou digitou errado.")
