<!-- src/App.vue -->
<template>
  <div class="min-h-screen bg-gradient-to-r from-blue-50 to-blue-100">
    <Navbar />
    <div class="container mx-auto p-4">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>
