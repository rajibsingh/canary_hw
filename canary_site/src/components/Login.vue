<!-- src/components/Login.vue -->
<template>
  <div class="overlay">
    <div class="login-container">
      <h2>Redirecting to GitHub for Authentication...</h2>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(async () => {
  try {
    // Immediately forward the user to GitHub OAuth endpoint by calling the backend
    const response = await axios.get('http://127.0.0.1:8000/gh_connect/login/');
    if (response.status === 200) {
      // The backend should handle the redirect to GitHub OAuth
      console.log('Redirecting to GitHub OAuth...');
    }
  } catch (error) {
    console.error('Failed to redirect to GitHub OAuth:', error);
    alert('An error occurred while trying to authenticate with GitHub.');
    // Optionally redirect to a fallback or error page
    router.push('/');
  }
});
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7); /* Gray overlay with transparency */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* High z-index to ensure it overlays other content */
}

.login-container {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 10px;
  text-align: center;
  color: #333;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h2 {
  margin: 0;
  font-size: 1.5rem;
}
</style>
