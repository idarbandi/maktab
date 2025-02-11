import { createStore } from 'vuex';
import apiService, { apiClient } from '@/apiService';
import axios from 'axios';

// Notifications module
const notificationsModule = {
  state: {
    notifications: [],
  },
  getters: {
    allNotifications: (state) => state.notifications,
  },
  actions: {
    async fetchNotifications({ commit }) {
      const response = await axios.get('http://127.0.0.1:8000/profile/notifications/');
      commit('setNotifications', response.data);
    },
  },
  mutations: {
    setNotifications: (state, notifications) => (state.notifications = notifications),
  },
};

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: JSON.parse(localStorage.getItem('user')) || {},
    status: '',
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading';
    },
    auth_success(state, payload) {
      state.status = 'success';
      state.token = payload.token;
      state.user = payload.user;
    },
    auth_error(state) {
      state.status = 'error';
    },
    logout(state) {
      state.status = '';
      state.token = '';
      state.user = {};
    },
  },
  actions: {
    async login({ commit }, user) {
      commit('auth_request');
      console.log('Login action called with user:', user);
      try {
        const response = await apiService.post('/dj-rest-auth/login/', user);
        console.log('Login response:', response);

        const token = response.data.key;
        if (!token) {
          throw new Error('Invalid response format');
        }

        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user)); // Store user info
        apiClient.defaults.headers.common['Authorization'] = `Token ${token}`;
        commit('auth_success', { token, user });
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Login error:', error);
        throw error;
      }
    },
    async register({ commit }, user) {
      commit('auth_request');
      console.log('Register action called with user:', user);
      try {
        const response = await apiService.post('/dj-rest-auth/registration/', user);
        console.log('Registration response:', response);

        if (response.data.key) {
          const token = response.data.key;
          localStorage.setItem('token', token);
          localStorage.setItem('user', JSON.stringify(user)); // Store user info
          apiClient.defaults.headers.common['Authorization'] = `Token ${token}`;
          commit('auth_success', { token, user });
        } else {
          // Assume email confirmation is required
          console.log('Email confirmation required');
          commit('auth_success', { token: null, user });
        }
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Registration error:', error);
        throw error;
      }
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('token');
      localStorage.removeItem('user'); // Remove user info
      delete apiClient.defaults.headers.common['Authorization'];
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    authStatus: (state) => state.status,
    user: (state) => state.user,
  },
  modules: {
    notifications: notificationsModule,
  },
});

export default store;
