<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-home-container">
    <SearchBar />
    <MaktabFilterSort />
    <h2>لیست مطالب</h2>
    <ul>
      <li v-for="post in maktabPosts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <small>{{ post.created_at }}</small>
      </li>
    </ul>
    <MaktabLogoutButton v-if="isAuthenticated" />
    <div v-if="isAuthenticated">
      <p>خوش آمدید، {{ user?.username || 'کاربر عزیز' }}</p>
    </div>
    <div v-else>
      <p>شما وارد نشده‌اید. لطفاً وارد شوید.</p>
      <router-link to="/login">ورود</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import apiService from '@/apiService';
import SearchBar from '@/components/SearchBar.vue';
import MaktabFilterSort from '@/components/FilterSort.vue';
import MaktabLogoutButton from './LogoutButton.vue';

export default {
  name: 'MaktabHomePage',
  components: {
    MaktabLogoutButton,
    SearchBar,
    MaktabFilterSort,
  },
  data() {
    return {
      maktabPosts: [],
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'user']),
  },
  async created() {
    // دریافت مطالب و به‌روزرسانی لیست پست‌ها هنگام ساخت کامپوننت
    try {
      const response = await apiService.get('/profiles/dashboard/');
      this.maktabPosts = response.data.recent_posts;
      console.log('maktabPosts', response);
    } catch (error) {
      console.error('Failed to fetch posts:', error);
    }
  },
};
</script>

<style scoped>
.maktab-home-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: right;
  /* استایل‌دهی به بخش اصلی صفحه اصلی */
}

h2 {
  margin-bottom: 20px;
  /* استایل‌دهی به تیتر ها */
}

ul {
  list-style-type: none;
  padding: 0;
  /* استایل‌دهی به لیست پست‌ها */
}

li {
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 5px;
  /* استایل‌دهی به هر پست در لیست */
}

h3 {
  margin: 0;
  /* حذف حاشیه از تگ h3 */
}

small {
  color: #888;
  /* استایل‌دهی به تاریخ ایجاد و جزئیات پست‌ها */
}

p {
  margin: 10px 0;
  /* استایل‌دهی به پاراگراف‌ها */
}

.error-message {
  color: red;
  text-align: center;
  /* استایل‌دهی به پیام خطا */
}
</style>
