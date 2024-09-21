<!-- src/components/Home.vue -->
<template>
  <div class="home-container">
    <h1>Welcome to the Home Page</h1>
    <p>This is the home page of your application. You can customize this content as needed.</p>
  </div>
</template>

<script setup>
// Currently, no specific setup or script is required for this blank page.
// You can add your logic here if needed in the future.
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  padding: 20px;
  background-color: #f5f5f5;
}

h1 {
  margin-bottom: 1rem;
  font-size: 2rem;
  color: #333;
}

p {
  font-size: 1.2rem;
  color: #555;
}
</style>
