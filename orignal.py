from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


   

def mine(block_number, transactions, previous_hash, prefix_zeros):
    c=0
    prefix_str = '0'*prefix_zeros
    pattern_num1=1
    pattern_num2=2
    pattern_num3=3
    pattern_num4=4
    pattern_num5=5
    pattern_num6=6
    pattern_num7=7
    pattern_num8=8
    pattern_num9=9
    pattern_num10=10

    for j in range(MAX_NONCE):
        pattern_num1+=(pattern_num1*10)+pattern_num1
        pattern_num2=(pattern_num2*10)+pattern_num2
        pattern_num3=(pattern_num3*10)+pattern_num3
        pattern_num4=(pattern_num4*10)+pattern_num4
        pattern_num5=(pattern_num5*10)+pattern_num5
        pattern_num6=(pattern_num6*10)+pattern_num6
        pattern_num7=(pattern_num7*10)+pattern_num7
        pattern_num8=(pattern_num8*10)+pattern_num8
        pattern_num9=(pattern_num9*10)+pattern_num9
        pattern_num10=(pattern_num10*10)+pattern_num10
        c=c+1
        if(c==9):
            pattern_num1=1
            pattern_num2=2
            pattern_num3=3
            pattern_num4=4
            pattern_num5=5
            pattern_num6=6
            pattern_num7=7
            pattern_num8=8
            pattern_num9=9
            pattern_num10=10


        for nonce in range(MAX_NONCE):
            text = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', nonce)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
                return new_hash
            nonce2=nonce*nonce
            text = str(block_number) + transactions + previous_hash + str(nonce2)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce2 :', nonce2)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce2}")
                return new_hash

            nonce3=nonce**3
            text = str(block_number) + transactions + previous_hash + str(nonce3)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce3 :', nonce3)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce3}")
                return new_hash
            nonce4=nonce2+1
            text = str(block_number) + transactions + previous_hash + str(nonce4)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce4 :', nonce4)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce4}")
                return new_hash
            nonce5=nonce3+1
            text = str(block_number) + transactions + previous_hash + str(nonce5)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce4 :', nonce5)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce5}")
                return new_hash
            digits = len(str(nonce))
            nonce6=pattern_num1*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce6)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce 6', nonce6)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce6}")
                return new_hash


            nonce7=pattern_num2*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce7)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce7', nonce7)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce7}")
                return new_hash
            nonce8=pattern_num3*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce8)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce8 is', nonce8)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce8}")
                return new_hash
            nonce9=pattern_num4*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce9)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce9 is', nonce9)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce9}")
                return new_hash


            nonce10=pattern_num5*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce10)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is 10', nonce10)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce10}")
                return new_hash

            nonce11=pattern_num6*(10**digits)+nonce

            text = str(block_number) + transactions + previous_hash + str(nonce11)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce11 is', nonce11)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce11}")
                return new_hash

            nonce12=pattern_num7*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce12)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce12 is', nonce12)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce12}")
                return new_hash
            nonce13=pattern_num8*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce13)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is13', nonce13)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce13}")
                return new_hash

            nonce14=pattern_num9*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce14)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is14', nonce14)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce14}")
                return new_hash
            nonce15=pattern_num10*(10**digits)+nonce
            text = str(block_number) + transactions + previous_hash + str(nonce15)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce15 is', nonce15)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce15}")
                return new_hash





    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=6 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("started mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
    print('level was', difficulty)
