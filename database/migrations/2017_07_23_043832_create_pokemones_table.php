<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreatePokemonesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('pokemones', function (Blueprint $table) {
            $table->increments('id');       // id único del registro
            $table->integer('user_id');     // id del dueño
            $table->integer('pokedex_id');  // id en la pokedex
            $table->string('apodo');        // apodo asignado
            $table->string('nombre');       // nombre del pokemón
            $table->integer('nivel');       // nivel actual
            $table->integer('exp');         // exp actual
            $table->timestamps();           // created/updated_at
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('pokemones');
    }
}
