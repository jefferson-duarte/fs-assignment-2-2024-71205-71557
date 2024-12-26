<template>
  <div class="nutritionist-register">
    <h2>Register as Nutritionist</h2>
    <form @submit.prevent="registerNutritionist">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="form.name" required />
      </div>
      <div>
        <label for="registration_number">Registration Number:</label>
        <input type="text" id="registration_number" v-model="form.registration_number" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="form.email" required />
      </div>
      <div>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" v-model="form.phone" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="form.password" required />
      </div>
      <div>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" v-model="form.confirm_password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        name: '',
        registration_number: '',
        email: '',
        phone: '',
        password: '',
        confirm_password: ''
      },
      message: ''
    };
  },
  methods: {
    async registerNutritionist() {
      try {
        await axios.post('http://127.0.0.1:8000/auth/api/register/nutritionist/', this.form);
        this.message = 'Nutritionist registered successfully!';
        this.form = { name: '', registration_number: '', email: '', phone: '', password: '', confirm_password: '' };
      } catch (error) {
        this.message = 'Error registering nutritionist. Please check your data.';
      }
    }
  }
};
</script>
