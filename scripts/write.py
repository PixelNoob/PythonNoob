# append
f = open("write_to_file.txt", "a")
f.write("Cualquier cosa!\n")
f.close()

#open and read the file after the appending:
f = open("write_to_file.txt", "r")
print(f.read())

# write over it!
#f = open("write_to_file.txt", "w")
#f.write("lo borre sapo teton!")
#f.close()
