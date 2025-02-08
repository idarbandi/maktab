<template>
  <div id="home-page">
    <header>
      <div class="logo">
        <img src="logo.png" alt="پروژه مکتب" />
      </div>
      <nav>
        <ul>
          <li><router-link to="/">خانه</router-link></li>
          <li><router-link to="/about">درباره ما</router-link></li>
          <li><router-link to="/resources">منابع آموزشی</router-link></li>
          <li><router-link to="/contact">تماس با ما</router-link></li>
        </ul>
      </nav>
      <div class="auth-buttons">
        <span v-if="isAuthenticated">
          خوش آمدید, {{ user.username }}!
          <button @click="logout" class="logout-button">خروج</button>
        </span>
        <router-link v-else to="/login" class="login-button">ورود</router-link>
      </div>
    </header>
    <main>
      <section class="hero">
        <h1>به مکتب خوش آمدید</h1>
        <p>جامع‌ترین منابع آموزشی برای همه</p>
        <button class="cta-button">شروع کنید</button>
      </section>
      <section class="posts">
        <h2>آخرین مطالب</h2>
        <div class="post-grid">
          <div v-for="post in posts" :key="post.id" class="post-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.content }}</p>
          </div>
        </div>
        <div class="pagination">
          <button @click="fetchPosts(page - 1)" :disabled="page === 1">قبلی</button>
          <span>صفحه {{ page }} از {{ totalPages }}</span>
          <button @click="fetchPosts(page + 1)" :disabled="page === totalPages">بعدی</button>
        </div>
      </section>
    </main>
    <footer>
      <p>حق نشر © 2025. تمامی حقوق محفوظ است.</p>
    </footer>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import apiService from '@/apiService';

export default {
  name: 'HomePage',
  data() {
    return {
      posts: [],
      page: 1,
      totalPages: 1
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'user'])
  },
  created() {
    this.fetchPosts(this.page);
    console.log('Component created, fetching posts...'); // Debugging log
  },
  methods: {
    ...mapActions(['logout']),
    async fetchPosts(page) {
      try {
        const response = await apiService.getPosts(page);
        this.posts = response.data.results;
        this.page = page;
        this.totalPages = Math.ceil(response.data.count / 10);
        console.log('Posts fetched:', this.posts); // Debugging log
      } catch (error) {
        console.error('Failed to fetch posts:', error); // Debugging log
      }
    },
    logout() {
      console.log('Logging out'); // Debugging log
      this.logout(); // Dispatch the logout action from Vuex
      this.$router.push('/login'); // Redirect to the login page
    }
  }
};
</script>

<style scoped>
#home-page {
  font-family: 'Iran Sans', Tahoma, sans-serif;
  direction: rtl;
  background-color: #f9f9f9;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #004d40;
  padding: 10px 20px;
  color: white;
}

header .logo img {
  height: 50px;
}

nav ul {
  list-style-type: none;
  display: flex;
  gap: 20px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s;
}

nav ul li a:hover {
  color: #b2dfdb;
}

.auth-buttons {
  display: flex;
  align-items: center;
}

main {
  padding: 20px;
}

.hero {
  text-align: center;
  background-color: #e0f7fa;
  padding: 60px 20px;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.hero h1 {
  font-size: 40px;
  margin-bottom: 10px;
}

.hero p {
  font-size: 22px;
  margin-bottom: 20px;
}

.hero .cta-button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 18px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s, transform 0.3s;
}

.hero .cta-button:hover {
  background-color: #00796b;
  transform: translateY(-2px);
}

.posts {
  text-align: center;
}

.posts h2 {
  font-size: 28px;
  margin-bottom: 20px;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.post-card {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.pagination {
  margin-top: 20px;
}

.pagination button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 10px 15px;
  margin: 0 5px;
  cursor: pointer;
  border-radius: 5px;
}

.pagination button:hover {
  background-color: #00796b;
}

.pagination span {
  font-size: 16px;
}

footer {
  background-color: #004d40;
  color: white;
  text-align: center;
  padding: 10px 0;
  margin-top: 40px;
}
</style>
