<template>
  <div id="app">
    <!-- Navbar appears on every page -->
    <NavBar />
    <!-- This is where the page components are rendered -->
    <router-view />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>
