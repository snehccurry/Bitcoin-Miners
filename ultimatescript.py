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
    found=0
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
        if(found==1):
            print('upperone')
            break
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
           # print('nonce is', nonce)
            if new_hash.startswith(prefix_str):
                print('nonce is', nonce)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
                found=1
                return new_hash
                
                break
            nonce2=nonce*nonce
            text = str(block_number) + transactions + previous_hash + str(nonce2)
            new_hash = SHA256(text)
            #print('nonce is nonce2 :', nonce2)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce2 :', nonce2)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce2}")
                found=1
                return new_hash
                
                break
            nonce3=nonce**3
            text = str(block_number) + transactions + previous_hash + str(nonce3)
            new_hash = SHA256(text)
           # print('nonce is nonce3 :', nonce3)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce3 :', nonce3)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce3}")
                found=1
                return new_hash
                break
                
            nonce4=nonce2+1
            #print('nonce is nonce4 :', nonce4)
            text = str(block_number) + transactions + previous_hash + str(nonce4)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce4 :', nonce4)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce4}")
                found=1
                return new_hash
                
                break
            nonce5=nonce3+1
            #print('nonce is nonce5 :', nonce5)
            text = str(block_number) + transactions + previous_hash + str(nonce5)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce5 :', nonce5)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce5}")
                found=1
                return new_hash    
                break


            digits = len(str(nonce))
            nonce6=pattern_num1*(10**digits)+nonce
            #print('nonce is nonce 6', nonce6)
            text = str(block_number) + transactions + previous_hash + str(nonce6)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce 6', nonce6)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce6}")
                found=1
                return new_hash
                
                break


            nonce7=pattern_num2*(10**digits)+nonce
            #print('nonce is nonce7', nonce7)
            text = str(block_number) + transactions + previous_hash + str(nonce7)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is nonce7', nonce7)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce7}")
                found=1
                return new_hash
                
                break
            nonce8=pattern_num3*(10**digits)+nonce
            #print('nonce8 is', nonce8)
            text = str(block_number) + transactions + previous_hash + str(nonce8)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce8 is', nonce8)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce8}")
                found=1
                return new_hash
                
                break
            nonce9=pattern_num4*(10**digits)+nonce
            #print('nonce9 is', nonce9)
            text = str(block_number) + transactions + previous_hash + str(nonce9)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce9 is', nonce9)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce9}")
                found=1
                return new_hash
                
                break


            nonce10=pattern_num5*(10**digits)+nonce
            #print('nonce is 10', nonce10)
            text = str(block_number) + transactions + previous_hash + str(nonce10)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is 10', nonce10)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce10}")
                found=1
                return new_hash
                
                break

            nonce11=pattern_num6*(10**digits)+nonce
            #print('nonce11 is', nonce11)
            text = str(block_number) + transactions + previous_hash + str(nonce11)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce11 is', nonce11)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce11}")
                found=1
                return new_hash
                
                break

            nonce12=pattern_num7*(10**digits)+nonce
            #print('nonce12 is', nonce12)
            text = str(block_number) + transactions + previous_hash + str(nonce12)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce12 is', nonce12)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce12}")
                found=1
                return new_hash
                
                break
            nonce13=pattern_num8*(10**digits)+nonce
            #print('nonce13 is', nonce13)
            text = str(block_number) + transactions + previous_hash + str(nonce13)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce13 is', nonce13)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce13}")
                found=1
                return new_hash
                
                break

            nonce14=pattern_num9*(10**digits)+nonce
            #print('nonce is14', nonce14)
            text = str(block_number) + transactions + previous_hash + str(nonce14)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is14', nonce14)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce14}")
                found=1
                return new_hash
            
                break
            nonce15=pattern_num10*(10**digits)+nonce
            #print('nonce15 is', nonce15)
            text = str(block_number) + transactions + previous_hash + str(nonce15)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce15 is', nonce15)
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce15}")
                found=1
                return new_hash
                

          
            
            

         
        if(found==1):
            print('lower one')
            break

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")




    
if __name__=='__main__':
    transactions='''
    DDhaval->BBhavin->220,
    MMando->CCara->445,
    '''
    difficulty=10 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("started mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
    print('level was', difficulty)
























#special nonce, where you check probability by 1k close to numbers., 1k will change according to power
''' if(nonce>20000):
                for close_range_checker in range(1000):
                    nonce26=nonce2+close_range_checker
                    print('nonce26 is', nonce26)
                    text = str(block_number) + transactions + previous_hash + str(nonce26)
                    new_hash = SHA256(text)
                    if new_hash.startswith(prefix_str):
                        print('nonce26 is', nonce26)
                        print(f"Yay! Successfully mined bitcoins with nonce value:{nonce26}")
                        found=1
                        return new_hash
                        break


                    nonce27=nonce3+close_range_checker
                    text = str(block_number) + transactions + previous_hash + str(nonce27)
                    print('nonce27 is', nonce27)
                    new_hash = SHA256(text)
                    if new_hash.startswith(prefix_str):
                        print('nonce27 is', nonce27)
                        print(f"Yay! Successfully mined bitcoins with nonce value:{nonce27}")
                        found=1
                        return new_hash
                    

                    nonce28=nonce2-close_range_checker
                    text = str(block_number) + transactions + previous_hash + str(nonce28)
                    print('nonce28 is', nonce28)
                    new_hash = SHA256(text)
                    if new_hash.startswith(prefix_str):
                        print('nonce28 is', nonce28)
                        print(f"Yay! Successfully mined bitcoins with nonce value:{nonce28}")
                        found=1
                        return new_hash
                        break


                    nonce29=nonce3-close_range_checker
                    text = str(block_number) + transactions + previous_hash + str(nonce29)
                    new_hash = SHA256(text)
                    print('nonce29 is', nonce29)
                    if new_hash.startswith(prefix_str):
                        print('nonce29 is', nonce29)
                        print(f"Yay! Successfully mined bitcoins with nonce value:{nonce29}")
                        found=1
                        return new_hash
                        break '''
