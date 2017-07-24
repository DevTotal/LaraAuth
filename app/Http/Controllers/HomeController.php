<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use App\Pokemon;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    public function user(Request $request)
    {
        return $request->user();
    }

    public function user_pokemones(Request $request)
    {
        return $request->user()->pokemones;
    }

    public function user_pokemones_agregar(Request $request)
    {
        return $request->user()->pokemones()->create($request->all());
    }

    public function user_buscar(Request $request)
    {
        return ($r = User::find($request->user_id)) == NULL ? "Error: ID no encontrado" : $r;
    }

    public function pokemon_buscar(Request $request)
    {
        return ($r = Pokemon::find($request->pokemon_id)) == NULL ? "Error: ID no encontrado" : $r;
    }
}
