from random import randint
def choose():
    print('ai choosin')
    ai=randint(1,3)
    if ai==1:
        aichoose='rock'
    if ai==2:
        aichoose='papar'
    if ai==3:
        aichoose='scisorz'
    print('ai chosein')
    print("ur turn to chosin")
    player=input('rock,papar,scisorz?: ')
    if player=='rock':
        playerchoise='rock'
    if player=='papar':
        playerchoise='papar'
    if player=='scisorz':
        playerchoise='scisorz'
    print('time to battle (: epic)))')
    if playerchoise=='rock' and aichoose=='rock':
        print('everyone loses):')
    if playerchoise=='rock' and aichoose=='papar':
        print('ai wins')
    if playerchoise=='rock' and aichoose=='scisorz':
        print('u win')
    if playerchoise=='papar' and aichoose=='rock':
        print('u win')
    if playerchoise=='papar' and aichoose=='papar':
        print('every1 loses')
    if playerchoise=='papar' and aichoose=='scisorz':
        print('u die):')
    if playerchoise=='scisorz' and aichoose=='rock':
        print('u die):')
    if playerchoise=='scisorz' and aichoose=='papar':
        print('u win')
    if playerchoise=='scisorz' and aichoose=='scisorz':
        print('every1 loses')
    print("your choice was " + playerchoise + ". and ai choice was " + aichoose)
while True:
    choose()
