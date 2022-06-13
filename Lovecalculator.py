ur_name= input("enter your first name: ")

partner= input("enter your partner's first name: ")

c=1
counter=1
combined_name= ur_name +partner

for i in combined_name:
	if(i=='a' or i=='e' or i=='i' or i== 'o' or i=='u'):
		c=c+1
	counter=counter+1

if (c>=5):
	
	print("you're made for each other")
else:
	print("It's okay to be together if you love each other, you can ignore the calculations that way...")

love_percentage= (counter/20)*100
print('love percentage calculated is:', love_percentage)

''' 
######################### this is reversion
            def reverse(n):
                d=0
                rev=0
                while(n>0):
                    d=n%10
                    n=n/10
                    rev=rev*10+d
                return rev 
        
            reversion= reverse(nonce)

            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay!reversion Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break








            reversion= reverse(nonce2)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! reversion Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce3)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay!reversion Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce4)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay!reversion Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break

        reversion= reverse(nonce5)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce6)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce7)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce8)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce9)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce10)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce11)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce12)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce13)
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break
            reversion= reverse(nonce14) 
            text = str(block_number) + transactions + previous_hash + str(reversion)
            new_hash = SHA256(text)
            if new_hash.startswith(prefix_str):
                print('nonce is', reversion)
                print(f"Yay! Successfully mined bitcoins with nonce value:{reversion}")
                found=1
                return new_hash
                
                break    '''