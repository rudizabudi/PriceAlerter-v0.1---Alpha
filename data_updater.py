from config import command_ledger, data_ledger
import data_handler
import time
from yahoofinancials import YahooFinancials

def update_data():
    time.sleep(10)

    print('Update Data started')
    update_timer = 300
    while True:
        print(-1)
        for typegroup in data_ledger.keys():
            print('UpdateData:', data_ledger)
            print(0)
            if typegroup != 'Header':
                print(1)
                print(data_ledger[typegroup])
                if data_ledger[typegroup] not in [None, '']:
                    print(2)
                    for list_name in data_ledger[typegroup].keys():
                        print(3)
                        if data_ledger[typegroup][list_name] is not None:
                            print(4)
                            for stock_name in data_ledger[typegroup][list_name].keys():
                                print(stock_name)
                                print(5)
                                symbol = data_ledger[typegroup][list_name][stock_name]['Symbol']
                                for object in data_ledger[typegroup][list_name][stock_name].keys():
                                    # TODO Add price update for other alerttypes and watchlist here
                                    if 'Alert' in object:
                                        print(6)
                                        if data_ledger[typegroup][list_name][stock_name][object]['Reference'] == 'Price':
                                            print(symbol)
                                            stock_data = YahooFinancials(symbol)
                                            data_ledger[typegroup][list_name][stock_name][object]['Price'] = stock_data.get_stock_price_data(reformat=True)[symbol]['regularMarketPrice']
                                            print(data_ledger[typegroup][list_name][stock_name][object]['Price'])
                                            data_ledger[typegroup][list_name][stock_name][object]['Ratio'] = \
                                                '{}%'.format(round(float(data_ledger[typegroup][list_name][stock_name][object]['Price']) / float(data_ledger[typegroup][list_name][stock_name][object]['Threshold']) * 100, 2))
                                            print(data_ledger[typegroup][list_name][stock_name][object]['Ratio'])
        command_ledger.append({'forceGUIUpdate': None})
        print('Data updated: ', data_ledger)
        time.sleep(60)
