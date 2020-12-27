

# script formata arquivo aptos.txt para formato aptos.csv
# a formatação é feita em dois niveis, primeiro cria uma string em um pre formato e então é aplicado uma
# função, sobre a string gerada, que finaliza a formatação


# função que recebe cada linha do arquivo aptos.txt e formata para o tipo aptos.csv
def formatFile_aptos(line_file):
    new_line = '' # armazena linha formatada
    for ind, char in enumerate(line_file):
        if(ind == 0 and char != ' '): # verifica se o atual caractere é o primeiro e se é diferente de espaço.
            new_line += char
        elif(char != ' ' and char != '\t'): # verifica se o atual caractere é diferente de espaço ou tab
            new_line += char
        elif((ind != len(line_file)-1) and (ind != 0) and line_file[ind+1] != ' '): # verifica se o atual caractere não é o primeiro, se o próximo caractere é diferente de espaço e se o atual caractere não é o útilmo da linha, a ordem dessas operações lógicas é importante.
            new_line += ';'
    return new_line


# finaliza a formatação para csv
def formatString(line):
    new_line = ''
    for ind, char in enumerate(line):
        if(ind == 0 and char == ';'): # elimina ';' em inicio de nova linha
            continue;
        elif(char == ';' and ind != (len(line)-1) and line[ind+1] == ';'): # elimina ';' duplicados
            continue;
        else:
            new_line += char;
    return new_line;
        

    
new_string = [] # armazena string, quase já pronta para o formato csv

# abre arquivo aptos.txt e realiza sua leitura linha por linha
with open('./aptos.txt') as file:
    for line in file:
        new_string.append(formatFile_aptos(line)) # formata linha para csv e concatena com new_file
        
new_file = '' # armazena o arquivo formatado para csv

for a in new_string:
    new_file += formatString(a)

#print(new_file)

#cria arquivo aptos.csv salvando a string new_file, string contendo arquivo formatado
with open('./aptos.csv', 'a') as file:
    file.write(new_file)
    
    
    
# Reference

#[1]https://www.pythoncheatsheet.org/#Reading-and-Writing-Files
#[2]https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python


        
    
