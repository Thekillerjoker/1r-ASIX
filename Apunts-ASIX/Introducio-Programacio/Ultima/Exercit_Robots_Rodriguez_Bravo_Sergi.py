def dibuixarPeus():
   print("      __   __")
   print("     |  | |  |")
   print("      --   --")


def dibuixarCames():
   print("     |   _   |")
   print("     |  | |  |")
   print("     |  | |  |")


def dibuixarCos():
   print("   -------------")
   print("  / /|       |\\ \\")
   print(" / / |       | \\ \\")
   print("( )  |       |  ( )")
   print("     ---------")


def dibuixarColl():
   print("        ||")


def dibuixarCap():
   print("       ____")
   print("      (o  o)")
   print("       ----")

def socunrobot():
    print("              +-----------------+")
    print("              |  Sóc un Robot   |")
    print("              +-----------------+")
    print("                   /")
    print("                  /")
    print("                 /")
def dibuixarRobot(i):
    socunrobot()
    dibuixarCap()
    dibuixarColl()
    dibuixarCos()
    dibuixarCames()
    dibuixarPeus()

for i in range(1, 1001):
    dibuixarRobot(i)