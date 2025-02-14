/*
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
*/

import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import LoginForm from '@/LoginForm.vue';
import RegisterForm from '@/RegisterForm.vue';
import MaktabDashboardPage from '@/components/dashboardPage.vue';
import store from '@/store'; // Import the store
import PasswordReset from '@/components/PasswordReset.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm,
    beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next('/');
      } else {
        next();
      }
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterForm,
  },
  {
    path: '/password-reset',
    name: 'PasswordReset',
    component: PasswordReset,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/components/AboutPage.vue'), // Lazy-loaded route
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: MaktabDashboardPage,
    beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next();
      } else {
        next('/login');
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard to protect routes
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register', '/password-reset'];
  const authRequired = !publicPages.includes(to.path);
  const isLoggedIn = store.getters.isAuthenticated;

  if (authRequired && !isLoggedIn) {
    return next('/login');
  }

  next();
});

export default router;
