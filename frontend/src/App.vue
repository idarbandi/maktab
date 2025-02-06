<template>
  <div id="app">
    <nav>
      <router-link to="/">صفحه اصلی</router-link>
      <router-link to="/about">درباره ما</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
#app {
  text-align: center;
  font-family: 'Tahoma', sans-serif;
  direction: rtl;
  padding: 20px;
}

nav {
  background-color: #f8f9fa;
  padding: 10px;
}

nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #42b983;
  font-size: 18px;
}

nav a.router-link-exact-active {
  font-weight: bold;
  color: #2c3e50;
}
</style>
