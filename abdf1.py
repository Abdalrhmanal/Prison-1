
#from multiprocessing.spawn import is_forking
#from select import select
import sqlite3
abd = sqlite3.connect("Prosen1.db")
conn = abd.cursor()
print("True : : :  : :")
abd.execute("""CREATE TABLE if not exists Offense (
	Id	INTEGER NOT NULL UNIQUE,
	Name	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT)
)
""")
abd.execute("""CREATE TABLE if not exists Convicts(
	Id	INTEGER NOT NULL UNIQUE,
	formData	TEXT NOT NULL,
	toData	TEXT NOT NULL,
	PersonId	INTEGER NOT NULL,
	OffenseId	INTEGER NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT),
	FOREIGN KEY(OffenseId) REFERENCES Offense(Id),
	FOREIGN KEY(PersonId) REFERENCES Person(Id)
)
""")
abd.execute("""CREATE TABLE if not exists Person (
	Id	INTEGER NOT NULL UNIQUE,
	fristName	TEXT NOT NULL,
	father	TEXT NOT NULL,
	lastName	TEXT NOT NULL,
	Gender	TEXT NOT NULL,
	BirthYeer	TEXT NOT NULL,
	Address	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT)
)
""")
abd.execute("""CREATE TABLE if not exists Visitings (
	Id	INTEGER NOT NULL UNIQUE,
	DateVisited	TEXT NOT NULL,
	PersonId	INTEGER NOT NULL,
	VisitOrName	TEXT NOT NULL,
	MontinMinutes	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT),
	FOREIGN KEY(PersonId) REFERENCES Person(Id)
)
""")
abd.execute("""CREATE TABLE if not exists DungeonMoves (
	Id	INTEGER NOT NULL UNIQUE,
	DungeonId	INTEGER NOT NULL,
	PersonId	INTEGER NOT NULL,
	fromDate	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT),
	FOREIGN KEY(PersonId) REFERENCES Person(Id),
	FOREIGN KEY(DungeonId) REFERENCES Dungeon(Id)
)
""")
abd.execute("""CREATE TABLE if not exists Dungeon (
	Id	INTEGER NOT NULL UNIQUE,
	Name	TEXT NOT NULL,
	Size	TEXT NOT NULL,
	PRIMARY KEY(Id AUTOINCREMENT)
)
""")

# Offense إنشاء صف


class Offense:
    def __init__(self, Id, Name):

        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id > 0")

        if len(Name) > 1:
            self.__Name = Name
        else:
            raise Exception("Length name >1")

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0")

    def getId(self):
        return self.__Id

    def getName(self):
        return self.__Name

    def setName(self, Name):
        if len(Name) > 1:
            self.__Id = Name
        else:
            raise Exception("Id < 0")

# Convicts أنشاء صف


class Convicts:

    def __init__(self, Id, fromDate, toDate, PersonId, OffenseId):

        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0")

        if len(fromDate) > 1:
            self.__fromDate = fromDate
        else:
            raise Exception("Length fromDate < 1")
        if len(toDate) > 1:
            self.__toDate = toDate
        else:
            raise Exception("Length toDate < 1")
        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("PersonId < 0")
        if OffenseId > 0:
            self.__OffenseId = OffenseId
        else:
            raise Exception("OffenseId < 0")
        '''
    def __init__(self):
         self.__Id=0
         self.__fromDate =""
         self.__toDate =  ""
         self.__PersonId = ""
         self.__OffenseId = ""
         '''

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0")

    def getId(self):
        return self.__Id

    def getfromDate(self):
        return self.__fromDate

    def setfromDate(self, fromDate):
        if len(fromDate) > 1:
            self.__fromDate = fromDate
        else:
            raise Exception("Length fromDate < 1")

    def gettoDate(self):
        return self.__toDate

    def settoDate(self, toDate):
        if len(toDate) > 1:
            self.__fromDate = toDate
        else:
            raise Exception("Length toDate < 1")

    def getPersonId(self):
        return self.__PersonId

    def setPersonId(self, PersonId):
        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("PersonId < 0")

    def getOffenseId(self):
        return self.__OffenseId

    def setOffenseId(self, OffenseId):
        if OffenseId > 0:
            self.__OffenseId = OffenseId
        else:
            raise Exception("PersonId < 0")


