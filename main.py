import MySQLdb
import pickle
import numpy as np

pkl_filename = "progkmeans.pkl"

with open(pkl_filename, 'rb') as file:

    pickle_model = pickle.load(file)

# Connect to server
cnx = MySQLdb.connect(
     user = "root",
     password = "",
     database = "stechoq")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT sensor1_ch4, sensor1_co, sensor1_h2, sensor2_co, sensor3_ch4, sensor4_nh3, sensor5_h2, sensor6_co, sensor6_h2, sensor6_c4h10 FROM tangkap_sensor_1_ppm ORDER BY id desc limit 1")

result = cur.fetchall()

for row in result:
    row = np.asarray(row)
    row = row.reshape(1, -1)
    hasil = pickle_model.predict((row))
    print(hasil)
    hasilstr = ''
    if (hasil==0):
        hasilstr = 'Udara Bersih'
    else:
        hasilstr = 'Udara Kotor'
    print(hasilstr)
    # cur.execute(f'INSERT INTO klasifikasi_industry({hasil}) VALUES ({hasilstr})')
    cur.execute(f"INSERT INTO klasifikasi_industry (hasil, waktu) VALUES ('{hasilstr}', now())")
    cnx.commit()
    # print([[row]])
    # print("\n")

cnx.close()