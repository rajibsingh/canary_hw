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

// Access the GitHub client ID from environment variables
const clientId = import.meta.env.VITE_GITHUB_CLIENT_ID;
console.log('*** clientId', clientId);
// const redirectUri = 'http://127.0.0.1:8000/gh_connect/callback/'; // Your registered redirect URI
const redirectUri = 'http://127.0.0.1:5173/home'; // Your registered redirect URI
const scope = 'user'; // Adjust scope as needed

onMounted(() => {
  // Construct the full GitHub OAuth URL
  const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}&scope=${scope}`;

  // Redirect the user directly to GitHub's OAuth page
  window.location.href = githubAuthUrl;
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
