import mysql.connector

from appJar import gui

db = mysql.connector.connect(host='localhost', database='mysql', user='root', password='mysql123')
cursor = db.cursor()
cursor.execute("use reg12")
app = gui()
kol = 1
ranked = ''
sql = ''
points = 0
gid = 0
l = 0
w = 0


def swaroski():
    # print('swa')
    app = gui()

    def loc(win):
        app.showSubWindow(win)
        app.setBg("orange")

    # start initial, vertical pane
    app.startPanedFrameVertical("p1")
    app.setGeometry("400x310")
    app.setBg("orange")
    app.addButton("Add player", loc)

    # start additional panes inside initial pane
    app.startPanedFrame("p2")
    app.setBg("orange")
    app.addButton("Add match info", loc)
    app.stopPanedFrame()

    app.startPanedFrame("p3")
    app.setBg("orange")
    app.addButton("Show player info", loc)
    app.stopPanedFrame()

    app.startPanedFrame("p4")
    app.setBg("orange")
    app.addButton("Show all players", loc)
    app.stopPanedFrame()

    app.startPanedFrame("p5")
    app.setBg("orange")
    app.addButton("delete player", loc)
    app.stopPanedFrame()

    # stop initial pane
    app.stopPanedFrame()

    # this is a pop-up
    app.startSubWindow("Add player", modal=True)

    def terarank(points):
        global ranked
        if points < 1500:
            ranked = 'Copper4'
        elif 1499 < points < 1600:
            ranked = 'Copper3'
        elif 1599 < points < 1700:
            ranked = 'Copper2'
        elif 1699 < points < 1800:
            ranked = 'Copper1'
        elif 1799 < points < 1900:
            ranked = 'Bronz4'
        elif 1899 < points < 2000:
            ranked = 'Bronz3'
        elif 1999 < points < 2100:
            ranked = 'Bronz2'
        elif 2099 < points < 2200:
            ranked = 'Bronz1'
        elif 2199 < points < 2300:
            ranked = 'Silver4'
        elif 2299 < points < 2400:
            ranked = 'Silver3'
        elif 2399 < points < 2500:
            ranked = 'Silver2'
        elif 2499 < points < 2600:
            ranked = 'Silver1'
        elif 2599 < points < 2800:
            ranked = 'Gold4'
        elif 2799 < points < 3000:
            ranked = 'Gold3'
        elif 2999 < points < 3200:
            ranked = 'Gold2'
        elif 3199 < points < 3400:
            ranked = 'Gold1'
        elif 3399 < points < 3800:
            ranked = 'Platinum3'
        elif 3799 < points < 4200:
            ranked = 'Platinum2'
        elif 4199 < points < 4600:
            ranked = 'Platinum1'
        elif points > 4599:
            ranked = 'Diamond'

        return ranked

    def pressed(button):
        if button == "Cancel":
            app.stop()
            swaroski()
        else:
            playername = app.getEntry("playername")
            gamingname = app.getEntry("gamingname")
            age = app.getEntry("age")
            wins = app.getEntry("wins")
            loss = app.getEntry("loss")
            level = app.getEntry("level")
            points = 2500 + (int(wins) * 50) - (int(loss) * 50)
            ranked = terarank(points)
            count = 0
            cursor.execute("use reg12")

            try:

                playername = str(playername)
                gamingname = str(gamingname)
                age = int(age)
                wins = int(wins)
                loss = int(loss)
                level = int(level)
                ranked = str(ranked)
                points = int(points)
                # for kll in range(rankedInfo):
                # sql1 = "INSERT INTO playerifo(playername,gamingname,age,wins,loss,level,rankedinfo) VALUES('%s','%s','%d','%d','%d','%d','%s')" %(playername, gamingname, age, wins, loss, level, rankedinfo)

                # Execute the SQL command
                cursor.execute(
                    "INSERT INTO playerinfo(playername,gamingname,age,wins,loss,level,ranked,points) VALUES('%s','%s','%d','%d','%d','%d','%s','%d')" % (
                        playername, gamingname, age, wins, loss, level, ranked, points))
                #    Commit your changes in the database
                db.commit()


            except:
                count = count + 1

            if (count == 0):
                app.infoBox("new window", "entry successful", parent="Add player")

            else:
                app.infoBox("new window", "entry usuccessful", parent="Add player")

        app.stop()
        swaroski()

    app.addLabelEntry("playername")
    app.addLabelEntry("gamingname")
    app.addLabelEntry("age")
    app.addLabelEntry("wins")
    app.addLabelEntry("loss")
    app.addLabelEntry("level")
    # app.addLabelEntry("ranked")

    app.addButtons(["Add", "Cancel"], pressed)
    app.stopSubWindow()

    # this is arankedInfother pop-up
    app.startSubWindow('Show player info')
    lol = ''
    x = 1

    def pr(win):

        def close(button):
            app.stop()
            swaroski()

        app.startSubWindow("show data")
        k = app.getOptionBox("Options")

        l = app.getEntry("search")

        if k == 'GID':
            lol = "Select * from playerinfo where (%s ='%d') " % \
                  (k, int(l))

        else:
            lol = "Select * from playerinfo where (%s = '%s') " % \
                  (k, l)

        app.setBg("orange")

        app.setSticky("news")
        app.setExpand("both")
        app.setFont(20)
        app.addButton("DONE", close, 2, 3)
        app.addLabel("lpp1", "GID", 0, 0)
        app.addLabel("lppp2", "playername", 0, 1)
        app.addLabel("lpp3", "gamingname", 0, 2)
        app.addLabel("lpp4", "age", 0, 3)
        app.addLabel("lpp5", "wins", 0, 4)
        app.addLabel("lpp6", "loss", 0, 5)
        app.addLabel("lpp7", "level", 0, 6)
        app.addLabel("lpp8", "ranked", 0, 7)
        app.addLabel("lpp9", "points", 0, 8)

        km = 1

        cursor.execute("use reg12")
        # print('c1')
        # Execute the SQL command
        cursor.execute(lol)
        # print('c2')
        # Fetch all the rows in a list of lists.
        rows = cursor.fetchall()
        # print('c3')
        for row in rows:
            # print('c4')
            gid = row[0]
            playername = row[1]
            gamingname = row[2]
            age = row[3]
            wins = row[4]
            loss = row[5]
            level = row[6]
            ranked = row[7]
            points = row[8]
            # Now print fetched result
            app.setExpand("both")
            app.setFont(20)
            app.addLabel("a1%s" % str(km), "%d" % gid, km, 0)
            app.addLabel("m2%s" % str(km), "%s" % playername, km, 1)
            app.addLabel("n3%s" % str(km), "%s" % gamingname, km, 2)
            app.addLabel("o4%s" % str(km), "%d" % age, km, 3)
            app.addLabel("p5%s" % str(km), "%d" % wins, km, 4)
            app.addLabel("q6%s" % str(km), "%d" % loss, km, 5)
            app.addLabel("r7%s" % str(km), "%d" % level, km, 6)
            app.addLabel("r8%s" % str(km), "%s" % ranked, km, 7)
            app.addLabel("s8%s" % str(km), "%d" % points, km, 8)

            km = km + 1

        app.stopSubWindow()
        app.showSubWindow(win)

    app.setFont(20)
    app.addLabelOptionBox("Options", ['GID', 'playername', 'gamingname'])
    app.addLabelEntry("search")

    app.addButton("show data", pr)

    app.stopSubWindow()

    # this is arankedInfother popup

    app.startSubWindow("Add match info")
    app.addLabel("l3", "SubWindow Three")

    def pre(button):
        global sql, points, gid, w, l
        cursor.execute("use reg12")
        # print('pre')
        if button == "done":
            app.stop()
            swaroski()
        else:
            # print('c1')
            flag = 1
            k = app.getOptionBox("Match Type")
            gamingname = app.getEntry("gaming name")
            kills = app.getEntry("kills")
            deaths = app.getEntry("deaths")
            result = app.getEntry("Win or Loss")
            cursor.execute("select * from playerinfo")
            row = cursor.fetchone()
            while row is not None:
                # print(row)
                if row[2] == gamingname:
                    points = row[8]
                    gid = row[0]
                    w = row[4]
                    l = row[5]
                    flag = 0

                row = cursor.fetchone()

            if (flag == 1):
                app.infoBox("new window", 'No player found', parent=None)
                pre('ok')


                # print(points)
            if k == 'Ranked':
                # print('R')
                if result == 'win':
                    # print('win')
                    points = points + 50 + (int(kills) * 10) - (int(deaths) * 10)
                    rank = terarank(points)
                    cursor.execute(
                        "update playerinfo set ranked = '%s' where gamingname = '%s' " % (rank, gamingname))
                    cursor.execute(
                        "update playerinfo set points = '%d' where gamingname = '%s' " % (int(points), gamingname))
                    w = w + 1
                    cursor.execute(
                        "update playerinfo set wins = '%d' where gamingname = '%s' " % (int(w), gamingname))
                    db.commit()
                elif result == 'loss':
                    # print('loss')
                    points = points + (int(kills) * 10) - (int(deaths) * 10) - 50
                    rank = terarank(points)
                    cursor.execute(
                        "update playerinfo set ranked = '%s' where gamingname = '%s' " % (rank, gamingname))
                    cursor.execute(
                        "update playerinfo set points = '%d' where gamingname = '%s' " % (int(points), gamingname))
                    l = l + 1
                    cursor.execute(
                        "update playerinfo set loss = '%d' where gamingname = '%s' " % (int(l), gamingname))
                    db.commit()

                sql = "INSERT INTO rankedinfo1(GID,kills,deaths,result,points)\
                        VALUES('%d','%d','%d','%s','%d')" % (int(gid), int(kills), int(deaths), result, int(points))

            elif k == 'Casual':
                # print('C')
                if result == 'win':
                    # print('win')
                    points = points + 25 + (int(kills) * 10) - (int(deaths) * 10)
                    rank = terarank(points)
                    cursor.execute(
                        "update playerinfo set ranked = '%s' where gamingname = '%s' " % (rank, gamingname))
                    cursor.execute(
                        "update playerinfo set points = '%d' where gamingname = '%s' " % (int(points), gamingname))
                    w = w + 1
                    cursor.execute(
                        "update playerinfo set wins = '%d' where gamingname = '%s' " % (int(w), gamingname))
                    db.commit()
                elif result == 'loss':
                    # print('loss')
                    points = points + (int(kills) * 10) - (int(deaths) * 10) - 25
                    rank = terarank(points)
                    cursor.execute(
                        "update playerinfo set ranked = '%s' where gamingname = '%s' " % (rank, gamingname))
                    cursor.execute(
                        "update playerinfo set points = '%d' where gamingname = '%s' " % (int(points), gamingname))
                    l = l + 1
                    cursor.execute(
                        "update playerinfo set loss = '%d' where gamingname = '%s' " % (int(l), gamingname))
                    db.commit()
                sql = "INSERT INTO casualinfo1(GID,kills,deaths,result,points)\
                        VALUES('%d','%d','%d','%s','%d')" % (int(gid), int(kills), int(deaths), result, int(points))

                # print('c2')

            # Execute the SQL command
            cursor.execute(sql)
            # print('c3')

            #    Commit your changes in the database
            db.commit()
            # print('c4')
            app.infoBox("new window", "entry successful", parent="Add player")

    app.addLabelOptionBox("Match Type", ['Ranked', 'Casual'])
    app.addLabelEntry("gaming name")
    app.addLabelEntry("kills")
    app.addLabelEntry("deaths")
    app.addLabelEntry("Win or Loss")
    app.addButtons(["OK", "done"], pre)

    app.stopSubWindow()

    app.startSubWindow("Show all players")
    app.setBg("orange")

    def closes(button):
        app.stop()
        swaroski()

    km = 1
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(20)

    app.addLabel("lp1", "GID", 0, 0)
    app.addLabel("lp2", "playername", 0, 1)
    app.addLabel("lp3", "gamingname", 0, 2)
    app.addLabel("lp4", "age", 0, 3)
    app.addLabel("lp5", "wins", 0, 4)
    app.addLabel("lp6", "loss", 0, 5)
    app.addLabel("lp7", "level", 0, 6)
    app.addLabel("lp8", "ranked", 0, 7)
    app.addLabel("lp9", "points", 0, 8)

    cursor.execute("select * from playerinfo")
    rows = cursor.fetchall()

    for row in rows:
        gid = row[0]
        playername = row[1]
        gamingname = row[2]
        age = row[3]
        wins = row[4]
        loss = row[5]
        level = row[6]
        ranked = row[7]
        points = row[8]
        # Now print fetched result
        app.setExpand("both")
        app.setFont(20)
        app.addLabel("1l1%s" % str(km), "%d" % gid, km, 0)
        app.addLabel("2m2%s" % str(km), "%s" % playername, km, 1)
        app.addLabel("3n3%s" % str(km), "%s" % gamingname, km, 2)
        app.addLabel("4o4%s" % str(km), "%d" % age, km, 3)
        app.addLabel("5p5%s" % str(km), "%d" % wins, km, 4)
        app.addLabel("6q6%s" % str(km), "%d" % loss, km, 5)
        app.addLabel("7r7%s" % str(km), "%d" % level, km, 6)
        app.addLabel("8r8%s" % str(km), "%s" % ranked, km, 7)
        app.addLabel("9s8%s" % str(km), "%d" % points, km, 8)

        km = km + 1
    app.addButton("ok", closes, km, 3)

    app.stopSubWindow()

    app.startSubWindow("delete player")

    def dele(button):
        if button == 'Ok':
            app.stop()
            swaroski()

        k = app.getOptionBox("Option's")
        print(k)

        l = app.getEntry("Entry")

        print(l)
        if k == 'GID':
            lo = " delete from playerinfo where %s = '%d' " % (k, int(l))
            l1 = " delete from rankedinfo1 where %s = '%d' " % (k, int(l))
            l2 = " delete from casualinfo1 where %s = '%d' " % (k, int(l))
        else:
            lo = "delete from playerinfo where %s = '%s' " % (k, str(l))
            l1 = "delete from rankedinfo1 where %s = '%s' " % (k, str(l))
            l2 = "delete from casualinfo1 where %s = '%s' " % (k, str(l))

        cursor.execute(l1)
        db.commit()
        cursor.execute(l2)
        db.commit()
        cursor.execute(lo)
        db.commit()

    app.setFont(20)
    app.addLabelOptionBox("Option's", ['GID', 'playername', 'gamingname'])
    app.addLabelEntry("Entry")

    app.addButtons(["delete", "Ok"], dele)

    app.stopSubWindow()

    app.go()


app.startLabelFrame("Login Details")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.setBg("red")
app.setFont(18)


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if (usr == "atom" and pwd == "abhi123"):

            app.infoBox("new window", "congrats connection successful", parent=None)
            app.stop()
            swaroski()
        else:
            app.infoBox("new window", "unsuccessful try again", parent=None)


app.addButtons(["Submit", "Cancel"], press)
app.stopLabelFrame()

app.go()
