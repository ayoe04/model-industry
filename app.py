import MySQLdb
import pickle

# Connect to server
cnx = MySQLdb.connect(
     user = "root",
     password = "",
     database = "stechoq")

# Get a cursor
cur = cnx.cursor()

# Execute a query
data = cur.execute("SELECT * FROM tangkap_sensor_1_ppm")

# load pkl
pkl_filename = "progkmeans.pkl"

with open(pkl_filename, 'rb') as file:

    pickle_model = pickle.load(file)
    
# print(pickle_model.predict([[1.26, 1.17, 0.77, 0.0, 0.0, 0.19, 304557000.0, 0.07, 0.07, 0.04]]))

print(pickle_model.predict(data))

# tampilkan di dashboard
hasil = 'Bersih' if pickle_model.predict(data) == 0 else 'Kotor'
    
# disconnect from server

cnx.close()