<template>
  <div class="home-container">
    <SearchBar />
    <FilterSort />
    <h2>لیست مطالب</h2>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <small>{{ post.created_at }}</small>
      </li>
    </ul>
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
import FilterSort from '@/components/FilterSort.vue';

export default {
  name: 'HomePage',
  components: {
    SearchBar,
    FilterSort,
  },
  data() {
    return {
      posts: [],
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'user']),
  },
  async created() {
    try {
      const response = await apiService.get('/profile/dashboard/');
      this.posts = response.data.recent_posts;
    } catch (error) {
      console.error('Failed to fetch posts:', error);
    }
  },
};
</script>

<style scoped>
.home-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: right;
}

h2 {
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 5px;
}

h3 {
  margin: 0;
}

small {
  color: #888;
}

p {
  margin: 10px 0;
}

.error-message {
  color: red;
  text-align: center;
}
</style>
