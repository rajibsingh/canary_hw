// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';

const routes = [
    { path: '/', name: 'login', component: Login },
    { path: '/home', name: 'home', component: Home }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
