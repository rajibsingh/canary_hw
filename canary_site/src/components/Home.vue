<!-- src/components/Home.vue -->
<template>
  <div class="home-container">
    <h1>Welcome to Your GitHub Repositories</h1>
    <ul v-if="repositories.length">
      <li v-for="repo in repositories" :key="repo.id">
        <a :href="repo.html_url" target="_blank">{{ repo.name }}</a>
      </li>
    </ul>
    <p v-else>Loading your repositories...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const repositories = ref([]);

// Function to fetch GitHub repositories using the access token
const fetchRepositories = async (accessToken) => {
  try {
    const response = await axios.get('https://api.github.com/user/repos', {
      headers: {
        Authorization: `token ${accessToken}`, // Use the token correctly
      },
    });
    repositories.value = response.data;
  } catch (error) {
    console.error('Failed to fetch repositories:', error);
    alert('An error occurred while fetching your repositories.');
  }
};

// Retrieve the access token from the URL parameters
const getAccessTokenFromUrl = () => {
  const params = new URLSearchParams(window.location.search);
  return params.get('token');
};

// Fetch repositories on component mount
onMounted(() => {
  const accessToken = getAccessTokenFromUrl();

  if (accessToken) {
    fetchRepositories(accessToken);
  } else {
    console.error('Access token is missing.');
    alert('Access token is missing. Please log in again.');
  }
});
</script>

<style scoped>
.home-container {
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}

a {
  color: #0366d6;
  text-decoration: none;
  font-weight: bold;
}

a:hover {
  text-decoration: underline;
}
</style>
