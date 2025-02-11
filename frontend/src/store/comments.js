// store/comments.js
import axios from 'axios';

const state = {
  comments: [],
};

const getters = {
  allComments: state => state.comments,
};

const actions = {
  async fetchComments({ commit }, postId) {
    const response = await axios.get(`http://127.0.0.1:8000/profile/comments/?post=${postId}`);
    commit('setComments', response.data);
  },
  async addComment({ commit }, comment) {
    const response = await axios.post('http://127.0.0.1:8000/profile/comments/', comment);
    commit('newComment', response.data);
  },
  async likeComment({ commit }, commentId) {
    await axios.post(`http://127.0.0.1:8000/profile/comments/${commentId}/like/`);
    commit('toggleLike', commentId);
  },
};

const mutations = {
  setComments: (state, comments) => (state.comments = comments),
  newComment: (state, comment) => state.comments.unshift(comment),
  toggleLike: (state, commentId) => {
    const comment = state.comments.find(c => c.id === commentId);
    if (comment) {
      if (comment.likes.includes(state.user.id)) {
        comment.likes = comment.likes.filter(id => id !== state.user.id);
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
