from RSA import RSA
from ECC import ECC
import data_compiler

# will compile data in csv files to show average times
data_compiler.RSA_data()
# repeat x number of times to record data x number of times
for i in range(1):
  ECC.do_ecc()
  RSA.do_rsa()
