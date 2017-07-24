<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/


Route::middleware('auth:api')->group(function () {
	
	// Devuelve los datos del usuario autentificado 
	// Parámetros: Ninguno
	Route::post('/user', 'HomeController@user');

	// Devuelve los pokemones del usuario autentificado 
	// Parámetros: Ninguno
	Route::post('/user/pokemones', 'HomeController@user_pokemones');

	// Agrega un Pokémon a los pokemones del usuario autentificado
	// Parámetros: 	pokedex_id => ID Pokedex del pokémon
	//	  	apodo => Apodo del Pokémon
	//		nombre => Nombre original del Pokémon
	//		nivel => Nivel del Pokémon 
	//		exp => Experiencia del Pokémon 
	Route::post('/user/pokemones/agregar', 'HomeController@user_pokemones_agregar');
	
	// Devuelve los datos del ID buscado y un error al no encontrarlo
	// Parámetros: user_id => Id del usuario buscado
	Route::post('/user/buscar', 'HomeController@user_buscar');

	// Devuelve los datos pokemon del ID buscado y un error al no encontrarlo
	// Parámetros: pokemon_id => Id del pokemon buscado
	Route::post('/pokemon/buscar', 'HomeController@pokemon_buscar');
});