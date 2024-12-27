<template>
  <div class="nutritionist-register">
    <h2>Register as Nutritionist</h2>
    <form @submit.prevent="registerNutritionist">
      <!-- First Name field -->
      <div>
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" v-model="nutritionist.first_name" required />
      </div>
      <!-- Last Name field -->
      <div>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" v-model="nutritionist.last_name" required />
      </div>
      <!-- Registration Number field -->
      <div>
        <label for="registration_number">Registration Number:</label>
        <input type="text" id="registration_number" v-model="nutritionist.registration_number" required />
      </div>
      <!-- Email field -->
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="nutritionist.email" required />
      </div>
      <!-- Phone field -->
      <div>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" v-model="nutritionist.phone" required />
      </div>
      <!-- Password field -->
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="nutritionist.password" required />
      </div>
      <!-- Confirm Password field -->
      <div>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" v-model="nutritionist.confirm_password" required />
      </div>
      <button type="submit">Register</button>
    </form>

    <!-- Message display -->
    <p v-if="message" class="error">{{ message }}</p>
  </div>
</template>

<script scoped>
import axios from 'axios';

export default {
  data() {
    return {
      nutritionist: {
        first_name: '',
        last_name: '',
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
      // Prepare the data to be sent to the backend
      const nutritionistData = {
        first_name: this.nutritionist.first_name,
        last_name: this.nutritionist.last_name,
        registration_number: this.nutritionist.registration_number,
        email: this.nutritionist.email,
        phone: this.nutritionist.phone,
        password: this.nutritionist.password,
        confirm_password: this.nutritionist.confirm_password,
      };
      try {
        // Send registration data to the Django backend
        await axios.post('http://127.0.0.1:8000/auth/api/register/nutritionist/', nutritionistData);
        // Handle success, redirect or show success message
        this.message = 'Nutritionist registered successfully!';
      } catch (error) {
        // Handle errors if any
        if (error.response) {
          // If error.response exists, show the error message from backend
          const errors = error.response.data;
          if (errors.email) {
            this.message = errors.email[0];
          } else if (errors.non_field_errors) {
            this.message = errors.non_field_errors[0];
          } else if (errors.password){
            this.message = errors.password[0];
          } else {
            this.message = 'Error registering nutritionist: ' + JSON.stringify(errors);
          }
        } else {
          // If there's no response, handle the general error
          this.message = 'An unexpected error occurred.';
        }
      }
    }
  }
};
</script>
