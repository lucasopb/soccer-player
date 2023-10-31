resp =''
resp2 = 0
player = {}
time = []
golsli = []
while resp != 'N':
    player['name'] = input('name of the player:')
    partidas = int(input('how many games he played?'))
    for c in range(0,partidas):
        golsli.append(int(input(f'how many gols he did on game {c + 1}:')))
    player['gols'] = golsli[:]
    player['total'] = sum(golsli)
    golsli.clear()
    time.append(player.copy())
    resp = input('want continue?[S/N]').upper()
    while resp != 'S' and resp != 'N':
        resp = input('invalid caracter. type S or N').upper()
print('=-' * 30)
print(f'{"cod":<4}{"name":<11}{"gols":<18}total')
for i,e in enumerate(time):
    print(f'{i:.<4}{str(e["name"]):.<11}{str(e["gols"]):.<18}{str(e["total"])}')
while resp2 != 999:
    resp2 = int(input('show data of whitch player? (999 to end)'))
    for i,c in enumerate(time):
        if i == resp2:
            print(f'{e["name"]} player data collection')
            for i,v in enumerate(c['gols']):
                print(f'in game {i + 1} he did {v} gols')
print('finished')

        
            