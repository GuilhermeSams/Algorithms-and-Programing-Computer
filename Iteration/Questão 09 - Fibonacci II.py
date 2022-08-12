def fibonacci(N):
    cont_a = 0
    cont_b = 1
    cont = 3
    if N == 1:
        print(cont_a)
    else:
        print(f'{cont_a} {cont_b}', end=" ")
        while cont <= N:
            cont_c = cont_a + cont_b
            print(f'{cont_c}', end=" ")
            cont_a = cont_b
            cont_b = cont_c
            cont += 1


fibonacci(2)
