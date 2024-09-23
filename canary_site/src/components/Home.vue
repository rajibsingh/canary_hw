<!-- src/components/Home.vue -->
<template>
  <div class="home-container">
    <h1>Welcome to Your GitHub Repositories</h1>
    <ul v-if="repositories.length">
      <li v-for="repo in repositories" :key="repo.id">
        <label>
          <input
              type="checkbox"
              :checked="repo.id === selectedRepoId"
              @change="selectRepository(repo)"
          />
          <a :href="repo.html_url" target="_blank">{{ repo.name }}</a>
        </label>
      </li>
    </ul>
    <p v-else>Loading your repositories...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const repositories = ref([]); // Store the list of repositories
const selectedRepoId = ref(null); // Store the ID of the currently selected repository
let accessToken = ''; // Store the access token globally

// Function to fetch the GitHub repositories using the access token
const fetchRepositories = async (accessToken) => {
  try {
    const response = await axios.get('https://api.github.com/user/repos', {
      headers: {
        Authorization: `token ${accessToken}`, // Use the access token to authenticate the request
      },
    });
    repositories.value = response.data; // Set the fetched repositories
  } catch (error) {
    console.error('Failed to fetch repositories:', error);
    alert('An error occurred while fetching your repositories.');
  }
};

// Function to fetch the previously selected repository from the backend
const fetchSelectedRepository = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/gh_connect/get-selected-repository/', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        'X-CSRFToken': getCSRFToken()
      },
    });

    const selectedRepo = response.data.selected_repo;
    if (selectedRepo) {
      // Find the matching repository from the list and set it as selected
      const matchingRepo = repositories.value.find(repo => repo.id === selectedRepo.id);
      if (matchingRepo) {
        selectedRepoId.value = matchingRepo.id;
      }
    }
  } catch (error) {
    console.error('Failed to fetch the previously selected repository:', error);
  }
};

// Function to retrieve the access token from the URL parameters
const getAccessTokenFromUrl = () => {
  const params = new URLSearchParams(window.location.search);
  return params.get('token');
};

// Function to handle repository selection
const selectRepository = async (repo) => {
  // Set the selected repository ID
  selectedRepoId.value = repo.id;

  // Save the selected repository to the backend
  try {
    // const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const response = await axios.post('http://127.0.0.1:8000/gh_connect/save-repository/', {
      selected_repo: {
        name: repo.name,
        url: repo.html_url,
        description: repo.description,
        id: repo.id,
      },
    }, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        'X-CSRFToken': getCSRFToken()
      },
    });

    alert(response.data.message);
  } catch (error) {
    console.error('Error saving repository:', error);
    alert('Failed to save the repository.');
  }
};

// Fetch repositories on component mount
onMounted(() => {
  accessToken = getAccessTokenFromUrl();

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
  display: flex;
  align-items: center;
}

a {
  color: #0366d6;
  text-decoration: none;
  font-weight: bold;
  margin-left: 8px;
}

a:hover {
  text-decoration: underline;
}
</style>
