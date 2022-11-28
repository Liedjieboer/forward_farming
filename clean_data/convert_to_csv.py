sheff_data = open('sheff_data.txt','r')
data = sheff_data.read()
new_data = data.replace('#','')
new_data = new_data.replace(' Provisional','')
new_data = new_data.replace('*','')
new_data = new_data.replace(' ', ',')
csv_file = open("sheff_data.csv", "w")
csv_file.write(new_data)
csv_file.close
