<template>
  <nav>
    <router-link to="/login">Login</router-link> |
    <router-link to="/registrar">Registrar</router-link>
  </nav>
  
  <router-view/>
</template>


<script setup lang="ts">
import { onMounted } from 'vue';
import router from './router';

  onMounted(async ()=>{      
    router.push({path : '/login'})  
  })
  
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

form{
  
}
</style>
