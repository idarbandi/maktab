// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import LoginForm from '@/LoginForm.vue';
import RegisterForm from '@/RegisterForm.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm, // Updated component name
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterForm, // Updated component name
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
