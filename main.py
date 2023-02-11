#---------- Definir la función principal ----------
def main():
  #---------- Definir un dicccionario con los estados ----------
  states = {
      'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
      'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15
  }
  # print('Diccionario de estados: {}'.format(states))

  #---------- Definir una lista con las acciones que podrá tomar nuestro agente ----------
  actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  # print('Lista de acciones: {}'.format(actions))

  #---------- Definir una matriz donde la recompenza es 1 al hacer una transicion valida y cero en una que no es posible ----------
  rewards = [ #A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#A
              [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#B
              [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#C
              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],#D
              [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#E
              [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],#F
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],#G
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],#H
              [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#I
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],#J
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],#K
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],#L
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],#M
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],#N
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],#O
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0] #P
            ]

  #---------- Llamar a la funcion para mostrar las transiciones ----------
  show_transitions(states, rewards)

#---------- Definir una función para mostar los nodos y sus transiciones ----------
def show_transitions(states, rewards):
  for state in states:
    actualState = states[state]
    transitionList = []
    for transitionIndex, transitions in enumerate(rewards[actualState]):
      if transitions == 1:
        transitionList.append(list(states.keys())[list(states.values()).index(transitionIndex)])

    print('{} puede ir a: {}'.format(state, transitionList))

#---------- Llamar a la funcion principal ----------
if __name__ == '__main__':
    main()