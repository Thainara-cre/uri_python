linha1 = input().split(" ")

lanche, quantidade = linha1

if int(lanche)==1:
    print('Total: R$ {:.2f}'.format(int(quantidade) * 4))
elif int(lanche)==2:
    print('Total: R$ {:.2f}'.format(int(quantidade) * 4.5))
elif int(lanche)==3:
    print('Total: R$ {:.2f}'.format(int(quantidade) * 5))
elif int(lanche)==4:
    print('Total: R$ {:.2f}'.format(int(quantidade) * 2))
elif int(lanche)==5:
    print('Total: R$ {:.2f}'.format(int(quantidade) * 1.5))