# Person إنشاء صف


class Person:
    def __init__(self, Id, FirstName, Father, LastName, Gender, BirthYear, Address):

        if Id > 0:
            self.__Id = Id
            self.__BirthYear = BirthYear
        else:
            raise Exception("Id < 0")

        if len(FirstName) > 1:
            self.__FirstName = FirstName
        else:
            raise Exception("Length FirstName  < 1")
        if len(Father) > 1:
            self.__Father = Father
        else:
            raise Exception("Length Father < 1")
        if len(LastName) > 1:
            self.__LastName = LastName
        else:
            raise Exception("Length  LastName  < 1")
        if Gender in ("male", "female", "null"):
            self.__Gender = Gender
        else:
            raise Exception("Gender in ('male', 'female','null')")

        self.__BirthYear = BirthYear

        if len(Address) > 2:
            self.__Address = Address
        else:
            raise Exception("Length Address > 2")

# **************لا تنسى Birth year تحتاج الى تعديل لا تنسى ********************

    def getId(self):
        return self.__Id

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0")

    def getfirstName(self):
        return self.__FirstName

    def setfirstName(self, FirstName):
        if len(FirstName) > 1:
            self.__FirstName = FirstName
        else:
            raise Exception("Length FirstName  < 1")

    def getFather(self):
        return self.__Father

    def setFather(self, Father):
        if len(Father) > 1:
            self.__Father = Father
        else:
            raise Exception("Length Father  < 1")

    def getlastName(self):
        return self.__LastName

    def setlastName(self, lastName):
        if len(lastName) > 1:
            self.__lastName = lastName
        else:
            raise Exception("Length lastName  < 1")

    def getGender(self):
        return self.__Gender

    def setGender(self, Gender):
        if Gender in ("male", "female", "null"):
            self.__Gender = Gender
        else:
            raise Exception("Gender in ('male', 'female','null')")

    def getBirthYear(self):
        return self.__BirthYear

    def setBirthYear(self, BirthYear):

        self.__BirthYear = BirthYear

    def getAddress(self):
        return self.__Address

    def setAddress(self, Address):
        if len(Address) > 1:
            self.__Address = Address
        else:
            raise Exception("Length Address  < 1")

# Dungeon أنشاء صف


class Dungeon:
    def __init__(self, Id, Name, Size):

        if Id > 0 and Size >= 2:
            self.__Id = Id
            self.__Size = Size
        else:
            raise Exception("Id < 0 ")

        if len(Name) > 1:
            self.__Name = Name
        else:
            raise Exception("Length Name  < 1 ")
        if Size >= 2:
            self.__Size = Size
        else:
            raise Exception("Size >= 2 ")

    def getId(self):
        return self.__Id

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0 ")

    def getName(self):
        return self.__Name

    def setName(self, Name):
        if len(Name) > 1:
            self.__Name = Name
        else:
            raise Exception("Length Name  < 1 ")

    def getSize(self):
        return self.__Size

    def setSize(self, Size):
        if Size >= 2:
            self.__Size = Size
        else:
            raise Exception("Size >= 2 ")


# Visitings أنشاء صف
class Visitings:
    def __init__(self, Id, DateVisited, PersonId, VisitorName, MontinMinutes):

        if Id > 0:
            self.__Id = Id

        else:
            raise Exception("Id < 0 ")

        if len(DateVisited) > 1:
            self.__DateVisited = DateVisited
        else:
            raise Exception("Length DateVisited < 1")

        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("Person Id < 0 ")
        if len(VisitorName) > 1:
            self.__VisitorName = VisitorName
        else:
            raise Exception("Length VisitorName  < 1")
        if MontinMinutes > 1:
            self.__MontinMinutes = MontinMinutes
        else:
            raise Exception("MountinMinutes < 1")

    def getId(self):
        return self.__Id

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0 ")

    def getDateVisited(self):
        return self.__DateVisited

    def setDateVisited(self, DateVisited):
        if len(DateVisited) > 1:
            self.__DateVisited = DateVisited
        else:
            raise Exception("Length DateVisited < 1")

    def getPersonId(self):
        return self.__PersonId

    def setPersonId(self, PersonId):
        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("PersonId < 0")

    def getVisitorName(self):
        return self.__VisitorName

    def setVisitorName(self, VisitorName):
        if len(VisitorName) > 1:
            self.__VisitorName = VisitorName
        else:
            raise Exception("Length VisitorName  < 1")

    def getMontinMinutes(self):
        return self.__MontinMinutes

    def setMontinMinutes(self, MontinMinutes):
        if MontinMinutes > 1:
            self.__MontinMinutes = MontinMinutes
        else:
            raise Exception("MountinMinutes < 1")


