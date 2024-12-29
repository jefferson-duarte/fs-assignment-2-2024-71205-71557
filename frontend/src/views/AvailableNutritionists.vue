<template>
  <div class="nutritionist-list container mt-5">
    <!-- Page Title -->
    <h2 class="text-center mb-4">Choose Your Nutritionist</h2>
    <!-- Success Message Alert -->
    <div v-if="message" class="alert alert-success">{{ message }}</div>
    <!-- Error Message Alert -->
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <!-- List of Nutritionists -->
    <ul class="list-group">
      <!-- Loop through nutritionists and display each one -->
      <li v-for="nutritionist in nutritionists" :key="nutritionist.id"
        class="list-group-item d-flex justify-content-between align-items-center">
        <span>
          {{ nutritionist.first_name || 'No Name' }} {{ nutritionist.last_name || '' }}
        </span>
        <!-- Button to select a nutritionist -->
        <button @click="selectNutritionist(nutritionist.id)" class="btn btn-primary btn-sm">
          Select
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  data() {
    return {
      // List of nutritionists
      nutritionists: [],
      // Success message
      message: '',
      // Error message
      error: ''
    }
  },
  // Fetch the list of nutritionists when the component is created
  created() {
    this.fetchNutritionists();
  },
  methods: {
    // Method to fetch the list of nutritionists from the backend
    async fetchNutritionists() {
      try {
        const response = await axiosInstance.get('/api/nutritionists/');
        this.nutritionists = response.data;
      } catch (error) {
        this.error = 'Failed to fetch nutritionists.';
      }
    },
    // Method to select a nutritionist
    async selectNutritionist(nutritionistId) {
      try {
        await axiosInstance.post('/api/select-nutritionist/', {
          nutritionist_id: nutritionistId
        });
        this.message = 'Nutritionist selected successfully!';
        // Redirect to the dashboard after selecting a nutritionist
        this.$router.push('/dashboard');
      } catch (error) {
        this.error = 'Failed to select nutritionist.';
      }
    }
  }
}
</script>

<style scoped>
.nutritionist-list {
  max-width: 600px;
  margin: 0 auto;
}
</style>
