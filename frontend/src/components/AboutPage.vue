<template>
  <div id="about-page">
    <header>
      <h1>درباره ما</h1>
    </header>
    <main>
      <p>این صفحه درباره پروژه مکتب است. ما در اینجا به شما اطلاعات بیشتری ارائه می‌دهیم.</p>
    </main>
    <footer>
      <p>حق نشر © 2025. تمامی حقوق محفوظ است.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'AboutPage',
};
</script>

<style scoped>
#about-page {
  text-align: center;
  font-family: 'Tahoma', sans-serif;
  direction: rtl;
  padding: 20px;
}

header {
  background-color: #42b983;
  color: white;
  padding: 20px;
}

header h1 {
  margin: 0;
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
