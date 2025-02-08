<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2>ثبت نام</h2>
      <form @submit.prevent="handleRegister">
        <div class="input-group">
          <input type="text" v-model="username" placeholder="نام کاربری" required />
        </div>
        <div class="input-group">
          <input type="email" v-model="email" placeholder="ایمیل" required />
        </div>
        <div class="input-group">
          <input type="password" v-model="password1" placeholder="رمز عبور" required />
        </div>
        <div class="input-group">
          <input type="password" v-model="password2" placeholder="تایید رمز عبور" required />
        </div>
        <button type="submit" class="auth-button">ثبت نام</button>
        <p v-if="error" class="error-message">{{ errorMessage }}</p>
        <p v-if="confirmationMessage" class="confirmation-message">{{ confirmationMessage }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'RegisterForm',
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: '',
      error: false,
      errorMessage: '',
      confirmationMessage: ''
    };
  },
  methods: {
    ...mapActions(['register']),
    async handleRegister() {  // Renamed to avoid conflict
      console.log('Register form submitted'); // Debugging log
      try {
        await this.register({
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2
        });
        if (!this.$store.state.token) {
          this.confirmationMessage = 'لطفاً ایمیل خود را برای تأیید حساب بررسی کنید.';
        } else {
          this.$router.push('/');
        }
      } catch (error) {
        this.error = true;
        this.errorMessage = 'خطایی در ثبت نام رخ داده است.';
        console.error('Register form error:', error); // Debugging log
      }
    }
  }
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f9f9f9;
}

.auth-card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

.auth-card h2 {
  margin-bottom: 20px;
  text-align: center;
}

.input-group {
  margin-bottom: 15px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.auth-button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 10px 20px;
  width: 100%;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.auth-button:hover {
  background-color: #00796b;
}

.error-message {
  color: red;
  text-align: center;
}

.confirmation-message {
  color: green;
  text-align: center;
}
</style>
