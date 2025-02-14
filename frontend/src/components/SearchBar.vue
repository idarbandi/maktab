<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-search-bar">
    <input type="text" v-model="query" placeholder="جستجو..." @input="searchMaktab" />
    <div v-if="results.posts.length || results.users.length" class="maktab-results">
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
  name: 'MaktabSearchBar',
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
    async searchMaktab() {
      // جستجو در مطالب و کاربران براساس پرسش کاربر
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
.maktab-search-bar {
  position: relative;
  margin-bottom: 20px;
  /* استایل‌دهی به بخش جستجو */
}

.maktab-search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  /* استایل‌دهی به فیلد ورودی جستجو */
}

.maktab-results {
  position: absolute;
  top: 40px;
  left: 0;
  width: 100%;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* استایل‌دهی به بخش نتایج جستجو */
}

.maktab-results h3 {
  margin: 10px;
  /* استایل‌دهی به تیترهای نتایج */
}

.maktab-results ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  /* استایل‌دهی به لیست نتایج */
}

.maktab-results ul li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  /* استایل‌دهی به هر نتیجه در لیست */
}

.maktab-results ul li:last-child {
  border-bottom: none;
  /* حذف حاشیه پایانی از آخرین نتیجه در لیست */
}

.maktab-results ul li h4 {
  margin: 0;
  /* حذف حاشیه از تگ h4 */
}

.maktab-results ul li p {
  margin: 5px 0;
  /* استایل‌دهی به پاراگراف‌های نتیجه */
}

.maktab-results ul li small {
  color: #888;
  /* استایل‌دهی به اطلاعات اضافی نتایج */
}
</style>
