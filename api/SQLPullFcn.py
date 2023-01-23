import mysql.connector

def SQL_Pull(firstname, lastname):

    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='jAjtd5G4Y3ABjr',
        database="UFCPredictor"
    )

    mycursor = mydb.cursor()

    mydb.raise_on_warnings = True

    query = "SELECT * FROM fighterstats WHERE firstname = %s AND lastname = %s"

    mycursor.execute(query, (firstname, lastname))

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        data = 'NULL'
    else:
        for row in myresult:
            data = row

    #print(data)

    #stat_standing = data[9]
    #print(stat_standing)

    if data == 'NULL':
        return data
    else:
        #data[0]
        #data[1]
        weight = data[2]
        height = data[3]
        age = data[4]
        strikeacc = data[5]
        tdacc = data[6]
        armreach = data[7]
        legreach = data[8]
        standing = data[9]
        clinch = data[10]
        ground = data[11]
        kotko = data[12]
        decision = data[13] 
        sub = data[14] 

        return [str(x) for x in (weight, height, age, strikeacc, tdacc, armreach, legreach, standing, clinch, ground, kotko, decision, sub)]

jones = SQL_Pull('jon', 'jones')
print(jones)

        

