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

// Define a reactive array to store repositories
const repositories = ref([]);

// Fetch the GitHub repositories using the access token
const fetchRepositories = async (accessToken) => {
  Console.log("*** accessToken: " + accessToken);
  try {
    // Fetch the user's repositories from GitHub using the access token
    const response = await axios.get('https://api.github.com/user/repos', {
      headers: {
        Authorization: `token ${accessToken}`, // Include the access token in the request header
      },
    });

    // Store the fetched repositories in the reactive array
    repositories.value = response.data;
  } catch (error) {
    console.error('Failed to fetch repositories:', error);
    alert('An error occurred while fetching your repositories.');
  }
};

// Simulate fetching the access token from the backend or session storage
onMounted(() => {
  // Replace this with the actual token retrieval logic
  const accessToken = sessionStorage.getItem('github_access_token') || 'your_access_token_here';

  if (accessToken) {
    fetchRepositories(accessToken);
  } else {
    console.error('Access token is missing.');
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
