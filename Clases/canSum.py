def canSum(Digito, Valores, Memoria = {}):

    if(Digito in Memoria):
        return Memoria[Digito];
    if(Digito == 0):
        return True;
    if(0 > Digito):
        return False;

    for i in Valores:

        Restante = Digito - i;
        if(canSum(Restante, Valores, Memoria)):
            Memoria[Digito] = True;
            return True;

    Memoria[Digito] = False;
    return False;

print(canSum(7, [4, 3]));
print(canSum(300, [7, 14]));
