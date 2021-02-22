from config import command_ledger, data_ledger
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from yahoofinancials import YahooFinancials
from dicttoxml import dicttoxml
import xmltodict
from xml.dom.minidom import parseString
import data_updater
import threading
import windows.popups.popup_handler as ph


'''
*** command_ledger Documentation:
command_ledger = [{command_type1: [parameter1, parameter2]}, {command_type2: [parameter1, parameter2, parameter3]}]
Format Documentation:
    Add new alert:
        Type: Price reference/type
            {'addAlert': [watchlist, name, symbol, reference, operator, threshold]}
    Add alert list:
        {'addList': ['Alert', listname]}
    Delete alert list:
        {'deleteList': ['Alert', [listname1, listname2, ...]]} 
    Save lists to file:
        {'savetofile': filepath)
    Open list from file:
        {'openfile': filepath}
    Create new list:
        {'new': None}
    Switch list view:
        {'changeList': [listtype, listname]}
    Force GUI update:
        {'forceGUIUpdate': None}

Format:
self.data_ledger =   [{  Header:         {Misc. Information}                            },
                {Alertlists:
                    {   Alertlist1:     {Stockname: [{XYZ}, {XYZ}], Stockname: [{XYZ}]  },
                    {   Alertlist2:     {Stockname: [{XYZ}], Stockname: [{XYZ}]         }},
                {Watchlist:
                    {   Watchlist1:     {Stockname: [{ABC}, {ABC}]                      }}                     
                ]

*** self.data_ledger Documentation:
    Alertlist:
        self.data_ledger =
            {   Header: {'active': {'activeListtype': listtype,'activeListname': listname}},
                Alertlists:                
                    {   AlertlistName:
                        { Coca Cola:
                            {       Symbol: CO,
                                    Alert1:  *** TYPE PRICE EXAMPLE ***
                                        {
                                            Reference: Price,
                                            Operator: Over,
                                            Threshold: 53,
                                            Price: 47,
                                            Ratio: 0.987
                                        },
                                    Alert2:
                                        {
                                            Reference: Price,
                                            Operator: Under,
                                            Threshold: 42,
                                            Price: 47,
                                        }
                            }
                        }
                    },
                Watchlists:
                    {
                    }
            }
'''


