#Faça um programa que tenha uma função notas() que pode receber várias
#notas de alunos e vai retornar um dicionário com as seguintes informações:
# -  quantidade de notas;
# -  a maior nota;
# -  a menor nota;
# -  a média da turma;
# -  a situação (opcional).
#
# Adicione também as docstrings da função.

def notas(*num, sit=False):
    """
    --> Função para analizar notas e situação de vários alunos.
    :param num: recebe uma ou mais notas dos alunos (aceita várias)
    :param sit: opcional, mostra ou não a situação dos alunos (padrão=False).
    :return: retorna um dicionário com quantidade, maior, menor, média da turma
    """
    r = dict()
    r['Total de Notas'] = len(num)
    r['Maior Nota'] = max(num)
    r['Menor Nota'] = min(num)
    r['Média'] = sum(num) / len(num)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


#Programa Principal
resp = notas(3, 5.5, 6.7, 8.9, 7, sit=True)
print(resp)
help(notas)
