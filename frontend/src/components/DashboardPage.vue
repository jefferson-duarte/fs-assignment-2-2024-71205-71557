<template>
  <div>
    <h2>Welcome to the Dashboard</h2>
    <button @click="logout">Logout</button>
  </div>
</template>

<script scoped>
export default {
  methods: {
    logout() {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      this.$router.push("/login");
    },
  },
};
</script>
