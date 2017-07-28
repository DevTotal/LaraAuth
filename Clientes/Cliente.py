import requests
import json

token = ""
refresh_token = ""
client_id = 2
client_secret = "h08zl23nLtqSZxpJ9vnP7CdHTFWqCUgxX9gcMKWZ"

def ObtenerToken(user, password):
	global token
	global refresh_token

	url = 'http://localhost/oauth/token'
	payload = {"grant_type":"password","client_id":client_id,"client_secret":client_secret,"username":user,"password":password,"scope":"*"}
	r = requests.post(url, data=payload)
	d = json.loads(r.text)

	token = d['access_token']
	refresh_token = d['refresh_token']

def MiCuenta():
	if token == "":
		print("Consigue un Token de Acceso antes de usar esta opción")
		return

	url = 'http://localhost/api/user'
	r = requests.post(url, headers={"Authorization":"Bearer "+token})
	print(r.text)

def CrearPokemon(id_pokedex, apodo, nombre, nivel, exp):

	if token == "":
		print("Consigue un Token de Acceso antes de usar esta opción")
		return

	url = 'http://localhost/api/user/pokemones/agregar'
	payload = {"pokedex_id":id_pokedex,"apodo":apodo,"nombre":nombre,"nivel":nivel,"exp":exp}
	r = requests.post(url, data=payload, headers={"Authorization":"Bearer "+token})
	print(r.text)

def MisPokemones():
	if token == "":
		print("Consigue un Token de Acceso antes de usar esta opción")
		return

	url = 'http://localhost/api/user/pokemones'
	r = requests.post(url, headers={"Authorization":"Bearer "+token})
	print(r.text)

def BuscarUsuario(user_id):

	if token == "":
		print("Consigue un Token de Acceso antes de usar esta opción")
		return

	url = 'http://localhost/api/user/buscar'
	payload = {"user_id":user_id}
	r = requests.post(url, data=payload, headers={"Authorization":"Bearer "+token})
	print(r.text)

def BuscarPokemon(pokemon_id):

	if token == "":
		print("Consigue un Token de Acceso antes de usar esta opción")
		return

	url = 'http://localhost/api/pokemon/buscar'
	payload = {"pokemon_id":pokemon_id}
	r = requests.post(url, data=payload, headers={"Authorization":"Bearer "+token})
	print(r.text)

def RefrescarToken():
	global token
	global refresh_token
	
	url = 'http://localhost/oauth/token'
	payload = {"grant_type":"refresh_token","client_id":client_id,"client_secret":client_secret,"refresh_token":refresh_token,"scope":"*"}
	r = requests.post(url, data=payload)
	d = json.loads(r.text)

	token = d['access_token']
	refresh_token = d['refresh_token']


def menu(opcion):

	if opcion == "1":
		ObtenerToken(input("Ingresar Usuario: "), input("Ingresar Contraseña: "))
	elif opcion == "2":
		MiCuenta()
	elif opcion == "3":
		CrearPokemon(input("ID Pokedex: "), input("Apodo: "), input("Nombre: "), input("Nivel: "), input("Exp: "))
	elif opcion == "4":
		MisPokemones()
	elif opcion == "5":
		BuscarUsuario(input("Ingresar ID: "))
	elif opcion == "6":
		BuscarPokemon(input("Ingresar ID:"))
	elif opcion == "7":
		RefrescarToken()
	elif opcion == "8":
		print("Tutorial Creado por Gonzalo de DevTotal.Cl para Facebook Developer Circles")
		return 0

	print("Escoga una Opción:")

	print("1. Obtener un Token")
	print("2. Datos de mi Cuenta")
	print("3. Crear un Pokémon")
	print("4. Consultar mis Pokémons")
	print("5. Buscar un Usuario por su ID")
	print("6. Buscar un Pokémon por su ID")
	print("7. Refrescar Token")
	print("8. Salir")

	return menu(input("\n"))

menu(0)