print("True : : :  : :")

# DungeonMoves أنشاء صف


class DungeonMoves:
    def __init__(self, Id, DungeonId, PersonId, FromDate):

        if Id > 0:
            self.__Id = Id

            self.__FromDate = FromDate
        else:
            raise Exception("Id < 0")

        if DungeonId > 0:
            self.__DungeonId = DungeonId
        else:
            raise Exception("DungeonId < 0 ")
        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("PersonId < 0")
        if len(FromDate) > 1:
            self.FromDate = FromDate
        else:
            raise Exception("Length FromDate  < 1")

    def getId(self):
        return self.__Id

    def setId(self, Id):
        if Id > 0:
            self.__Id = Id
        else:
            raise Exception("Id < 0 ")

    def getDungeonId(self):
        return self.__DungeonId

    def serDungeonId(self, DungeonId):
        if DungeonId > 0:
            self.__DungeonId = DungeonId
        else:
            raise Exception("DungeonId < 0 ")

    def getPersonId(self):
        return self.__PersonId

    def setPersonId(self, PersonId):
        if PersonId > 0:
            self.__PersonId = PersonId
        else:
            raise Exception("PersonId < 0")

    def getFromDate(self):
        return self.__FromDate

    def setFromDate(self, FromDate):
        if len(FromDate) > 1:
            self.FromDate = FromDate
        else:
            raise Exception("Length FromDate  < 1")


class date:
    def __init__(self, year, month, day):
        if int(year) > 1950:
            self.__year = year
        else:
            raise Exception("the year must be in range from 1950 to now")
        if int(month) in range(1, 13):
            self.__month = month
        else:
            raise Exception("the month must be in range from 1 to 12")
        if int(day) in range(1, 32):
            self.__day = day
        else:
            raise Exception("the day must be in range from 1 to 31")

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def getDay(self):
        return self.__day

    def allDate(self):
        return self.getYear()+str("/")+self.getMonth()+str("/")+self.getDay()


''''
def selectValueNamePerson():
    inputx=input("Name offense  :")
    abd.execute("""
    select FirstName,Father,LastName from Person where (select Name="inputx" from offense)
                 """)
selectValueNamePerson()

print("True  : :  ; : : :")
'''

try:
    # **********************add to Offense*****************************************************

    def insertValueOffense():
        ab = Offense(int(input("Enter Id : ")), str(input("Enter name: ")))
        conn.execute("""
                        insert into Offense values (?,?) 
                    """, (ab.getId(), ab.getName()))

# **********************add to person******************************************************

    def insertValueperson():
        d1 = date(input("Enter year: "), input(
            "Enter month: "), input("Enter day: "))
        by = d1.allDate()
        ab2 = Person(int(input("Enter Id: ")), input("Enter first name: "),
                     input("Enter father name: "), input("Enter last name: "),
                     input("Enter gender: "), by, input("Enter address: "))

        conn.execute("""
                    insert into Person  values(?,?,?,?,?,?,?)
                """, (ab2.getId(), ab2.getfirstName(), ab2.getFather(),
                      ab2.getlastName(), ab2.getGender(), ab2.getBirthYear(), ab2.getAddress()))

