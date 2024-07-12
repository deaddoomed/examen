<template>
   <div>
      <form @submit.prevent="registrar">
          <label for="usuario">Usuario: </label>
          <input type="text" id="usuario" v-model="datos_usuario.nombre" />

          <label for="contrasena">Contrasena: </label>
          <input type="password" id="contrasena" v-model="datos_usuario.contrasena" />

          <label for="email">Email: </label>
          <input type="text" id="email" v-model="datos_usuario.email" />
          <br>

          <button type="submit">Registrar</button>
          <br>
                    
          <p style="text-align: center;">{{mensaje}}</p>
      </form>
  </div>
</template>


<script setup lang="ts">
import router from '@/router';
import { ref } from 'vue';

const datos_usuario = ref({nombre:"", contrasena: "", email: ""})
const mensaje = ref("")

async function registrar(){    
      if(datos_usuario.value.contrasena.length == 0 || datos_usuario.value.nombre.length == 0 || datos_usuario.value.email.length == 0){
          mensaje.value = 'Usuario o Contrasena vacio';
      }
      else{
        var solicitud = await fetch("http://127.0.0.1:4000/login/crear", {
              method: 'POST',
              headers: {'Content-Type': 'application/json',},
              body: JSON.stringify({nombre: datos_usuario.value.nombre, 
                                    contrasena: datos_usuario.value.contrasena,
                                    email: datos_usuario.value.email}),
              })
        var respuesta = await solicitud.json();

        if(respuesta){
          mensaje.value = respuesta
          if(confirm(mensaje.value)){
            router.push({path : '/login'})
          }
          else{
            router.push({path : '/login'})
          }
        }

        console.log(respuesta)
      }        
  }
</script>
