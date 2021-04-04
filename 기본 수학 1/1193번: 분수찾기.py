num = int(input())
if num==1:
    print('1/1')
else:
    i = 1
    acc = 0
    while True:
        acc += i
        if num >= acc and num <= acc+i+1:
            if i%2 == 0:
                print(str(acc+(i+1)+1-num)+'/'+str(num-acc))
            else:
                print(str(str(num-acc)+'/'+str(acc+(i+1)+1-num)))
            break
        i += 1
