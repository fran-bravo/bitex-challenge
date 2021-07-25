<template>
  <div id="app">
    <BitexClient msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import BitexClient from './components/BitexClient.vue'

export default {
  name: 'App',
  components: {
    BitexClient
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