# noinspection SpellCheckingInspection
class DataHandler():
    def __init__(self, root_ui):
        #load previous lists or load default self.data_ledger
        self.data_ledger = {'Header': {'active': {'activeListtype': None, 'activeListname': None}},
                            'Alertlists':   {},
                            'Watchlists':   {}
                            }

        update_timer = 300
        ud_thread = threading.Thread(target=self.update_data, name='Data Updater', args=(update_timer,))
        ud_thread.start()
        #TODO change on autoload
        self.current_file_path = ''

        print('DataHandler initialized')


    def logic_loop(self, root_ui):

        while True:
            def process_new_commands():
                if command_ledger:
                    for command in list(command_ledger):
                        print('Command:', command)
                        if str(list(command.keys())[0]) == 'addAlert':
                            if self.data_ledger['Alertlists'][command['addAlert'][0]] is None or command['addAlert'][1] not in self.data_ledger['Alertlists'][command['addAlert'][0]].keys():
                                self.data_ledger['Alertlists'][command['addAlert'][0]][command['addAlert'][1]] = {}
                                self.data_ledger['Alertlists'][command['addAlert'][0]][command['addAlert'][1]]['Symbol'] = command['addAlert'][2]
                                self.data_ledger['Alertlists'][command['addAlert'][0]][command['addAlert'][1]]['Price'] = ' - - - '

                            new_list_count = sum('Alert' in s for s in list(self.data_ledger['Alertlists'][command['addAlert'][0]][command['addAlert'][1]].keys())) + 1
                            self.data_ledger['Alertlists'][command['addAlert'][0]][command['addAlert'][1]]['Alert{}'.format(new_list_count)] = \
                                                            {
                                                                'Reference':    command['addAlert'][3],
                                                                'Operator':     command['addAlert'][4],
                                                                'Threshold':    command['addAlert'][5],
                                                                'Ratio':        None,
                                                            }
                            self.update_sleep = True
                            update_gui()

                        elif str(list(command.keys())[0]) == 'addList':
                            # TODO Add watchlists here
                            if command['addList'][0] == 'Alert':
                                self.data_ledger['Alertlists'][command['addList'][1].replace(' ', '_')] = {}
                                if None in self.data_ledger['Header']['active']:
                                    self.data_ledger['Header']['active'] = {'activeListtype': 'Alertlists', 'activeListname': command['addList'][1].replace(' ', '_')}
                            update_gui()

                        elif str(list(command.keys())[0]) == 'deleteList':
                            # TODO Add watchlists here
                            if command['deleteList'][0] == 'Alert':
                                for list_to_delete in command['deleteList'][1]:
                                    del self.data_ledger['Alertlists'][list_to_delete.replace(' ', '_')] # TODO TEST THIS
                                    if list_to_delete.replace(' ', '_') == self.data_ledger['Header']['active']['activeListname']:
                                        self.data_ledger['Header']['active']['activeListtype'] = 'Alertlists'
                                        self.data_ledger['Header']['active']['activeListname'] = root_ui.listWidget_alertlists.item(0).text().replace(' ', '_')
                            update_gui()

                        elif str(list(command.keys())[0]) == 'save':
                            if self.current_file_path == '':
                                ph.popup_triggers('savetofile', root_ui=root_ui)
                            else:
                                save_file_dict = parseString(dicttoxml(self.data_ledger, attr_type=False))
                                f = open(self.current_file_path, 'w', encoding='utf-8')
                                f.write(save_file_dict.toprettyxml())
                                f.close()

                        elif str(list(command.keys())[0]) == 'savetofile':
                            if not command['savetofile'] == '':
                                self.current_file_path = command['savetofile']
                                save_file_dict = parseString(dicttoxml(self.data_ledger, attr_type=False))
                                f = open(command['savetofile'], 'w', encoding='utf-8')
                                f.write(save_file_dict.toprettyxml())
                                f.close()

                        elif str(list(command.keys())[0]) == 'openfile':
                            if not command['openfile'] == '':
                                self.current_file_path = command['openfile']
                                f = open(command['openfile'], 'r', encoding='utf-8')
                                self.data_ledger = dict(xmltodict.parse(f.read(), process_namespaces=False, dict_constructor=dict))['root']
                                f.close()
                                self.update_sleep = True
                                update_gui()

                        elif str(list(command.keys())[0]) == 'new':
                            self.current_file_path = None
                            self.data_ledger = {'Header': {'active': {'activeListtype': None, 'activeListname': None}},
                                                'Alertlists': {},
                                                'Watchlists': {}
                                                }
                            update_gui()

                        elif str(list(command.keys())[0]) == 'changeList':
                            self.data_ledger['Header']['active'] = {'activeListtype': command['changeList'][0], 'activeListname': (command['changeList'][1].text().replace(' ', '_'))}
                            update_gui()

                        elif str(list(command.keys())[0]) == 'forceGUIUpdate':
                            update_gui()

                        command_ledger.remove(command)

            process_new_commands()

            def update_gui():
                #TODO Color or bold active list in listwidget
                print('Updating Gui')
                root_ui.listWidget_alertlists.clear()
                [root_ui.listWidget_alertlists.addItem(listname.replace('_', ' ')) for listname in self.data_ledger['Alertlists'].keys()]
                [root_ui.listWidget_alertlists.item(i).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) for i in range(root_ui.listWidget_alertlists.count())]


                rowcount = 0
                table_insert = []
                last_stock = None
                if self.data_ledger['Header']['active']['activeListtype'] is not None and self.data_ledger['Header']['active']['activeListname'] is not None:
                    if self.data_ledger[self.data_ledger['Header']['active']['activeListtype']][self.data_ledger['Header']['active']['activeListname']] is not None:
                        for stock in self.data_ledger[self.data_ledger['Header']['active']['activeListtype']][self.data_ledger['Header']['active']['activeListname']]:
                            for object in self.data_ledger[self.data_ledger['Header']['active']['activeListtype']][self.data_ledger['Header']['active']['activeListname']][stock].keys():
                                if 'Alert' in object: #TODO And Reference == Price, for other types
                                    rowcount += 1
                                    alert_info = self.data_ledger[self.data_ledger['Header']['active']['activeListtype']][self.data_ledger['Header']['active']['activeListname']][stock][object]
                                    price = self.data_ledger[self.data_ledger['Header']['active']['activeListtype']][self.data_ledger['Header']['active']['activeListname']][stock]['Price']
                                    condition = '{} {}'.format(alert_info['Operator'], alert_info['Threshold'])
                                    table_insert.append([stock if stock != last_stock else '', condition, price, alert_info['Ratio']])
                                    last_stock = stock

                        root_ui.tableWidget_listDisplay.setRowCount(rowcount)
                        for row in range(rowcount):
                            for column in range(root_ui.tableWidget_listDisplay.columnCount()):
                                root_ui.tableWidget_listDisplay.setItem(row, column, QtWidgets.QTableWidgetItem(str(table_insert[row][column])))
                                # if str(table_insert[row][column]) == '':
                                #     root_ui.tableWidget_listDisplay.item(row, column).setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                #     print(row, column)
                                font = QtGui.QFont()
                                font.setFamily('Roboto')
                                font.setPointSize(12)
                                font.setWeight(75)
                                root_ui.tableWidget_listDisplay.item(row, column).setFont(font)
                                root_ui.tableWidget_listDisplay.item(row, column).setForeground(QtGui.QColor(234, 230, 228))
                                if column in [0, 1]:
                                    root_ui.tableWidget_listDisplay.item(row, column).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                                elif column in [2, 3]:
                                    root_ui.tableWidget_listDisplay.item(row, column).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                                if row % 2 == 0:
                                    root_ui.tableWidget_listDisplay.item(row, column).setBackground(QtGui.QColor(81, 81, 81))
                else:
                    rowcount = 0
                    root_ui.tableWidget_listDisplay.setRowCount(rowcount)

                root_ui.tableWidget_listDisplay.setGeometry(QtCore.QRect(190, 70, 621, 30 + (rowcount * 30)))

            time.sleep(0.2)
            #     root_ui.tableWidget_Alert.setItem(entry_row, counter, QtWidgets.QTableWidgetItem(command['addAlert'][counter]))

    def update_data(self, update_timer):
        time.sleep(10)

        while True:
            try:
                for typegroup in self.data_ledger.keys():
                    if typegroup != 'Header':
                        if self.data_ledger[typegroup] not in [None, '']:
                            for list_name in self.data_ledger[typegroup].keys():
                                if self.data_ledger[typegroup][list_name] is not None:
                                    for stock_name in self.data_ledger[typegroup][list_name].keys():
                                        symbol = self.data_ledger[typegroup][list_name][stock_name]['Symbol']
                                        for object in self.data_ledger[typegroup][list_name][stock_name].keys():
                                            # TODO Add price update for other alerttypes and watchlist here
                                            if 'Alert' in object:
                                                if self.data_ledger[typegroup][list_name][stock_name][object]['Reference'] == 'Price':
                                                    stock_data = YahooFinancials(symbol)
                                                    self.data_ledger[typegroup][list_name][stock_name]['Price'] = stock_data.get_stock_price_data(reformat=True)[symbol]['regularMarketPrice']
                                                    self.data_ledger[typegroup][list_name][stock_name][object]['Ratio'] = \
                                                        '{}%'.format(round(float(self.data_ledger[typegroup][list_name][stock_name]['Price']) / float(self.data_ledger[typegroup][list_name][stock_name][object]['Threshold']) * 100, 2))
                                                    command_ledger.append({'forceGUIUpdate': None})

            except RuntimeError:
                continue
            except KeyError:
                break


            self.update_sleep = True
            while self.update_sleep:
                for i in range(update_timer):
                    if self.update_sleep:
                        time.sleep(1)
                self.update_sleep = False

















