<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-auth-container">
    <div class="maktab-auth-card">
      <h2>رمز عبور را بازیابی کنید</h2>
      <form @submit.prevent="resetMaktabPassword">
        <div class="input-group">
          <input type="email" v-model="email" placeholder="ایمیل" required />
        </div>
        <button type="submit" class="maktab-auth-button">ارسال لینک بازیابی</button>
        <p v-if="message" class="success-message">{{ message }}</p>
        <p v-if="error" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MaktabPasswordResetForm',
  data() {
    return {
      email: '',
      message: '',
      error: false,
      errorMessage: ''
    };
  },
  methods: {
    async resetMaktabPassword() {
      // ارسال درخواست بازیابی رمز عبور به API
      try {
        await axios.post('http://127.0.0.1:8000/dj-rest-auth/password/reset/', {
          email: this.email
        });
        this.message = 'لینک بازیابی رمز عبور به ایمیل شما ارسال شد.';
        this.error = false;
      } catch (error) {
        this.error = true;
        this.errorMessage = 'خطایی در ارسال لینک بازیابی رخ داده است.';
      }
    }
  }
};
</script>

<style scoped>
.maktab-auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f9f9f9;
  /* استایل‌دهی به بخش ورود */
}

.maktab-auth-card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  /* استایل‌دهی به کارت احراز هویت */
}

.maktab-auth-card h2 {
  margin-bottom: 20px;
  text-align: center;
  /* استایل‌دهی به تیتر */
}

.input-group {
  margin-bottom: 15px;
  /* استایل‌دهی به گروه ورودی */
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  /* استایل‌دهی به فیلد ورودی ایمیل */
}

.maktab-auth-button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 10px 20px;
  width: 100%;
  cursor: pointer;
  border-radius: 5px;
  /* استایل‌دهی به دکمه ارسال */
}

.maktab-auth-button:hover {
  background-color: #00796b;
  /* استایل‌دهی دکمه در حالت هاور */
}

.success-message {
  color: green;
  text-align: center;
  /* استایل‌دهی به پیام موفقیت */
}

.error-message {
  color: red;
  text-align: center;
  /* استایل‌دهی به پیام خطا */
}
</style>
