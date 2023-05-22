print("Encryption Program")
inp_fname = input("Enter the input filename: ")
out_fname = input("Enter the output filename: ")
with open(inp_fname, 'rb') as inp_f, open(out_fname, 'wb') as out_f:
 while True:
  byte = inp_f.read(1)
  if not byte:
   break
  out_f.write(bytes([byte[0] + 5]))

# print("Decryption Program")
# inp_fname = input("Enter the input filename: ")
# out_fname = input("Enter the output filename: ")
# with open(inp_fname, 'rb') as inp_f, open(out_fname, 'wb') as out_f:
#  while True:
#   byte = inp_f.read(1)
#   if not byte:
#    break
 
#  out_f.write(bytes([byte[0] - 5]))
#  print(f"Encrypted Message: {byte}")
#  print(f"Decrypted Message: {byte[0] - 5}")