<!-- src/components/Login.vue -->
<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="input-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // Import useRouter to handle navigation

const email = ref('');
const password = ref('');
const router = useRouter(); // Initialize the router instance

const handleLogin = async () => {
  try {
    // Send a POST request to the backend service
    const response = await axios.post('http://127.0.0.1:8000/gh_connect/login/', {
      email: email.value,
      password: password.value,
    });

    alert('Login successful!');
    // If login is successful, navigate to the desired route
    console.log('Login successful:', response.data);
    router.push('/home');
    // router.replace('/home');
    // $router.push({ name: 'home' })
  } catch (error) {

    console.error('Login failed:', error);
    alert('Login failed. Please check your credentials.');
  }
};
</script>

<style scoped>
.login-container {
  width: 300px;
  padding: 2rem;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h2 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.input-group {
  margin-bottom: 1rem;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

button {
  width: 100%;
  padding: 0.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: #369f75;
}
</style>
