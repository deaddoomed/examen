<template>
  <div>
      <form @submit.prevent="login">
          <label for="usuario">Usuario: </label>
          <input type="text" id="usuario" v-model="datos_usuario.usuario" />

          <label for="contrasena">Contrasena: </label>
          <input type="password" id="contrasena" v-model="datos_usuario.contrasena" />

          <button type="submit">Login</button>
                    
          <p style="text-align: center;">{{mensaje}}</p>
      </form>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';

  const datos_usuario = ref({usuario:"", contrasena: ""})
  const mensaje = ref("")

  async function login(){    
        if(datos_usuario.value.contrasena.length == 0 || datos_usuario.value.usuario.length == 0){
            mensaje.value = 'Usuario o Contrasena vacio';
        }
        else{
          var solicitud = await fetch("http://127.0.0.1:4000/login", {
                method: 'POST',
                headers: {'Content-Type': 'application/json',},
                body: JSON.stringify({usuario: datos_usuario.value.usuario, contrasena: datos_usuario.value.contrasena}),
                })
          var respuesta = await solicitud.json();

          if(respuesta.detail){
            mensaje.value = respuesta.detail
          }
          console.log(respuesta)
        }        
    }


</script>
