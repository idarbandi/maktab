/*
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
*/

import axios from 'axios';

const state = {
  comments: [],
};

const getters = {
  allMaktabComments: (state) => state.comments, // تغییر نام به شکل اختصاصی
};

const actions = {
  async fetchMaktabComments({ commit }, postId) {
    // دریافت کامنت‌های پست
    const response = await axios.get(`http://127.0.0.1:8000/profile/comments/?post=${postId}`);
    commit('setMaktabComments', response.data);
  },
  async addMaktabComment({ commit }, comment) {
    // افزودن کامنت جدید
    const response = await axios.post('http://127.0.0.1:8000/profile/comments/', comment);
    commit('newMaktabComment', response.data);
  },
  async likeMaktabComment({ commit }, commentId) {
    // لایک کردن کامنت
    await axios.post(`http://127.0.0.1:8000/profile/comments/${commentId}/like/`);
    commit('toggleMaktabLike', commentId);
  },
};

const mutations = {
  setMaktabComments: (state, comments) => (state.comments = comments), // تغییر نام به شکل اختصاصی
  newMaktabComment: (state, comment) => state.comments.unshift(comment), // تغییر نام به شکل اختصاصی
  toggleMaktabLike: (state, commentId) => {
    // تغییر وضعیت لایک کامنت
    const comment = state.comments.find((c) => c.id === commentId);
    if (comment) {
      if (comment.likes.includes(state.user.id)) {
        comment.likes = comment.likes.filter((id) => id !== state.user.id);
      } else {
        comment.likes.push(state.user.id);
      }
    }
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
