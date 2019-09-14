#Exercicio 105 - Faça um programa que tenha uma função notas () que pode
#receber várias notas de alunos e vai retornar um dicionário com as
#seguintes informações:
# - quantidade de notas;
# - a maior nota;
# - a menor nota;
# - a média da turma;
# - a situação (opcional).



def notas(*num, sit=False):
    """
    -->> Função que recebe várias notas de alunos, e mostra estatísticas
    da turma juntamente com a situação.
    :param num: recebe as notas da turma
    :param sit: parâmetro opcional que exibe a situação da turma
    :return: retorna um dicionário com a quantidade de notas, maior nota,
    menor nota e média da turma.
    """
    boletim = dict()
    boletim['Quantidade de Notas'] = len(num)
    boletim['Maior Nota'] = max(num)
    boletim['Menor Nota'] = min(num)
    boletim['Média Turma'] = sum(num) / len(num)

    if boletim['Média Turma'] >= 70:
        boletim['Situação'] = 'BOA'
    elif boletim['Média Turma'] <= 50:
        boletim['Situação'] = 'RUIM'
    else:
        boletim['Situação'] = 'RAZOÁVEL'

    return boletim



#Programa Principal
#n = notas(10, 80, 90, 80, 90, sit=True)
#print(f'{n}')
help(notas)