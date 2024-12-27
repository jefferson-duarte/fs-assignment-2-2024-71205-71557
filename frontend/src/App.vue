<template>
  <!-- The root div element of the app -->
  <div id="app">
    <!-- This is where the routed components will be rendered based on the active route -->
    <router-view />
  </div>
</template>

<script scoped>
export default {
  name: 'App', // Define the name of the component
};
</script>
