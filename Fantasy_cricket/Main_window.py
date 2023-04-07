# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from SqliteDataManager import DataManager

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from NewTeam import Ui_Dialog as DialogN
from SelectTeam import Ui_Dialog as DialogS
from evaluate_Score import Ui_MainWindow as Evaluatewindow
from Final_Score import  Ui_Dialog as FinalScore

import sqlite3
fantasycricket = sqlite3.connect('Fantasy_cricket.db')
curs = fantasycricket.cursor()

class Ui_MainWindow(object):
    def __init__(self):
                                 
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = DialogN()
        self.new_screen.setupUi(self.evalDialog)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = DialogS()
        self.open_screen.setupUi(self.openDialog)

        self.EvatulateDialog=QtWidgets.QMainWindow()
        self.evaluate_screen = Evaluatewindow()
        self.evaluate_screen.setupUi(self.EvatulateDialog)

    def show_popup_close(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("Waring")
        msg.setIcon(QMessageBox.Question)
        msg.setInformativeText("Are You Sure,You Want To Close It")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        replay=msg.exec_()
        if(replay==QMessageBox.Yes):
            exit(0)
        else:
            pass

    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label0.setFont(font)
        self.label0.setObjectName("label0")
        self.horizontalLayout_3.addWidget(self.label0)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
                                 
        #for batsman
                                 
        self.labelbat = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelbat.setFont(font)
        self.labelbat.setObjectName("labelbat")
        self.horizontalLayout.addWidget(self.labelbat)
        self.batle = QtWidgets.QLineEdit(self.centralwidget)
        self.batle.setObjectName("batle")
        self.horizontalLayout.addWidget(self.batle)
                                 
        #for bowler
                                 
        self.labelbow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelbow.setFont(font)
        self.labelbow.setObjectName("labelbow")
        self.horizontalLayout.addWidget(self.labelbow)
        self.bowle = QtWidgets.QLineEdit(self.centralwidget)
        self.bowle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bowle.setInputMask("")
        self.bowle.setReadOnly(False)
        self.bowle.setObjectName("bowle")
        self.horizontalLayout.addWidget(self.bowle)
                                 
        #for allrunder
                                 
        self.labelar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelar.setFont(font)
        self.labelar.setObjectName("labelar")
        self.horizontalLayout.addWidget(self.labelar)
        self.arle = QtWidgets.QLineEdit(self.centralwidget)
        self.arle.setObjectName("arle")
        self.horizontalLayout.addWidget(self.arle)
        self.labelwk = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelwk.setFont(font)
        self.labelwk.setObjectName("labelwk")
        self.horizontalLayout.addWidget(self.labelwk)
        self.wkle = QtWidgets.QLineEdit(self.centralwidget)
        self.wkle.setObjectName("wkle")
        self.horizontalLayout.addWidget(self.wkle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                                 
        #Points Available
                                 
        self.labelptav = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelptav.setFont(font)
        self.labelptav.setObjectName("labelptav")
        self.horizontalLayout_4.addWidget(self.labelptav)
        self.ptavle = QtWidgets.QLineEdit(self.centralwidget)
        self.ptavle.setObjectName("ptavle")
        self.horizontalLayout_4.addWidget(self.ptavle)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
                                 
        #Points Used
                                 
        self.labelptu = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelptu.setFont(font)
        self.labelptu.setObjectName("labelptu")
        self.horizontalLayout_4.addWidget(self.labelptu)
        self.ptule = QtWidgets.QLineEdit(self.centralwidget)
        self.ptule.setObjectName("ptule")
        self.horizontalLayout_4.addWidget(self.ptule)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.batrb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.batrb.setFont(font)
                                 
        #batsman Radiobutton                       
        self.batrb.setObjectName("batrb")
        self.horizontalLayout_5.addWidget(self.batrb)
                                 
        #bowler Radiobutton
        self.bowrb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bowrb.setFont(font)
        self.bowrb.setObjectName("bowrb")
        self.horizontalLayout_5.addWidget(self.bowrb)
                                 
        #allrounder Radiobuttton
        self.arrb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.arrb.setFont(font)
        self.arrb.setObjectName("arrb")
        self.horizontalLayout_5.addWidget(self.arrb)

        #weeketkeeper Radiobutton
        self.wkrb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.wkrb.setFont(font)
        self.wkrb.setObjectName("wkrb")
        self.horizontalLayout_5.addWidget(self.wkrb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)

        #team name
        self.labeltn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labeltn.setFont(font)
        self.labeltn.setObjectName("labeltn")
        self.horizontalLayout_5.addWidget(self.labeltn)
        self.tnle = QtWidgets.QLineEdit(self.centralwidget)
        self.tnle.setObjectName("tnle")
        self.horizontalLayout_5.addWidget(self.tnle)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                                 
        self.labelavp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelavp.setFont(font)
        self.labelavp.setObjectName("labelavp")
        self.horizontalLayout_8.addWidget(self.labelavp)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
                                 
        self.labelsp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelsp.setFont(font)
        self.labelsp.setObjectName("labelsp")
        self.horizontalLayout_8.addWidget(self.labelsp)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        #list of players to select
        self.listmain1 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.listmain1.setFont(font)
        self.listmain1.setObjectName("listmain1")
        self.horizontalLayout_6.addWidget(self.listmain1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)

        #list of selected players
        self.listmain2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.listmain2.setFont(font)
        self.listmain2.setObjectName("listmain2")
        self.horizontalLayout_6.addWidget(self.listmain2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        #Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ##New Team
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionNEW_Team.triggered.connect(self.NewFile)
        self.new_screen.btnCreate.clicked.connect(self.ChangeTeamName)
                                 
        ##Open Team
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionOPEN_Team.triggered.connect(self.SelectTeam)
        self.open_screen.open.clicked.connect(self.AfterOpenTeam) #click to open

        ##Save team
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.triggered.connect(self.Team_Save)
        

        ##Evaluate
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        elf.actionEVALUATE_Team.triggered.connect(self.evaluate_Score)
        self.evaluate_screen.cbteam.currentTextChanged.connect(self.EvaluateScore)
        self.evaluate_screen.Evaluatescore.clicked.connect(self.Schow_score)
                                 
        self.score_screen.btnok.clicked.connect(self.CloseScore)

        ##Exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.actionEXIT.triggered.connect(self.show_popup_close)

        #Help
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        #Radiobutton function
        self.batle.clicked.connect(self.Add_Team_Data)
        self.bowle.clicked.connect(self.Add_Team_Data)
        self.arle.clicked.connect(self.Add_Team_Data)
        self.wkle.clicked.connect(self.Add_Team_Data)
        #listing
        self.items = []

    #for items to swap between list - double click
        self.listmain1.itemDoubleClicked.connect(self.removefromlist1)
        self.listmain2.itemDoubleClicked.connect(self.removefromlist2)

        

                      ##########                                        
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addAction(self.actionExit)
        self.menuManage_Teams.addAction(self.actionHelp)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                        ##########
        self.batscount = 0
        self.weektcount = 0
        self.allroundscount = 0
        self.ballscount = 0
        self.totalscount = 0
        self.availablepoints=1000
        self.usedpoints=0
                                 
    def NewFile(self):
        self.evalDialog.show()
                                 
    def ChangeTeamName(self):
         #type name                        
        self.TeamName=self.new_screen.newle.text()
         #set name
        self.teamname.setText(self.TeamName)
        self.evalDialog.close()

                                 
    def Add_Team_Data(self):
        checked=[self.batle.isChecked(),self.bowle.isChecked(),self.arle.isChecked(),self.wkle.isChecked()]
        sel=["BAT","BOW","AR","WK"]
        values=[sel[idx] for idx,c in enumerate(checked) if c==True]
        sql = "select player ||'-'|| ctg from players where ctg='{}'".format(values[0])
        self.check2 = []
        for i in range(self.listmain2.count()):
            items = self.listmain2.item(i).text()
            self.check2.append(items)

        #get Data
        m11=DataManager()
        data=m11.FetchItems(sql)
        players=[m[0] for m in data]
        self.listWidget.clear()
        if(len(players)!=0):
            for i in range(len(players)):
                item = QtWidgets.QListWidgetItem(players[i])
                item.setBackground(QtGui.QColor('light gray'))
                                 
                if(players[i] in self.check2):
                    item.setForeground(QtGui.QColor('red'))
                self.listWidget.addItem(item)
                                 
    def GetPlayerpoints(self,name):
        sql="select value from stats where name='{}'".format(name)
        m11=DataManager()
        data=m11.FetchItems(sql)
        return data[0][0]

    def PointsSet(self,selectedit):
        points = self.GetPlayerpoints(selectedit)
        self.availablepoints -= points
        self.pointsavailable.setText(str(self.availablepoints))
        pointsused = 1000 - self.avipoints
        self.pointused.setText(str(pointsused))
                                 

    def removefromlist1(self,item):
        self.check2=[]
        for i in range(self.listmain2.count()):
            items=self.listmain2.item(i).text()
            self.check2.append(items)
        selectedit=str(self.listmain1.currentItem().text()).split("-")[0]
        if(self.listmain1.currentItem().text() not in self.check2):

            if self.availablepoints >= 0:
                # IF BAT is Clicked
                if self.batle.isChecked() == True:
                    if self.batscount >= 0 and self.batscount < 5:
                        self.PointsSet(selectedit)
                        self.listmain1.takeItem(self.listmain1.row(item))
                        self.listmain2.addItem(item)
                        self.batscount += 1
                        self.totalscount = self.listmain1.count()
                        self.batsmancount.setText(str(self.batscount))
                    else:
                        msg = "Only 5 batsman are allowed"
                        self.ShowError(msg)

                # for wicktekeeper
                elif self.WK.isChecked() == True:
                    if self.weektcount >= 0 and self.weektcount < 1:
                        self.PointsSet(selectedit)
                        self.listmain1.takeItem(self.listmain1.row(item))
                        self.listmain2.addItem(item)
                        self.weektcount += 1
                        self.totalscount = self.listmain1.count()
                        self.wicketkeepercount.setText(str(self.weektcount))
                    else:
                        msg = "Only 1 keeper are allowed"
                        self.ShowError(msg)
                # for allrounder
                elif self.AR.isChecked() == True:
                    if self.allroundscount >= 0 and self.allroundscount < 2:
                        self.PointsSet(selectedit)
                        self.listmain1.takeItem(self.listmain1.row(item))
                        self.listmain2.addItem(item)
                        self.allroundscount += 1
                        self.allroundercount.setText(str(self.allroundscount))
                    else:
                        msg = "Only 2 Allrounder Count"
                        self.ShowError(msg)
                ##for bowler
                else:
                    if self.ballscount >= 0 and self.ballscount < 3:
                        self.PointsSet(selectedit)
                        self.listmain1.takeItem(self.listmain1.row(item))
                        self.listmain2.addItem(item)
                        self.ballscount += 1
                        self.bowlercount.setText(str(self.ballscount))
                    else:
                        msg = "Only 3 bowlers are allowed"
                        self.ShowError(msg)
            else:
                message="Remaing Points are Less to select this player"
                self.ShowError(message)

        else:
            self.ShowError("already Selected")



    def removefromfinal(self,item):
        self.check = []
        for i in range(self.listmain1.count()):
            items = self.listmain1.item(i).text()
            self.check.append(items)
        checked = [self.BAT.isChecked(), self.BOW.isChecked(), self.AR.isChecked(), self.WK.isChecked()]
        sel = ["BAT", "BOW", "AR", "WK"]
        values = [sel[idx] for idx, c in enumerate(checked) if c == True]
        citem=values[0]
        selectitems=self.listmain2.currentItem().text().split("-")[1]
        selectid=self.listWidget_2.currentItem().text().split("-")[0]
        cs=self.listWidget_2.currentItem().text()#current selected Item

        points = self.GetPlayerpoints(selectid)
        self.availablepoints += points
        self.pointsavialable.setText(str(self.availablepoints))
        pointsused = 1000 - self.availablepoints
        self.pointused.setText(str(pointsused))


        if selectitems=="BAT":
            self.listmain2.takeItem(self.listmain2.row(item))
            if(citem=="BAT") and cs not in self.check :
                self.listWidget.addItem(item)
            self.batscount -= 1
            self.batsmancount.setText(str(self.batscount))




            # for wicketkeeper
        elif  selectitems=="WK":
            self.listmain2.takeItem(self.listmain2.row(item))
            if (citem == "WK") and  cs not in self.check:
                self.listmain2.addItem(item)
            self.weektcount -= 1
            self.wicketkeepercount.setText(str(self.weektcount))

        # for allrounder
        elif  selectitems=="AR":
            self.listmain2.takeItem(self.listmain2.row(item))
            if (citem == "AR") and cs not in self.check:
                self.listmain.addItem(item)
            self.allroundscount -= 1
            self.allroundercount.setText(str(self.allroundscount))

        ##for bowler
        else:
            self.listmain1.takeItem(self.listmain2.row(item))
            if (citem == "BOW") and cs not in self.check:
                self.listmain1.addItem(item)
            self.ballscount -= 1
            self.bowlercount.setText(str(self.ballscount))
                                 
    def ShowSuccess(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success")
        msg.setInformativeText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def ShowError(self,e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(e)
        msg.setWindowTitle("Error")
        msg.exec_()

    def Open_Team(self):
        self.openDialog.show()


    def AfterOpenTeam(self):
        self.selected =self.open_screen.combo_Pl_ev.currentText()
        if str(self.selected)!="Select":
            m11=DataManager()
            sql = "select * from teams where name='{}'".format(self.selected)
            data = m11.FetchItems(sql)
            TeamName=data[0][0]
            players=data[0][1].split(",")
            self.listmain1.clear()
            self.teamname.setText(TeamName)
            for i in range(len(players)) :
                item = QtWidgets.QListWidgetItem(players[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(100)
                item.setFont(font)
                item.setBackground(QtGui.QColor('light gray'))
                self.listmain2.addItem(item)
            self.openDialog.close()
        else:
            e="Please Select At least one Team"
            self.ShowError(e)

    def Team_Save(self):
        self.items.clear()
        for index in range(self.listmain2.count()):
            self.items.append(self.listmain2.item(index).text().split("-")[0])
        m11=DataManager()
        scoresdata = []
        for player in self.items:
            squery="select value from stats where name='{}';".format(player)
            data=str(m11.FetchItems(query)[0][0])
            scoresdata.append(data)
        #List = tuple(zip(self.items, score))
        name=self.teamname.text()
        players=",".join(self.items)
        scores=",".join(scoresdata)
        if(len(self.items)==11):
            checkteams="select name from teams where name='{}'".format(name)
            checkvalue=m11.FetchItems(checkteams)
            if (len(checkvalue)>0):
                e = "This Team Name is Already Exists"
                self.ShowError(e)
            elif(name=="#####"):
                e = "Blank Team Name Not Allowed"
                self.ShowError(e)

            else:
                sqladdteam = "Insert into teams (name,players,value) values(?,?,?)"
                inserteddata = d1.InsertItems(sqladdteam, (name, players, scores))
                if(inserteddata=="1"):
                    message="Successfully Saved"
                    self.ShowSuccess(message)
                else:
                    e = "Something Went Wrong Try Again"
                    self.ShowError(e)



        else:
            e = "Please Select At least 11 Players"
            self.ShowError(e)

    def Evaluate_Score(self):
        m11 = DataManager()
        t = "select name,value from teams"
        teams = m11.FetchItems(t)
        allteams = [t[0] for t in teams]
        self.evaluate_screen.combo_Pl_ev.addItem("Select Team")
        for i in range(len(allteams)):
            self.evaluate_screen.combo_Pl_ev.addItem(allteams[i])
        self.EvatulateDialog.show()
    def EvaluateScore(self):
        self.evaluate_screen.combo_P_ev.currentTextChanged.connect(self.FinalScore)
    def PlayerScoreCalulate(self,coloumns,d1,name):
        sql="select * from match where player='{}'".format(name)
        data=m11.FetchItems(sql)
        player_score=[]
        scored=data[0][1]
        try:
            strikerate=(scored/data[0][2])*100
        except:
            strikerate=0
        #Batsman Scored
        #1point for each 2 run
        try:
            player_score.append(scored/2)
        except:
            pass

        #if scored>50 then 5 points
        if(scored>=50):
            player_score.append(int(scored/50)*5)


        #if Strikerate is greator than 100 then extra 4 points
        if (scored >= 100):
            player_score.append(int(scored/100)*10)

        #if strikerate is 80-100 the extra 4 points
        if 80<=strikerate<=100:
            player_score.append(2)

        #per 4 1 point
        if data[0][3]>0:
            player_score.append(1*data[0][3])


        #per 6 2 points
        if data[0][4]>0:
            player_score.append(2*data[0][4])


        #FOR Bowling
        #per wicket 10 points
        wkt=data[0][8]
        if wkt>0:
            player_score.append(10 * wkt)

        #if wickets are greator than 3 the 5 points
        if 3<=wkt<=5:
            player_score.append(5)

        #if wicket is greator or equql to 5 then extra 10 points
        if wkt>5:
            player_score.append(10)



        #ECONOMY RRATE
        overs=data[0][5]/6
        givenruns=data[0][7]
        try:
            economyrate = givenruns / overs
        except:
            economyrate=0

        #if economy rate between 3.5 to 4.5 then 4 points
        if 3.5<=economyrate<=4.5:
            player_score.append(4)


        #economy rate between 2 to 3.5 then 7 points
        if 2<=economyrate<=3.5:
            player_score.append(7)

        #economy rate less than 2 them 10 points
        if economyrate<2:
            player_score.append(10)

        #10  points  each for catch / stumping / run out
        catch=data[0][9]*10
        stump=data[0][10]*10
        runout=data[0][11]*10

        player_score.extend([catch,stump,runout])

        #print(sum(player_score),player_score)

        #All Points Generated using rules
        return  sum(player_score)
    def FinalScore(self):
        scores=[]
        m11 = DataManager()
        #Get All Required Coloumns
        sql = "select * from match;"
        coloumnslist = m11.Fetchcoloumns(sql)
        team=self.evaluate_screen.combo_Pl_ev.currentText()
        psql ="select players from teams where name='{}'".format(team)
        pls=list(m11.FetchItems(psql)[0])
        playerlist=pls[0].split(",")
        self.evaluate_screen.listevaluate1.clear()
        self.evaluate_screen.listevaluate2.clear()
        for index in range(len(playerlist)):
            playerscore=self.PlayerScoreCalulate(coloumnslist,d1,playerlist[index])
            item = QtWidgets.QListWidgetItem(playerlist[index])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.evaluate_screen.listevaluate2.addItem(item)
            self.evaluate_screen.listevaluate1.addItem(str(playerscore))

    def Schow_score(self):

        pointcount=self.evaluate_screen.listevaluate1.count()
        self.scorepoints=[((self.evaluate_screen.listevaluate1.item(i).text())) for i in range(pointcount)]
        self.adds=0
        for sp in self.scorepoints:
            self.adds+=float(sp)

        if(self.evaluate_screen.combo_Pl_ev.currentText()!="Select Team" and self.evaluate_screen.combo_Pl_ev.currentText()!="Select Match"):
            self.ScoreDialog.show()
            m11 = DataManager()
            squery = "Update teams set value=? where name=?"
            data = m11.InsertItems(squry, (self.adds, self.evaluate_screen.combo_Pl_ev.currentText()))
            self.score_screen.label_2.setText('{}'.format(self.adds))
        else:
            message="Please Select team And Match"
            self.ShowError(message)
    
                                 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label0.setText(_translate("MainWindow", "Your Selections"))
        self.labelbat.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.labelbow.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.labelar.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.labelwk.setText(_translate("MainWindow", "Wicket-Keepers (WK)"))
        self.labelptav.setText(_translate("MainWindow", "Points Available"))
        self.labelptu.setText(_translate("MainWindow", "Points Used"))
        self.batrb.setText(_translate("MainWindow", "BAT"))
        self.bowrb.setText(_translate("MainWindow", "BOW"))
        self.arrb.setText(_translate("MainWindow", "AR"))
        self.wkrb.setText(_translate("MainWindow", "WK"))
        self.labeltn.setText(_translate("MainWindow", "Team Name"))
        self.labelavp.setText(_translate("MainWindow", "          Available Players"))
        self.labelsp.setText(_translate("MainWindow", "Selected players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Tab"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
