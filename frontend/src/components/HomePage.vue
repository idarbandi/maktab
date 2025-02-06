<template>
  <div id="home">
    <header>
      <h1>صفحه اصلی</h1>
    </header>
    <main>
      <p>به صفحه اصلی پروژه مکتب خوش آمدید!</p>
    </main>
    <footer>
      <p>حق نشر © 2025. تمامی حقوق محفوظ است.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
#home {
  text-align: center;
  font-family: 'Tahoma', sans-serif;
  direction: rtl;
  padding: 20px;
}

header h1 {
  color: #2c3e50;
}

main {
  margin-top: 20px;
  font-size: 18px;
}

footer {
  margin-top: 40px;
  color: #555;
}
</style>
