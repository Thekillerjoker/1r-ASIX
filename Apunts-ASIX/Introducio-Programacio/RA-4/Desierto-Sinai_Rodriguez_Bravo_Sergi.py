Cassos = int(input('Introdueix el numero de casos:' ))
for x in range(Cassos):
    k = int(input('Introdueix el numero de linies:' ))
    vots = {}
    for i in range(k):
        mapa = input('Introdueix el nom del mapa:' )
        vots[mapa] = vots.get(mapa, 0) + 1
    max_vots = 0
    mapa_guanyador = ""
    for mapa, vots_del_mapa in vots.items():
        if vots_del_mapa > max_vots:
            max_vots = vots_del_mapa
            mapa_guanyador = mapa
    print(mapa_guanyador)