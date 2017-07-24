<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Pokemon extends Model
{
    protected $table = 'pokemones';
    protected $fillable = ['pokedex_id', 'apodo', 'nombre', 'nivel', 'exp'];

    public function user()
    {
    	return $this->belongsTo('App\User');
    }
}
