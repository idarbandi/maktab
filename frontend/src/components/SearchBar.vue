<!-- SearchBar.vue -->
<template>
    <div class="search-bar">
      <input type="text" v-model="query" placeholder="جستجو..." @input="search" />
      <div v-if="results.posts.length || results.users.length" class="results">
        <div v-if="results.posts.length">
          <h3>مطالب</h3>
          <ul>
            <li v-for="post in results.posts" :key="post.id">
              <h4>{{ post.title }}</h4>
              <p>{{ post.content }}</p>
            </li>
          </ul>
        </div>
        <div v-if="results.users.length">
          <h3>کاربران</h3>
          <ul>
            <li v-for="user in results.users" :key="user.id">
              <p>{{ user.username }}</p>
              <small>{{ user.email }}</small>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import apiService from '@/apiService';
  
  export default {
    name: 'SearchBar',
    data() {
      return {
        query: '',
        results: {
          posts: [],
          users: [],
        },
      };
    },
    methods: {
      async search() {
        if (this.query.trim() === '') {
          this.results = { posts: [], users: [] };
          return;
        }
        try {
          const response = await apiService.get(`/search/?q=${this.query}`);
          this.results = response.data;
        } catch (error) {
          console.error('Search error:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .search-bar {
    position: relative;
    margin-bottom: 20px;
  }
  
  .search-bar input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .results {
    position: absolute;
    top: 40px;
    left: 0;
    width: 100%;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .results h3 {
    margin: 10px;
  }
  
  .results ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  .results ul li {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .results ul li:last-child {
    border-bottom: none;
  }
  
  .results ul li h4 {
    margin: 0;
  }
  
  .results ul li p {
    margin: 5px 0;
  }
  
  .results ul li small {
    color: #888;
  }
  </style>
  