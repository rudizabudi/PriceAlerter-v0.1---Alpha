from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os

from config import command_ledger, data_ledger
import windows.popups.add_alert_popup_first as aapf
import windows.popups.add_alert_popup_second as aaps
import windows.popups.add_watch_popup as awp
import windows.popups.add_alertlist_popup as aalp
import windows.popups.add_watchlist_popup as awlp
import windows.popups.add_type_selection as ats
import windows.popups.settings as stg


def popup_triggers(window_name, root_ui=None, popup_ui=None, popup=None, params=None):

    if window_name == 'addTypeSelection':
        #TODO Move to popup handler
        add_type_popup = QtWidgets.QMainWindow()
        add_type_ui = ats.Ui_Form()
        add_type_ui.setupUi(add_type_popup)
        add_type_popup.show()

        add_type_ui.toolButton_alertAdd.clicked.connect(lambda: popup_triggers('addAlertOne', root_ui=root_ui, popup=add_type_popup))
        add_type_ui.toolButton_watchAdd.clicked.connect(lambda: popup_triggers('addWatch', root_ui=root_ui, popup=add_type_popup))

    elif window_name == 'addAlertList':
        global alertlist_popup
        alertlist_popup = QtWidgets.QMainWindow()
        alertlist_ui = aalp.Ui_Form()
        alertlist_ui.setupUi(alertlist_popup)
        alertlist_popup.show()

        alertlist_ui.lineEdit_NewAlertName.returnPressed.connect(lambda: command_ledger.append({'addList': ['Alert', alertlist_ui.lineEdit_NewAlertName.text()]}))
        alertlist_ui.lineEdit_NewAlertName.returnPressed.connect(lambda: alertlist_popup.close())
        alertlist_ui.pushButton_Add.clicked.connect(lambda: command_ledger.append({'addList': ['Alert', alertlist_ui.lineEdit_NewAlertName.text()]}))
        alertlist_ui.pushButton_Add.clicked.connect(lambda: alertlist_popup.close())
        alertlist_ui.pushButton_Cancel.clicked.connect(lambda: alertlist_popup.close())

    elif window_name == 'addWatchList':
        global watchlist_popup
        watchlist_popup = QtWidgets.QMainWindow()
        watchlist_ui = awlp.Ui_Form()
        watchlist_ui.setupUi(watchlist_popup)
        watchlist_popup.show()

        watchlist_ui.lineEdit_NewWatchName.returnPressed.connect(lambda: command_ledger.append({'addList': ['Watch', watchlist_ui.lineEdit_NewWatchName.text()]}))
        watchlist_ui.lineEdit_NewWatchName.returnPressed.connect(lambda: watchlist_popup.close())
        watchlist_ui.pushButton_Add.clicked.connect(lambda: command_ledger.append({'addList': ['Watch', watchlist_ui.lineEdit_NewWatchName.text()]}))
        watchlist_ui.pushButton_Add.clicked.connect(lambda: watchlist_popup.close())
        watchlist_ui.pushButton_Cancel.clicked.connect(lambda: watchlist_popup.close())

    elif window_name == 'addAlertOne':
        popup.close()
        global alert_first_popup
        alert_first_popup = QtWidgets.QMainWindow()
        alert_ui = aapf.Ui_Form()
        alert_ui.setupUi(alert_first_popup)
        alert_first_popup.show()

        alert_ui.comboBox_alertlistSelect.clear()
        alert_ui.comboBox_alertlistSelect.addItems([root_ui.listWidget_alertlists.item(i).text() for i in range(root_ui.listWidget_alertlists.count())])
        alert_ui.pushButton_Continue.clicked.connect(lambda: alert_first_popup.close())

    elif window_name == 'addWatch':
        popup.close()
        global watch_popup
        watch_popup = QtWidgets.QMainWindow()
        watch_ui = awp.Ui_Form()
        watch_ui.setupUi(watch_popup)
        watch_popup.show()

        watch_ui.comboBox_watchlistSelect.clear()
        watch_ui.comboBox_watchlistSelect.addItems([root_ui.listWidget_watchlists.item(i).text() for i in range(root_ui.listWidget_watchlists.count())])
        watch_ui.pushButton_Continue.clicked.connect(lambda: command_ledger.append({'addWatch': [watch_ui.comboBox_watchlistSelect.currentText(), watch_ui.lineEdit_name.text(), watch_ui.lineEdit_symbol.text()]}))
        watch_ui.pushButton_Continue.clicked.connect(lambda: watch_popup.close())

    elif window_name == 'addAlertTwo':
        popup_ui.pushButton_Continue.clicked.connect(lambda: add_alert_second(popup_ui.comboBox_alertlistSelect.currentText(), popup_ui.lineEdit_name.text(), popup_ui.lineEdit_symbol.text()))

        def add_alert_second(alertlist, name, symbol):
            popup.close()
            global alert_second_popup
            alert_second_popup = QtWidgets.QMainWindow()
            alert_second_ui = aaps.Ui_Form()
            alert_second_ui.setupUi(alert_second_popup)
            alert_second_popup.show()

            alert_second_ui.toolButton_thresholdAdd.clicked.connect(lambda: modify_threshold_amount(1))
            alert_second_ui.toolButton_thresholdDelete.clicked.connect(lambda: modify_threshold_amount(-1))

            def modify_threshold_amount(command):
                vis_counter = 0
                if command == 0:
                    for i in range(2, 6):
                        for obj in ['label_alert', 'comboBox_reference', 'comboBox_operator', 'lineEdit_threshold']:
                            getattr(alert_second_ui, '{}{}'.format(obj, i)).hide()
                    alert_second_ui.toolButton_thresholdDelete.hide()
                else:
                    for i in range(1, 6):
                        label = getattr(alert_second_ui, 'label_alert{}'.format(i))
                        if label.isVisible():
                            vis_counter += 1
                    if command == 1:
                        if vis_counter < 5:
                            alert_second_ui.toolButton_thresholdAdd.show()
                            for obj in ['label_alert', 'comboBox_reference', 'comboBox_operator', 'lineEdit_threshold']:
                                getattr(alert_second_ui, '{}{}'.format(obj, vis_counter + command)).show()
                                alert_second_ui.toolButton_thresholdDelete.show()
                            if vis_counter == 4:
                                alert_second_ui.toolButton_thresholdAdd.hide()
                    if command == -1:
                        if vis_counter > 0:
                            alert_second_ui.toolButton_thresholdDelete.show()
                            for obj in ['label_alert', 'comboBox_reference', 'comboBox_operator', 'lineEdit_threshold']:
                                getattr(alert_second_ui, '{}{}'.format(obj, vis_counter)).hide()
                                alert_second_ui.toolButton_thresholdAdd.show()
                            if vis_counter == 2:
                                alert_second_ui.toolButton_thresholdDelete.hide()

            modify_threshold_amount(0)
            alertlist = alertlist.replace(' ', '_')
            alert_second_ui.pushButton_Continue.clicked.connect(lambda: process_new_alerts(alertlist, name, symbol))

            def process_new_alerts(alertlist, name, symbol):
                vis_counter = 0
                for i in range(1, 6):
                    label = getattr(alert_second_ui, 'label_alert{}'.format(i))
                    if label.isVisible():
                        vis_counter += 1

                control_counter = 0
                for i in range(1, vis_counter + 1):
                    if getattr(alert_second_ui, 'comboBox_reference{}'.format(i)).currentText() == 'Price' and getattr(alert_second_ui, 'lineEdit_threshold{}'.format(i)).text() != '':
                        control_counter += 1
                    #TODO: Add other reference types here

                try:
                    if vis_counter == control_counter:
                        # for price reference
                        for i in range(1, vis_counter + 1):
                            if getattr(alert_second_ui, 'comboBox_reference{}'.format(i)).currentText() == 'Price':
                                reference = getattr(alert_second_ui, 'comboBox_reference{}'.format(i)).currentText()
                                operator = getattr(alert_second_ui, 'comboBox_operator{}'.format(i)).currentText()
                                threshold = getattr(alert_second_ui, 'lineEdit_threshold{}'.format(i)).text()
                                command = {'addAlert': [alertlist, name, symbol, reference, operator, threshold]}
                                command_ledger.append(command)
                                alert_second_popup.close()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setWindowTitle('Fail!')
                        msg.setText('Inputs seem to contain no or flawed data.')
                        x = msg.exec_()

                except Exception as e:
                    print(e)

    elif window_name == 'settings':
        global settings_popup
        settings_popup = QtWidgets.QMainWindow()
        settings_ui = stg.Ui_Form()
        settings_ui.setupUi(settings_popup)
        settings_popup.show()



        def show_settings_page(page):
            for child in settings_popup.children():
                if child.objectName() not in ['_layout', 'treeWidget', 'pushButton_ApplyClose', 'pushButton_Cancel'] and page not in child.objectName():
                    print(child.objectName(), ' hidden.')
                    child.hide()

        show_settings_page('alerts_mobile')




    elif window_name == 'savetofile':

        filename = QFileDialog.getSaveFileName(root_ui, 'Save Lists', os.getcwd(), filter=('PriceWatcher (*.xml)'))[0]
        command_ledger.append({'savetofile': filename})

    elif window_name == 'openfile':
        filename = QFileDialog.getOpenFileName(root_ui, 'Open saved Lists', os.getcwd(), filter=('PriceWatcher (*.xml)'))[0]
        command_ledger.append({'openfile': filename})

















