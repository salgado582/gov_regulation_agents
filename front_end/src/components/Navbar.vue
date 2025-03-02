<template>
  <nav class="bg-white shadow mb-6">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <div class="text-2xl font-bold text-blue-600">
        <router-link to="/dashboard" class="hover:text-blue-700">
          Govt Regulation Agents Roadmap
        </router-link>
      </div>
      <div class="space-x-6">
        <router-link to="/dashboard" class="text-gray-700 hover:text-blue-600"
          >Dashboard</router-link
        >
        <router-link to="/upload" class="text-gray-700 hover:text-blue-600"
          >Upload Rules</router-link
        >
        <router-link to="/auditing" class="text-gray-700 hover:text-blue-600"
          >Auditing</router-link
        >
        <router-link to="/profile" class="text-gray-700 hover:text-blue-600"
          >Profile</router-link
        >
        <button
          @click="logout"
          class="text-gray-700 hover:text-blue-600 focus:outline-none"
        >
          Logout
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    logout() {
      // Clear authentication and redirect to login
      localStorage.removeItem("auth");
      this.$router.push("/login");
    },
  },
};
</script>
