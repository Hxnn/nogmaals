# name of student: Yavuz Alici
# number of student: 99067045
# purpose of program: Giving back the change, in the right ammount and automaticlly choosing which coins.
# function of program:
# structure of program: With questions, ifs,elifs and else. Multiple and different operators and functions.

toPay = int(float(input('Amount to pay: ')))  # toPay is de input en je moet zeggen hoeveel je nog moet betalen
# * 100 want het is in centen.
paid = int(float(input('Paid amount: ')))  # paid is de input en erbij zeggen hoeveel je daardwerkelijk hebt
# betaald * 100 want het is in centen.
change = paid - toPay  # Wisselgeld is hoeveel je hebt betaald - hoeveel je moet betalen.

if change > 0:  # Als je wisselgeld boven 0 is:
    coinValue = 5  # Dan is de waarde 500 cent, oftewel 5 euro.

    while change > 0 and coinValue > 0:  # Terwijl de wisselgeld EN geld waarde boven 0 is:
        nrCoins = change // coinValue  # Wisselgeld gedeeld door geld waarde. En hij rond het af op de dichtbijste
        # hele getal.

        if nrCoins > 0:  # Als nrCoins boven de 0 is
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' euro!')  # Print het maximale coins
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' euro did you return? '))  #
            # Hoeveel geld je terug krijgt, ligt aan hoeveel geld je hebt gegeven en in welke munten.
            change -= nrCoinsReturned * coinValue  # Coinsreturned * value = bedrag. Change is - bedrag en wordt dan
            # change.

        # comment on code below: Als het 5 euro is, ga verder. Als het niet zo is, ga naar 3, als niet zo, ga naar 2
        # etc.
        if coinValue == 500:
            coinValue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

if change > 0:  # Als wisselgeld groter is dan 0, print.
    print('Change not returned: ', str(change) + ' euro')
else:
    print('Finished! You gave back:', str(nrCoins) + ' coin(s)')
