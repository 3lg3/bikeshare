
import requests
import time
import psycopg2

conn = psycopg2.connect(dbname="bikeshare", user="qihang", password="qihang", port=9527)
URL = 'https://lime.bike/api/partners/v1/gbfs/free_bike_status.json'
URL2 = 'https://dc.jumpmobility.com/opendata/free_bike_status.json'
URL3 = 'https://gbfs.bird.co/dc'
URL4 = 'https://web.spin.pm/api/gbfs/v1/washington_dc/free_bike_status'
URL5 = 'https://sf.jumpbikes.com/opendata/free_bike_status.json'

while 1:
    #lime_DC
    response = requests.get(URL)
    data = response.json()
    t = data['last_updated']
    t_readable = time.ctime(t)
    bike_list = data["data"]["bikes"]
    for i in range(0, len(bike_list)):
        bike_list[i]['time'] = t
    print('\nlast updated:', t_readable)
    cur = conn.cursor()
    for i in range(0, len(data["data"]["bikes"])):
        row = []
        for key, value in data["data"]["bikes"][i].items():
            row.append(value)
        cur.execute("INSERT INTO dc_lime (bike_id,is_reserved,is_disabled,vehicle_type,  location,time) \
        VALUES (" + '\'' + str(row[0]) +'\'' + ',' + '\'' + str(row[3]) + '\'' + ',' + '\'' + str(row[4]) + '\'' + ',' + '\''+ str(row[5]) +'\'' +',' + '\'' + '('
                    + str(row[1]) + ',' + str(row[2]) + ')' +'\'' + ',' + '\'' + str(row[6]) + '\'' + ')')
    cur.close()
    conn.commit()

    #jump_DC
    response = requests.get(URL2)
    data = response.json()
    #t = data['last_updated']
    #t_readable = time.ctime(t)
    bike_list = data["data"]["bikes"]
    for i in range(0, len(bike_list)):
        bike_list[i]['time'] = t
    cur = conn.cursor()
    for i in range(0, len(data["data"]["bikes"])):
        row = []
        for key, value in data["data"]["bikes"][i].items():
            row.append(value)
        cur.execute("INSERT INTO dc_jump (bike_id,is_reserved,is_disabled,vehicle_type,  location,time) \
        VALUES (" + '\'' + str(row[0]) +'\'' + ',' + '\'' + str(row[4]) + '\'' + ',' + '\'' + str(row[5]) + '\'' + ',' + '\''+ str(row[7]) +'\'' +',' + '\'' + '('
                    + str(row[2]) + ',' + str(row[3]) + ')' +'\'' + ',' + '\'' + str(row[8]) + '\'' + ')')
    cur.close()
    conn.commit()

    #bird
    response = requests.get(URL3)
    data = response.json()
    #t = data['last_updated']
    #t_readable = time.ctime(t)
    bike_list = data["data"]["bikes"]
    for i in range(0, len(bike_list)):
        bike_list[i]['time'] = t
    cur = conn.cursor()
    for i in range(0, len(data["data"]["bikes"])):
        row = []
        for key, value in data["data"]["bikes"][i].items():
            row.append(value)
        #print(row)
        cur.execute("INSERT INTO dc_bird (bike_id,vehicle_type,  location,time) \
            VALUES (" + '\'' + str(row[0]) + '\'' + ',' + '\'' + str(row[4]) + '\'' + ',' + '\'' + '('
                    + str(row[1]) + ',' + str(row[2]) + ')' + '\'' + ',' + '\'' + str(row[7]) + '\'' + ')')
    cur.close()
    conn.commit()

    # spin
    response = requests.get(URL4)
    data = response.json()
    # t = data['last_updated']
    # t_readable = time.ctime(t)
    bike_list = data["data"]["bikes"]
    for i in range(0, len(bike_list)):
        bike_list[i]['time'] = t
    cur = conn.cursor()
    for i in range(0, len(data["data"]["bikes"])):
        row = []
        for key, value in data["data"]["bikes"][i].items():
            row.append(value)
        cur.execute("INSERT INTO dc_spin (bike_id,is_reserved,is_disabled,vehicle_type,  location,time) \
        VALUES (" + '\'' + str(row[0]) +'\'' + ',' + '\'' + str(row[4]) + '\'' + ',' + '\'' + str(row[5]) + '\'' + ',' + '\''+ str(row[3]) +'\'' +',' + '\'' + '('
                    + str(row[1]) + ',' + str(row[2]) + ')' +'\'' + ',' + '\'' + str(row[6]) + '\'' + ')')
    cur.close()
    conn.commit()

    #jump_sf
    response = requests.get(URL5)
    data = response.json()
    #t = data['last_updated']
    #t_readable = time.ctime(t)
    bike_list = data["data"]["bikes"]
    for i in range(0, len(bike_list)):
        bike_list[i]['time'] = t
    cur = conn.cursor()
    for i in range(0, len(data["data"]["bikes"])):
        row = []
        for key, value in data["data"]["bikes"][i].items():
            row.append(value)
        cur.execute("INSERT INTO sf_jump (bike_id,is_reserved,is_disabled,vehicle_type,  location,time) \
        VALUES (" + '\'' + str(row[0]) +'\'' + ',' + '\'' + str(row[4]) + '\'' + ',' + '\'' + str(row[5]) + '\'' + ',' + '\''+ str(row[7]) +'\'' +',' + '\'' + '('
                    + str(row[2]) + ',' + str(row[3]) + ')' +'\'' + ',' + '\'' + str(row[8]) + '\'' + ')')
    cur.close()
    conn.commit()

    time.sleep(300)
