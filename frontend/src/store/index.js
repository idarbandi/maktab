// store/index.js
import { createStore } from 'vuex';
import apiService, { apiClient } from '@/apiService';

const user = localStorage.getItem('user');
const parsedUser = user ? JSON.parse(user) : {};

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: parsedUser,
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
      try {
        const response = await apiService.post('/dj-rest-auth/login/', {
          email: user.email,
          password: user.password,
        });

        const token = response.data.key;
        const userInfo = response.data.user; // Update with correct user data path

        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(userInfo));
        apiClient.defaults.headers.common['Authorization'] = `Token ${token}`;

        commit('auth_success', { token, user: userInfo });
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Login error:', error);
        throw error;
      }
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      delete apiClient.defaults.headers.common['Authorization'];
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    authStatus: (state) => state.status,
    user: (state) => state.user,
  },
});

export default store;
