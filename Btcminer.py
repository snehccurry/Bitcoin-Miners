import hashlib

NONCE_LIMIT= 100000000000

zeros=6

#print(hashlib.sha256("Hello World".encode()).hexdigest())

'''def mine(block_number, transactions, previous_hash):
	for nonce in range(NONCE_LIMIT):
		base_text = str(block_number)+ transactions+previous_hash+str(nonce)
		hash_try= hashlib.sha256(base_text.encode()).hexdigest()
		if hash_try.startswith('0'* zeros):
			print(f"found hash with Nonce: {nonce}")
			return hash_try

	return -1
'''
'''
block_number=24
transactions="76123fcc2142"
previous_hash="876de8756967c87"
'''
#combined_text= str(block_number)+ transactions+previous_hash
#print(hashlib.sha256(combined_text.encode()).hexdigest())
'''
mine(block_number, transactions, previous_hash)
'''

combined_text= '00000021c251a735b47c72aec01a1803db7660f1fb6ccd2a7e8fb416645f90f6'
print(hashlib.sha256(combined_text.encode()).hexdigest())