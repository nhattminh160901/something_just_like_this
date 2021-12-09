import pickle
with open("d"+".pickle", "rb") as f:
    readfile = pickle.load(f)
    f.close()
print(readfile)