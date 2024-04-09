
#Funcion para crear la estructura
def crearEstructura (names, goals, goals_avoided, assists):
    hockey_mixed= {}
    
    #zip es utilizado para emparejar las diferentes listas y juntarlas despues en un diccionario
    #se crea un diccionario para cada jugador
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        hockey_mixed[name] = {
            "Goles": goal,
            "Goles evitados": goal_avoided,
            "Asistencias": assist
        }
    return hockey_mixed

#Funcion para buscar maximo goleador
def maximoGoleador (hockey_mixed):
    max= -1
    for player in hockey_mixed:
        goals= hockey_mixed[player]['Goles']
        if(goals > max):
            max= goals
            max_goalScorer= player

    return max_goalScorer, max

#Funcion para buscar el mas influyente
def masInfluyente (hockey_mixed):
    max= -1
    max_influential= ''
    for player in hockey_mixed:
        goals= hockey_mixed[player]['Goles']
        goals_avoided= hockey_mixed[player]['Goles evitados']
        assists= hockey_mixed[player]['Asistencias']
        score = (goals * 1.5) + (goals_avoided * 1.25) + (assists * 1)
        score= score /3
        if score > max:
            max= score
            max_influential= player
            
    return max_influential, max

#Funcion para calcular el promedio de goles por partido
def promedioGoles (goals):
    from functools import reduce
    #uso lamba para realizae la suma con los elementos de la lista de goles
    #reduce se usa para aplicar la funcion que tiene lamba a todos los elementos y juntar el resultado de la suma
    suma= reduce(lambda a, b: a + b, goals)

    return(suma/25)

#Funcion para calcular el promedio de goles del goleador
def promedioGoleador (hockey_mixed, player):
    goals= hockey_mixed[player]['Goles']
 
    return goals/25