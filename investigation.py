# encoding: utf-8
import random


def validation_theory(theory, msg):
    """ Checks if theory length is 3 and if all elements are digits, if fail, a new input is needed """
    return theory if len(theory) == 3 and ''.join(theory).isdigit() else validation_theory(input(msg).split(','),msg)

def investigate(theory, solution):
    """ Checks if one or more elements are different from solution and return one of them or 0 """
    errors = list(i+1 for i in range(0,3) if solution[i] != theory[i])
    return random.choice(errors) if errors else 0

if __name__ == '__main__':

    order_suspects = ('Assassins','Places','Weapons')
    fail_attempts = {'Assassins':[],'Places':[],'Weapons':[]}

    solution = validation_theory(input('Testemunha, registre os dados do caso, quem foi, onde foi e com qual arma? ').split(','),'Solução inválida, digite uma solução válida: ')

    response_ = 1

    while response_ != 0:

        print('Tentativas feitas {}\n'.format(fail_attempts))
        theory = validation_theory(input('Digite a teoria: ').split(','),'Teoria Inválida, digite uma teoria válida: ')
        response_ = investigate(theory,solution)
        fail_attempts[order_suspects[response_-1]].append(int(theory[response_-1]))


    print('Parabéns, você solucionou o caso!')