# **********************add to Convicts*****************************************************

    def insertValueConvicts():
        d1 = date(input("Enter year: "), input(
            "Enter month: "), input("Enter day: "))
        by = d1.allDate()
        d2 = date(int(input("Enter Id: ")), input("Enter year: "),
                  input("Enter month: "), input("Enter day: "))
        by1 = d2.allDate()
        ab1 = Convicts(by, by1,
                       int((input("Enter Person Id: "))), int((input("Enter Offense Id: "))))
        conn.execute("""
                        insert into Convicts values(?,?,?,?,?)
                    """, (ab1.getId(), ab1.getfromDate(),
                          ab1.gettoDate(), ab1.getPersonId(), ab1.getOffenseId()))

# **********************add to Dungeon******************************************************

    def insertValueDungeon():
        d = Dungeon(int(input("Enter Id: ")), input(
            "Enter name: "), int(input("Enter size: ")))
        conn.execute("""
                        insert into Dungeon  values(?,?,?)
                    """, (d.getId(), d.getName(), d.getSize()))

# **********************add to DungeonMoves**************************************************

    def insertValueDungeonMoves():
        d2 = date(input("Enter year: "), input(
            "Enter month: "), input("Enter day: "))
        by2 = d2.allDate()
        dn = DungeonMoves(int(input("Enter Id: ")), int(input("Enter DungeonId: ")),
                          int(input("Enter PersonId: ")), by2)
        conn.execute("""
                        insert into DungeonMoves  values(?,?,?,?)
                    """, (dn.getId(), dn.getDungeonId(),
                          dn.getPersonId(), dn.getFromDate()))

# **********************add to Visitings*****************************************************

    def insertValueVisitings():
        d3 = date(input("Enter year: "), input(
            "Enter month: "), input("Enter day: "))
        by3 = d3.allDate()
        v = Visitings(int(input("Enter Id: ")), by3, int(input("Enter PersonId: ")),
                      input("Enter VisitorName: "), int(input("Enter MontinMinutes: ")))
        conn.execute("""
                        insert into Visitings  values(?,?,?,?,?)
                    """, (v.getId(), v.getDateVisited(), v.getPersonId(),
                          v.getVisitorName(), v.getMontinMinutes()))

    # *****************أسماء المحكومين وفق جرم معين****************************************
    '''

    def selectValueNamePerson():
        inputx = input("Name offense  :")
        abd.execute("""
        select Person.firstName from Person where Person.Id =(SELECT Convicts.personId from Convicts where
        Convicts.offenseId=(SELECT Offense.Id from Offense WHERE Offense.Name="inputx"))
                    """)
    selectValueNamePerson()

    '''
    # *****************أسماء المحكومين وفق جرم معين****************************************

    def select_person_convict():
        name = input("Enter convicts name: ")
        conn.execute("""select Person.firstName 
                        from Person 
                        where Person.Id =(SELECT Convicts.personId
                            from Convicts where
                            Convicts.offenseId=(SELECT Offense.Id
                            from Offense WHERE Offense.Name='{}'))
                        """.format(name))
        abd.commit()
        print(conn.fetchall())

    # *******************قائمة الزيارات التي حصلت خالل زمنين ****************************

    def select_visitings_between_tow_dates():
        year = input("Enter from year : ")
        month = input("Enter from month : ")
        day = input("Enter from day : ")
        date_search1 = date(year, month, day)
        year_date_search2 = input("Enter to year : ")
        month_date_search2 = input("Enter to month : ")
        day_date_search2 = input("Enter to day : ")
        date_search2 = date(year_date_search2,
                            month_date_search2, day_date_search2)
        dat1 = date_search1.allDate()
        dat2 = date_search2.allDate()
        conn.execute("""SELECT Visitings.Id,
            Visitings.dateVisited,
            Visitings.visitorName,
            Visitings.mountinMinutes,
            (select (Person.FirstName||" "||Person.LastName) from Person where Person.Id=Visitings.PersonId) as presoned_name
            from Visitings 
            where (Visitings.dateVisited > ? and Visitings.dateVisited < ?)
            or ((Visitings.dateVisited < ? and Visitings.dateVisited > ?)) """, (dat1, dat2, dat1, dat2))
        abd.commit()
        print(conn.fetchall())
    # ****************قائمة بالسجناء الذين تم الحكم عليهم ضمن زمنين********************

    def SelectValueBetweenTowDates():
        year = input("Enter from year : ")
        month = input("Enter from month : ")
        day = input("Enter from day : ")
        date_search1 = date(year, month, day)
        year_date_search2 = input("Enter to year : ")
        month_date_search2 = input("Enter to month : ")
        day_date_search2 = input("Enter to day : ")
        date_search2 = date(year_date_search2,
                            month_date_search2, day_date_search2)
        dat1 = date_search1.allDate()
        dat2 = date_search2.allDate()
        conn.execute(
            """select * 
                from Person 
                where Person.Id in
                (select Convicts.PersonId 
                from Convicts 
                where (fromDate >(?) and fromDatete<(?)) or 
                (fromDate <(?) and fromDate>(?)))
                """, (dat1, dat2, dat1, dat2))
        abd.commit()
        print(conn.fetchall())

