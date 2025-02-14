<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

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
  // صفحه درباره ما که شامل اطلاعاتی درباره پروژه مکتب است
};
</script>

<style scoped>
#about-page {
  text-align: center;
  font-family: 'Tahoma', sans-serif;
  direction: rtl;
  padding: 20px;
  /* استایل‌دهی به صفحه درباره ما */
}

header {
  background-color: #42b983;
  color: white;
  padding: 20px;
  /* استایل‌دهی به هدر */
}

header h1 {
  margin: 0;
  /* حذف حاشیه از تگ h1 */
}

main {
  margin-top: 20px;
  font-size: 18px;
  /* استایل‌دهی به بخش اصلی محتوا */
}

footer {
  margin-top: 40px;
  color: #555;
  /* استایل‌دهی به فوتر */
}
</style>
