<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2>ورود</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <input type="email" v-model="email" placeholder="ایمیل" required />
        </div>
        <div class="input-group">
          <input type="password" v-model="password" placeholder="رمز عبور" required />
        </div>
        <button type="submit" class="auth-button">ورود</button>
        <p v-if="error" class="error-message">{{ errorMessage }}</p>
        <div class="additional-options">
          <div class="social-login">
            <p>یا:</p>
            <a :href="googleLoginUrl" class="social-button">ورود با گوگل</a>
          </div>
          <div class="password-reset">
            <a @click="goToPasswordReset" class="reset-link">فراموشی رمز عبور؟</a>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: '',
      error: false,
      errorMessage: '',
      googleLoginUrl: 'http://127.0.0.1:8000/accounts/google/login/',
    };
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin() {
      try {
        await this.login({ email: this.email, password: this.password });
        this.$router.push('/');
      } catch (error) {
        this.error = true;
        this.errorMessage = 'خطایی در ورود رخ داده است.';
      }
    },
    goToPasswordReset() {
      this.$router.push('/password-reset');
    },
  },
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
}

.auth-button:hover {
  background-color: #00796b;
}

.error-message {
  color: red;
  text-align: center;
}

.additional-options {
  margin-top: 20px;
  text-align: center;
}

.social-login {
  margin-bottom: 10px;
}

.social-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #db4437;
  color: white;
  border-radius: 5px;
  text-decoration: none;
  margin: 5px;
}

.social-button:hover {
  background-color: #c33c2f;
}

.password-reset {
  margin-top: 10px;
}

.reset-link {
  color: #00796b;
  text-decoration: none;
  cursor: pointer;
}

.reset-link:hover {
  color: #004d40;
}
</style>
