// store/index.js
import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: {},
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
      console.log('Login action called with user:', user); // Debugging log
      try {
        const response = await axios.post('http://127.0.0.1:8000/dj-rest-auth/login/', user); // Updated URL
        console.log('Login response:', response); // Debugging log
        const token = response.data.key;
        const userData = response.data.user;
        localStorage.setItem('token', token);
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        commit('auth_success', { token, user: userData });
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Login error:', error); // Debugging log
        throw error;
      }
    },
    async register({ commit }, user) {
      commit('auth_request');
      console.log('Register action called with user:', user); // Debugging log
      try {
        const response = await axios.post('http://127.0.0.1:8000/dj-rest-auth/registration/', user); // Updated URL
        console.log('Registration response:', response); // Debugging log
        const token = response.data.key;
        const userData = response.data.user;
        localStorage.setItem('token', token);
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        commit('auth_success', { token, user: userData });
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Registration error:', error); // Debugging log
        throw error;
      }
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('token');
      delete axios.defaults.headers.common['Authorization'];
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    authStatus: (state) => state.status,
    user: (state) => state.user,
  },
});

export default store;
