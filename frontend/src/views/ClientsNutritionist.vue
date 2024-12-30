<template>
  <div class="client-list container mt-5">
    <!-- Page Title -->
    <h2 class="text-center mb-4">Your Clients</h2>

    <!-- Error Message Alert -->
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <!-- List of Clients -->
    <ul class="list-group">
      <li v-for="client in clients" :key="client.id" class="list-group-item d-flex justify-content-between align-items-center">
        <span>{{ client.user.first_name || 'No Name' }} {{ client.user.last_name || '' }}</span>
        <span>{{ client.phone }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  data() {
    return {
      clients: [],
      error: ''
    }
  },
  created() {
    this.fetchClients();
  },
  methods: {
    async fetchClients() {
      try {
        const response = await axiosInstance.get('/api/nutritionist/clients/');
        this.clients = response.data;
      } catch (error) {
        this.$router.push('/login'); // Redirect to login page
      }
    },
  }
}
</script>

<style scoped>
.client-list {
  max-width: 600px;
  margin: 0 auto;
}
</style>
