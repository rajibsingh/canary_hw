<!-- src/App.vue -->
<template>
  <div id="app">
    <Login />
  </div>
</template>

<script setup>
import Login from './components/Login.vue';
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
  margin: 0;
}
</style>
