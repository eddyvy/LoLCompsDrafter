import data
import utils
import teamMains


TOP_LIST = teamMains.TOPLANER
JUN_LIST = teamMains.JUNGLER
MID_LIST = teamMains.MIDLANER
ADC_LIST = teamMains.ADCARRY
SUP_LIST = teamMains.SUPPORT


# def getAveragePoints(strategy):
#     return data.ALL_DATA.get(strategy)['Average']
def strategyPercentage(champName, strategy):
    return data.ALL_DATA.get(strategy)[champName] / data.ALL_DATA.get('Total2')[champName] * 100


def percentagesList(champName):
    return [
        strategyPercentage(champName, 'Attack'),
        strategyPercentage(champName, 'Catch'),
        strategyPercentage(champName, 'Protect'),
        strategyPercentage(champName, 'Siege'),
        strategyPercentage(champName, 'Split')
    ]

def flexibilityPoints(champName):
    return utils.desTipica(percentagesList(champName))


def champDic(champName):
    champ = {}
    champ['name'] = champName
    champ['flexibility'] = flexibilityPoints(champName)
    champ['percAttack'] = strategyPercentage(champName, 'Attack')
    champ['percCatch'] = strategyPercentage(champName, 'Catch')
    champ['percProtect'] = strategyPercentage(champName, 'Protect')
    champ['percSiege'] = strategyPercentage(champName, 'Siege')
    champ['percSplit'] = strategyPercentage(champName, 'Split')
    for param in data.DATA_PARAMS:
        if data.ALL_DATA.get(param)[champName]:
            champ[param] = float(data.ALL_DATA.get(param)[champName])

    return champ

def getListDicChamps(champNameList):
    returningList = []
    for champName in champNameList:
        champ = champDic(champName)
        returningList.append(champ)
    return returningList


def teamDicOfLists():
    return {
        'top': getListDicChamps(TOP_LIST),
        'jun': getListDicChamps(JUN_LIST),
        'mid': getListDicChamps(MID_LIST),
        'adc': getListDicChamps(ADC_LIST),
        'sup': getListDicChamps(SUP_LIST)
    }


def bestChampsFor(strategy, fromSmallToBig = False):
    if fromSmallToBig :
        for player in teamDicOfLists():
            orderedChamps = utils.orderSmallBig(teamDicOfLists()[player], strategy)
            orderedChampNames = []
            for champ in orderedChamps:
                orderedChampNames.append(champ['name'] + '(' + str(round(champ[strategy], 3)) + ')')
            print('--',player,'--')
            print(*orderedChampNames[:20], sep=', ')
    else:
        for player in teamDicOfLists():
            orderedChamps = utils.orderBigSmall(teamDicOfLists()[player], strategy)
            orderedChampNames = []
            for champ in orderedChamps:
                orderedChampNames.append(champ['name'] + '(' + str(round(champ[strategy], 3)) + ')')
            print('--',player,'--')
            print(*orderedChampNames[:20], sep=', ')
    

def showPercentages(champList):
    sumaAttack = 0
    sumaCatch = 0
    sumaProtect = 0
    sumaSiege = 0
    sumaSplit = 0

    for champ in champList:
        sumaAttack += champ['Attack']
        sumaCatch += champ['Catch']
        sumaProtect += champ['Protect']
        sumaSiege += champ['Siege']
        sumaSplit += champ['Split']

    sumaTotal = sumaAttack + sumaCatch + sumaProtect + sumaSiege + sumaSplit

    percAttack = round(sumaAttack / sumaTotal * 100)
    percCatch = round(sumaCatch / sumaTotal * 100)
    percProtect = round(sumaProtect / sumaTotal * 100)
    percSiege = round(sumaSiege / sumaTotal * 100)
    percSplit = round(sumaSplit / sumaTotal * 100)

    print('Attack:', percAttack, '% ---- Pierde: Catch, Protect - Gana: Siege, Split')
    print('Catch:', percCatch, '% ---- Pierde: Protect, Siege - Gana: Attack, Split')
    print('Protect:', percProtect, '% ---- Pierde: Siege, Split - Gana: Attack, Catch')
    print('Siege:', percSiege, '% ---- Pierde: Attack, Split - Gana: Catch, Protect')
    print('Split:', percSplit, '% ---- Pierde: Attack, Catch - Gana: Protect, Siege')
        


def draft():
    blueTeam = []
    redTeam = []

    print('1.Blue 2.Red')
    team = input()
    
    if team == '1':
        print('Buenos first Picks: ')
        bestChampsFor('flexibility', True)
    blueTeam.append(champDic(input('blue 1: ')))
    showPercentages(blueTeam)

    if team == '2':
        print('Buenos first Picks: ')
        bestChampsFor('flexibility', True)
    redTeam.append(champDic(input('red 1: ')))
    redTeam.append(champDic(input('red 2: ')))
    showPercentages(redTeam)

    if team == '1':
        buscando = input('Que buscas? Attack, Catch, Protect, Siege, Split: ')
        bestChampsFor(buscando)
    blueTeam.append(champDic(input('blue 2: ')))
    blueTeam.append(champDic(input('blue 3: ')))
    showPercentages(blueTeam)

    if team == '2':
        buscando = input('Que buscas? Attack, Catch, Protect, Siege, Split: ')
        bestChampsFor(buscando)
    redTeam.append(champDic(input('red 3: ')))
    redTeam.append(champDic(input('red 4: ')))
    showPercentages(redTeam)

    if team == '1':
        buscando = input('Que buscas? Attack, Catch, Protect, Siege, Split: ')
        bestChampsFor(buscando)
    blueTeam.append(champDic(input('blue 4: ')))
    blueTeam.append(champDic(input('blue 5: ')))
    showPercentages(blueTeam)

    if team == '2':
        buscando = input('Que buscas? Attack, Catch, Protect, Siege, Split: ')
        bestChampsFor(buscando)
    redTeam.append(champDic(input('red 5: ')))
    showPercentages(redTeam)


draft()

# blueTeam = [
#     champDic('Ornn'),
#     champDic('Leona')
# ]

# showPercentages(blueTeam)
# def flexibilityList():
#     for player in teamDicOfLists():


#     getAveragePoints('Attack')


# print('Attack')
# bestChampsFor('Attack')
# print('Catch')
# bestChampsFor('Catch')
# print('Protect')
# bestChampsFor('Protect')
# print('Siege')
# bestChampsFor('Siege')
# print('Split')
# bestChampsFor('Split')

# print('percAttack')
# bestChampsFor('percAttack')

# print('flexibility')
# bestChampsFor('flexibility', True)