# **************دالة إرجاع اسماء الزنزانات التي انتقل خلالها سجين***********************
    def select_dungeon_person_moves():
        name = input("Enter presoner first name: ")
        lname = input("Enter presoner last name: ")
        conn.execute(
            """select Dungeon.Name
                from Dungeon where 
                Dungeon.Id in
                (select DungeonMoves.dungeonId 
                from DungeonMoves where 
                personId=(select Person.Id 
                from Person where Person.fristName=? and Person.lastName=?))
                """, (name, lname))
        abd.commit()
        print(conn.fetchall())

    # ********دوال تقوم بحفظ البيانات ضمن ملفات نصية )إضافة سجين- إضافة جرم ..... الخ(******************
    '''
    #****************هذه من اجل الدوال النصية ************************
    Prosen_file = open('Prosen.txt' ,'a') 
    write_Prosen= open('Prosen.txt' ,'a') 
    my_Prosen = ['my name is Abdulrhman AL-Sraqpi \n and my age is 20 \n and I`m studying in the university'] 
    write_Prosen.writelines(my_Prosen)
    '''
    # ******************UPDATE to Typle Offense*************************

    def UPDATE_Offense():
        co = Offense()
        NewName = co.setName(input("Enter New Name :"))
        NewId = co.setId(input("Enter New Id :"))
        co.getId()
        co.getName()
        abd.execute("""
        update Offense set Name='?' where Id=?
                    """).format(NewName, NewId)
        abd.commit()
        print(conn.fetchall())

    # ******************UPDATE to Typle Convicts *************************
    #( Id, fromDate, toDate, PersonId, OffenseId)

    def UPDATE_Convicts():
        co1 = Convicts()
        co1.setId(input("Enter New Id :"))
        co1.setfromDate(input("Enter New fromDate :"))
        co1.settoDate(input("Enter New toDate :"))
        co1.setPersonId(input("Enter New Person Id :"))
        co1.setfromDate(input("Enter New Offense Id :"))
        NewId = co1.getId()
        NewfromDate = co1.getfromDate()
        NewtoDate = co1.gettoDate()
        NewPersonId = co1.getPersonId()
        NewOffenseId = co1.getOffenseId()

        abd.execute("""
        update Convicts set fromDate='?',toDate='?',PersonId=?,OffenseId=? where Id=?
                    """).format(NewfromDate, NewtoDate, NewPersonId, NewOffenseId, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************fromDate

    def UPDATE_Convicts_fromDate():
        co11 = Convicts()
        co11.setId(input("Enter New Id :"))
        co11.setfromDate(input("Enter New fromDate :"))
        NewfromDate = co11.getfromDate()
        NewId = co11.getId()
        abd.execute("""
        update Convicts set fromDate='?' where Id=?
                    """).format(NewfromDate, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************toDate

    def UPDATE_Convicts_toDate():
        co12 = Convicts()
        co12.setId(input("Enter New Id :"))
        co12.settoDate(input("Enter New toDate :"))
        NewtoDate = co12.gettoDate()
        NewId = co12.getId()
        abd.execute("""
        update Convicts set toDate='?' where Id=?
                    """).format(NewtoDate, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************PersonId

    def UPDATE_Convicts_PersonId():
        co11 = Convicts()
        co11.setId(input("Enter New Id :"))
        co11.setPersonId(int(input("Enter New PersonId :")))
        NewPersonId = co11.getPersonId()
        NewId = co11.getId()
        abd.execute("""
        update Convicts set PersonId='?' where Id=?
                    """).format(NewPersonId, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************OffenseId

    def UPDATE_Convicts_OffenseId():
        co11 = Convicts()
        co11.setId(input("Enter New Id :"))
        co11.setOffenseId(int(input("Enter New OffenseId :")))
        NewOffenseId = co11.getOffenseId()
        NewId = co11.getId()
        abd.execute("""
        update Convicts set OffenseId='?' where Id=?
                    """).format(NewOffenseId, NewId)
        abd.commit()
        print(conn.fetchall())
    # ******************UPDATE to Typle Person *************************
    #(Id, FirstName, Father, LastName, Gender, BirthYear, Address)

    def UPDATE_Person():
        co2 = Person()
        co2.setId(input("Enter New Id :"))
        co2.setfirstName(input("Enter New FirstName :"))
        co2.setFather(input("Enter New Father :"))
        co2.setlastName(input("Enter New LastName :"))
        co2.setGender(input("Enter New Gender :"))
        co2.setBirthYear(input("Enter New BirthYear :"))
        co2.setAddress(input("Enter New Address :"))
        NewId = co2.getId()
        NewFirstName = co2.getfirstName()
        NewFather = co2.getFather()
        NewLastName = co2.getlastName()
        NewGender = co2.getGender()
        NewBirthYear = co2.getBirthYear()
        NewAddress = co2.getAddress()
        abd.execute("""
        update Person set FirstName='?',Father='?',LastName='?',Gender='?',BirthYear='?',Address='?' where Id=?
        """).format(NewFirstName, NewFather, NewLastName, NewGender, NewBirthYear, NewAddress, NewId)

        abd.commit()
        print(conn.fetchall())

# ********************FirstName

    def UPDATE_Person_FirstName():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setfirstName(input("Enter New FirstName :"))
        NewId = co21.getId()
        NewFirstName = co21.getfirstName()
        abd.execute("""
        update Person set FirstName='?' where Id=?
        """).format(NewFirstName, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Father

    def UPDATE_Person_Father():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setFather(input("Enter New Father :"))
        NewId = co21.getId()
        NewFather = co21.getFather()
        abd.execute("""
        update Person set Father='?' where Id=?
        """).format(NewFather, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************LastName

    def UPDATE_Person_LastName():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setLastName(input("Enter New LastName :"))
        NewId = co21.getId()
        NewLastName = co21.getLastName()
        abd.execute("""
        update Person set LastName='?' where Id=?
        """).format(NewLastName, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Gender

    def UPDATE_Person_Gender():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setGender(input("Enter New Gender :"))
        NewId = co21.getId()
        NewGender = co21.getGender()
        abd.execute("""
        update Person set Gender='?' where Id=?
        """).format(NewGender, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************BirthYear

    def UPDATE_Person_BirthYear():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setBirthYear(input("Enter New BirthYear :"))
        NewId = co21.getId()
        NewBirthYear = co21.getBirthYear()
        abd.execute("""
        update Person set BirthYear='?' where Id=?
        """).format(NewBirthYear, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Address

    def UPDATE_Person_Address():
        co21 = Person()
        co21.setId(int(input("Enter Id :")))
        co21.setAddress(input("Enter New Address :"))
        NewId = co21.getId()
        NewAddress = co21.getAddress()
        abd.execute("""
        update Person set Address='?' where Id=?
        """).format(NewAddress, NewId)
        abd.commit()
        print(conn.fetchall())

    # ******************UPDATE to Typle Dungeon *************************
    #(self, Id, Name, Size)

    def UPDATE_Dungeon():
        co3 = Dungeon()
        NewId = co3.setId(input("Enter New Id : "))
        NewName = co3.setName(input("Enter New Name :"))
        NewSize = co3.setSize(input("Enter new Size :"))
        co3.getId()
        co3.getName()
        co3.getSize()
        abd.execute("""
        update Dungeon set Name='?',Size=?, where Id=?
        """).format(NewName, NewSize, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Name

    def UPDATE_Dungeon_Name():
        co3 = Dungeon()
        NewId = co3.setId(input("Enter New Id : "))
        NewName = co3.setName(input("Enter New Name :"))
        co3.getId()
        co3.getName()
        abd.execute("""
        update Dungeon set Name='?' where Id=?
        """).format(NewName, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Size

    def UPDATE_Dungeon_Size():
        co3 = Dungeon()
        NewId = co3.setId(input("Enter New Id : "))
        NewSize = co3.setSize(input("Enter New Size :"))
        co3.getId()
        co3.getSize()
        abd.execute("""
        update Dungeon set Size=? where Id=?
        """).format(NewSize, NewId)
        abd.commit()
        print(conn.fetchall())

    # ******************UPDATE to Typle Dungeon *************************
    #(self, Id, DateVisited, PersonId, VisitorName, MountinMinutes)

    def UPDATE_Visitings():
        co3 = Visitings()
        NewId = co3.setId(input("Enter New Id : "))
        NewDateVisited = co3.DateVisited(input("Enter New Date Visited :"))
        NewPersonId = co3.PersonId(input("Enter New Person Id : "))
        NewVisitorName = co3.VisitorName(input("Enter new Visitor Name :"))
        NewMountinMinutes = co3.MountinMinutes(
            input("Enter New Mountin Minutes : "))
        co3.getId()
        co3.getDateVisited()
        co3.getPersonId()
        co3.getVisitorName()
        co3.getMountinMinutes()
        abd.execute("""
        update Dungeon set DateVisited='?',PersonId=?,VisitorName='?',MountinMinutes=? where Id=?
        """).format(NewDateVisited, NewPersonId, NewVisitorName, NewMountinMinutes, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************Visited

    def UPDATE_Visitings_Visited():
        co31 = Visitings()
        co31.setId(input("Enter New Id : "))
        co31.setDateVisited(input("Enter New Date Visited :"))
        NewId = co31.getId()
        NewDateVisited = co31.getDateVisited()
        abd.execute("""
        update Dungeon set DateVisited='?' where Id=?
        """).format(NewDateVisited, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************PersonId

    def UPDATE_Visitings_PersonId():
        co32 = Visitings()
        co32.setId(input("Enter New Id :"))
        co32.setPersonId(int(input("Enter New PersonId :")))
        NewPersonId = co32.getPersonId()
        NewId = co32.getId()
        abd.execute("""
        update Visitings set PersonId='?' where Id=?
                    """).format(NewPersonId, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************VisitorName

    def UPDATE_Visitings_VisitorName():
        co31 = Visitings()
        NewId = co31.setId(input("Enter New Id : "))
        NewDateVisitorName = co31.DateVisitorName(
            input("Enter New Date VisitorName :"))
        co31.getId()
        co31.getVisitorName()
        abd.execute("""
        update Dungeon set VisitorName='?' where Id=?
        """).format(NewDateVisitorName, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************MountinMinutes

    def UPDATE_Visitings_MountinMinutes():
        co32 = Visitings()
        co32.setId(input("Enter New Id :"))
        co32.setMontinMinutes(int(input("Enter New MountinMinutes :")))
        NewMountinMinutes = co32.getMontinMinutes()
        NewId = co32.getId()
        abd.execute("""
        update Visitings set MountinMinutes='?' where Id=?
                    """).format(NewMountinMinutes, NewId)
        abd.commit()
        print(conn.fetchall())

    # ******************UPDATE to Typle DungeonMoves *************************
    #(self, Id, DungeonId, PersonId, FromDate)

    def UPDATE_DungeonMoves():
        co3 = DungeonMoves()
        NewId = co3.setId(input("Enter New Id : "))
        NewDungeonId = co3.serDungeonId(input("Enter New  Dungeon Id :"))
        NewPersonId = co3.setPersonId(input("Enter New Person Id : "))
        NewFromDate = co3.setFromDate(input("Enter new FromDate :"))
        co3.getId()
        co3.getDungeonId()
        co3.getPersonId()
        co3.getFromDate()
        abd.execute("""
        update Dungeon set DungeonId='?',PersonId='?', formData='?' where Id=?
        """).format(NewDungeonId, NewPersonId, NewFromDate, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************DungeonId

    def UPDATE_DungeonMoves_DungeonId():
        co41 = DungeonMoves()
        NewId = co41.setId(input("Enter New Id : "))
        NewDungeonId = co41.serDungeonId(input("Enter New  Dungeon Id :"))
        co41.getId()
        co41.getDungeonId()
        abd.execute("""
        update Dungeon set DungeonId='?' where Id=?
        """).format(NewDungeonId,  NewId)
        abd.commit()
        print(conn.fetchall())

# ********************PersonId

    def UPDATE_DungeonMoves_PersonId():
        co32 = DungeonMoves()
        co32.setId(input("Enter New Id :"))
        co32.setPersonId(int(input("Enter New PersonId :")))
        NewPersonId = co32.getPersonId()
        NewId = co32.getId()
        abd.execute("""
        update DungeonMoves set PersonId='?' where Id=?
                    """).format(NewPersonId, NewId)
        abd.commit()
        print(conn.fetchall())

# ********************NewFromDate

    def UPDATE_DungeonMoves_NewFromDate():
        co41 = DungeonMoves()
        NewId = co41.setId(input("Enter New Id : "))
        NewFromDate = co41.setFromDate(input("Enter New  NewFromDate  :"))
        co41.getId()
        co41.getFromDate()
        abd.execute("""
        update DungeonMoves set formData='?' where Id=?
        """).format(NewFromDate,  NewId)
        abd.commit()
        print(conn.fetchall())

except Exception:
    print(Exception)


# **********************While to Offense********************************1***************

while True:
    insertValueOffense()
    stop = input("if you  stop click y or n: ")
    if stop == "y" or stop == "n":
        break

# **********************While to Person*********************************2***************

while True:
    insertValueperson()
    stop = input("if you  stop click y or n: ")
    if stop == "y" or stop == "n":
        break


# *************************While to Convicts******************************3*************

    while True:

        insertValueConvicts()
        stop = input("if you  stop click y or n: ")
        if stop == "y" or stop == "n":
            break


# *******************While to DungeonMoves*******************************4**************

    while True:

        insertValueDungeonMoves()
        stop = input("if you  stop click y or n: ")
        if stop == "y" or stop == "n":
            break

# *********************While to Dungeon***************************************5*********

    while True:
        insertValueDungeon()
        stop = input("if you  stop click y or n: ")
        if stop == "y" or stop == "n":
            break

# **************************While to Visitings********************************6**********

while True:

    insertValueVisitings()
    stop = input("if you  stop click y or n: ")
    if stop == "y" or stop == "n":
        break

SelectValueBetweenTowDates()
select_dungeon_person_moves()
select_visitings_between_tow_dates()
select_person_convict()
'''
# ******************Delete to Typle offense*************************


def deleteValueOffense():
    conn.execute("""
                    delete from Offense 
                """)


deleteValueOffense()
print("True : : :  :Delete Offense:")
#conn.execute("""delete from Offense""")
# ******************Delete to Typle Convicts*************************


def deleteValueConvicts():
    conn.execute("""
                    delete from Convicts 
                """)


deleteValueConvicts()
print("True : : :  :Delete Convicts:")
# ******************Delete to Typle Person*************************


def deleteValuePerson():
    conn.execute("""
                    delete from Person 
                """)


deleteValuePerson()
print("True : : :  :Delete  Person:")

# ******************Delete to Typle Dungeon*************************


def deleteValueDungeon():
    conn.execute("""
                    delete from Dungeon 
                """)


deleteValueDungeon()
print("True : : :  :Delete Dungeon:")

# ******************Delete to Typle Visitings*************************


def deleteValueVisitings():
    conn.execute("""
                    delete from Visitings 
                """)


deleteValueVisitings()
print("True : : :  :Delete Visitings:")

# ******************Delete to Typle DungeonMoves*************************


def deleteValueDungeonMoves():
    conn.execute("""
                    delete from DungeonMoves 
                """)


deleteValueDungeonMoves()

print("True : : :  :Delete DungeonMoves :")
print("True : : :  : :")
'''
 
print("True : : :  : :")
abd.commit()
abd.close()
