// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/Home.vue';
import Login from '../components/Login.vue';

const routes = [
    { path: '/', name: 'login', component: Login },
    { path: '/home', name: 'home', component: HomePage }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
