from bitcoin import *


#generating a private key 
private_key1= random_key()
private_key2= random_key()
private_key3= random_key()


#generating a public key

public_key1= random_key()
public_key2= random_key()
public_key3= random_key()


# multi-sign address

my_multi_sig = mk_multisig_script(public_key1, public_key2, public_key3,2,3)
my_multi_address =scriptaddr(my_multi_sig)
print(my_multi_address)

#view address transactions history

valid_address='bc1qczfxadks4m5gxpx2p3ulgk6l96ytc3c6a53r6yelnavzuw0zftzqv9jr7v'
print(history(valid_address))



