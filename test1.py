# Probabilitas awal
P_X = 0.45
P_Y = 0.30
P_Z = 0.25

# Probabilitas mendaftar jika diberikan versi X, Y, dan Z
P_R_given_X = 0.12
P_R_given_Y = 0.08
P_R_given_Z = 0.10

# Menggunakan teorema probabilitas bersyarat
P_X_given_R = (P_X * P_R_given_X) / (P_X * P_R_given_X + P_Y * P_R_given_Y + P_Z * P_R_given_Z)

print("Probabilitas bahwa pengguna diberikan versi X jika dia mendaftar:", P_X_given_R)