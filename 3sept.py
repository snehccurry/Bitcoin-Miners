from hashlib import sha256
MAX_NONCE = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

  


    

def mine(block_number, transactions, previous_hash, prefix_zeros):
    c_power=10
    prefix_str = '0'*prefix_zeros
    for i in range(1,MAX_NONCE,1):
        nonce=i
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print('nonce is  ', nonce)
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            found=1
            return new_hash

        for j in range(1,11,1):

            product=i*j
            text = str(block_number) + transactions + previous_hash + str(product)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is product ', product)
                print('product was of ',i,"*",j)
                print(f"Yay! Successfully mined bitcoins with nonce value:{product}")
                found=1
                return new_hash
                
                break
            power=product
            
            for k in range(1,c_power,1):
                nonce4=power+k
                text = str(block_number) + transactions + previous_hash + str(nonce4)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    print('nonce4 is', nonce4)
                    print(f"Yay! Successfully mined bitcoins with nonce value:{nonce4}")
                    return new_hash
                nonce5=power-k
                text = str(block_number) + transactions + previous_hash + str(nonce5)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    print('none5 is ',nonce5)
                    print(f"Yay! Successfully mined bitcoins with nonce value:{nonce5}")
                    return new_hash

            power=2*j
            digits = len(str(power))
            if(nonce>1000):
                c_power_2=10
            elif(nonce>10000):
                c_power_2=100
            elif(nonce>1000000):
                c_power_2=150
            elif(nonce>100000000):
                c_power_2=500
            elif(nonce>1000000000):
                c_powe_2r=1000
            elif(nonce>10000000000000000):
                c_power_2=100000
            else:
                c_power_2=10


            text = str(block_number) + transactions + previous_hash + str(power)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is power ', power)
                print('power was of ',i,"**",j)
                print(f"Yay! Successfully mined bitcoins with nonce value:{power}")
                found=1
                return new_hash
            for k in range(1,c_power_2,1):
                nonce6=power+k
                text = str(block_number) + transactions + previous_hash + str(nonce6)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    print('nonce6 is', nonce6)
                    print(f"Yay! Successfully mined bitcoins with nonce value:{nonce6}")
                    return new_hash
                nonce7=power-k
                text = str(block_number) + transactions + previous_hash + str(nonce7)
                new_hash = SHA256(text)
                if new_hash.startswith(prefix_str):
                    print('none7 is ',nonce7)
                    print(f"Yay! Successfully mined bitcoins with nonce value:{nonce7}")
                    return new_hash



        
                
            break       
        if(nonce>1000):
            c_power=10
        elif(nonce>10000):
            c_power=100
        elif(nonce>1000000):
            c_power=150
        elif(nonce>100000000):
            c_power=500
        elif(nonce>1000000000):
            c_power=1000
        elif(nonce>10000000000000000):
            c_power=100000
        else:
            c_power=10

            
            
            
            
           




         
        

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")




    
if __name__=='__main__':
    transactions='''
    kapil->sam,
    abhay->Elon,
    rahul->sid
    '''
    difficulty=6# try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("started mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
    print('level was', difficulty)