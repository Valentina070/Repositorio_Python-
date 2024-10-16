
from model.restaurante import Restaurante
from model.menu import Menu
from model.cliente import Cliente

def main():
    print("       Código:7502410013 ")
    print("  Estudiante:Valentina Zuñiga Vasquez ")
    print("**************************************")

    restaurante = Restaurante("Emily's", "Comida italiana", 50, "Centro histórico de Cartagena", "300452817")
    menu = Menu("Delicias de italia", "plato fuerte", 20.2)
    cliente = Cliente("Daniela Zuñiga", "Pastas", "20", "3202235876")

    print("\nInformación del restaurante:")
    restaurante.mostrar_datos()
    print("\nInformación del menú:")
    menu.mostrar_datos()
    print("\nInformación del cliente:")
    cliente.mostrar_datos()

if __name__ == "__main__":
    main()
