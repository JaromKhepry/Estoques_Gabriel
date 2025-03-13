import unicodedata
import random
import json
import string

lojas = [
    "Jose Walter - Nova loja", "Loja Aeroporto - Teresina", "Loja Anjo da Guarda", "Loja Aquiraz",
    "Loja Aracati", "Loja Barbalha", "Loja Boa Esperanca - EFATS", "Loja Boa Ventura",
    "Loja Boa Viajem", "Loja Bom Jardim", "Loja Buena Vista", "Loja Caetes", "Loja Cambeba",
    "Loja Candeias", "Loja Carrefour", "Loja Cascavel", "Loja Cidade 2000", "Loja Cohatrac V",
    "Loja Cometa Sao Paulo", "Loja Cometa Washington Soares", "Loja Conceito", "Loja Conj Ceara",
    "Loja Conjunto Ceara II", "Loja Cristo Rei", "Loja Diniz", "Loja Dirceu PI", "Loja EFA Barra Mall",
    "Loja EFA Beberibe", "Loja EFA Cajazeiras", "Loja EFA Coco", "Loja EFA Fortim", "Loja EFA Itaoca Mall",
    "Loja EFA Joao Pessoa", "Loja EFA Mateus Jose Walter", "Loja EFA Messejana P. Matriz",
    "Loja EFA Mossoro II", "Loja EFA Pacajus II", "Loja EFA Parangaba", "Loja EFA Patio Castelao",
    "Loja EFA Praca do Romeiro", "Loja EFA Russas", "Loja EFA Sao Joao", "Loja EFA Via Sul",
    "Loja EFATS Shopping Sul", "Loja EFF Baturite", "Loja EFF Caninde", "Loja EFF Redencao",
    "Loja EMHD Acarau", "Loja EMHD Itapipoca", "Loja EMHD Parnaiba", "Loja EMHD Quixada",
    "Loja EMHD Quixeramobim", "Loja EMHD Sobral I", "Loja EMHD Trairi", "Loja EWR Caiuca",
    "Loja EWR Salgado", "Loja FIFE Boa Viagem", "Loja FIFE Candeias II", "Loja FIFE Garapu",
    "Loja FIFE Santo Agostinho", "Loja FIFE Shopping Recife", "Loja Francisco Sa",
    "Loja Frosty Abreu e Lima", "Loja Frosty Igarassu", "Loja Frosty Olinda", "Loja Frosty Primavera",
    "Loja Frosty Sobral I", "Loja Genibau", "Loja Granja Portugal", "Loja Guadalajara - Caucaia",
    "Loja Ibura", "Loja Ibura II", "Loja Igarassu", "Loja Iguatu", "Loja Itapipoca", "Loja Janga",
    "Loja Joquei", "Loja Juazeiro", "Loja Juazeiro CE", "Loja Kennedy PI", "Loja Lago Jacarey",
    "Loja Limoeiro do Norte", "Loja Mangabeira - EFATS", "Loja Maracanau", "Loja Maracanau shop",
    "Loja Maranguape CE", "Loja Maranguape II", "Loja Maranguape PE", "Loja Maraponga",
    "Loja Messejana", "Loja Mondubim", "Loja Olho dAgua", "Loja Oliveira Paiva", "Loja Outeiro da Cruz",
    "Loja Pacajus", "Loja Palmares", "Loja Parangaba", "Loja Parque Athenas", "Loja Parque Piaui",
    "Loja Parque Sao Jose", "Loja Paulista PE", "Loja Peixinhos", "Loja Piedade", "Loja Pinto Madeira",
    "Loja Pontes Vieira", "Loja Pontes Vieira EFA", "Loja Prazeres", "Loja Presidente Kennedy",
    "Loja Primavera", "Loja Reserva Open Mall", "Loja San Martin", "Loja Santa Tereza",
    "Loja Sao Cristovao", "Loja Sao Joao", "Loja Sao Luis MA", "Loja Sarg Herminio",
    "Loja Sarg Herminio Nova", "Loja Shopping Aldeota", "Loja Shopping Eusebio",
    "Loja Silas Munguba", "Loja Solares", "Loja Tabuleta", "Loja Tiradentes", "Loja Trairi",
    "Loja W Soares"
]



USERS = {}

for loja in lojas:
    username = loja.replace(" ", "_").replace("-", "_").lower()
    password = "Frosty" + ''.join(random.choices(string.digits, k=4))  
    USERS[username] = password


with open("usuariosgerador.json", "w") as json_file:
    json.dump(USERS, json_file, indent=4)

print("Usuários e senhas gerados e salvos em usuarios.json")
