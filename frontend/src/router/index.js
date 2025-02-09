// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import LoginForm from '@/LoginForm.vue';
import RegisterForm from '@/RegisterForm.vue';
import dashboardPage from '@/components/dashboardPage.vue';
import store from '@/store'; // Import the store

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
    path: '/about',
    name: 'About',
    component: () => import('@/components/AboutPage.vue'), // Lazy-loaded route
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: dashboardPage,
    beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next();
      } else {
        next('/login');
      }
    },
  },
  // {
  //   path: '/contact',
  //   name: 'Contact',
  //   component: () => import('@/components/Contact.vue'), // Lazy-loaded route
  // },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard to protect routes
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register'];
  const authRequired = !publicPages.includes(to.path);
  const isLoggedIn = store.getters.isAuthenticated;

  if (authRequired && !isLoggedIn) {
    return next('/login');
  }

  next();
});

export default router;
