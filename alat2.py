import MySQLdb
import pickle
import numpy as np

pkl_filename = "progkmeans.pkl"

with open(pkl_filename, 'rb') as file:

    pickle_model = pickle.load(file)

# Connect to server
cnx = MySQLdb.connect(
     user = "mbkm_enose",
     password = "",
     database = "mbkm_enose_b3")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM tangkap_sensor_2s_ppm ORDER BY id desc limit 1")

result = cur.fetchall()
for row in result:
    id = row[0]
    data = row[2:12]
    data = np.asarray(data)
    data = data.reshape(1, -1)
    hasil = pickle_model.predict((data))
    print(hasil)
    hasilstr = ''
    if (hasil==0):
        hasilstr = 'Udara Bersih'
    else:
        hasilstr = 'Udara Kotor'
    print(id)
    cur.execute(f"UPDATE tangkap_sensor_1_ppm SET hasil='{hasilstr}' WHERE id = {id}")
    cnx.commit()

cnx.close()
