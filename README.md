# consult_flight_with_struct
Os cadastros de aeroportos juntamente com suas localizações e companhias aéreas foram atualizados e você foi contratado para refazer o sistema de consultas. Seu programa deve responder porconsultas tanto sobre países, aeroportos ou companhias aéreas. Seguem abaixo todos os detalhes a serem feitos. 

A entrada é dada por: (1) um arquivo binário codificado de um arquivo texto, (2) tipo deconsulta e (3)nome a ser consultado:

(1) Um arquivo binário:
Implemente a codificação para a geração de um arquivo. bin a partir de um aquivo.txt que contenha as informações: país#cidade#nome_do_aeroporto#cias_aereas_que_operam_nesse_aeroporto_(separadas por &)

O arquivo binário de nome “cliente.bin” é, portanto, composto por uma sequência de registros formados por 4 strings, tais que:

A primeira string ocupa 20 bytes e se refere ao nome do país; 
A segunda string ocupa 50 bytes e se refere ao nome da cidade;
A terceira string ocupa 50 bytes e se refere ao nome do aeroporto;
A quarta string ocupa 100 bytes e se refere aos nomes das cias. aéreas, separadas por &.

(2) Tipo de consulta:
Há três tipos de consultas a serem informados: país; aeroporto; ou cia.

(3) Nome a ser consultado: 
.Caso o tipo de consulta tenha sido algum país que esteja na base de dados, retorne em cada linha o par 'nome do aeroporto', 'cidade'.

.Caso o tipo de consulta tenha sido algum país que não esteja na base de dados, retorne com a informação " 'Nome_consultado' não é um país listado na nossa base.";

.Caso o tipo de consulta tenha sido algum aeroporto que esteja na base de dados, retorne em cada linha os nomes das cias. aéreas que operam neste aeroporto consultado;

.Caso o tipo de consulta tenha sido alguma cia. aérea que esteja na base de dados,retorne em cada linha as informações dos aeroportos que recebem voo da cia aérea, da seguinte forma: nome do aeroporto, cidade, país.

.Caso o cia.
consulta da não esteja na base de dados então retorne a informação" A companhia aérea'Nome_consultado' não opera para nenhum dos aeroportos da base ou digitou errado.".

.Caso o programa receba um arquivo. bin que não esteja no diretório, retorne"Um dos arquivos não foi encontrado ou digitou errado."
