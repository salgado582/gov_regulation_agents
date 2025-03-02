<!-- src/components/Navbar.vue -->
<template>
  <nav class="bg-white shadow mb-6">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <div class="text-2xl font-bold text-blue-600">
        <router-link
          to="/dashboard"
          class="hover:text-blue-700"
          active-class="font-bold text-blue-700"
        >
          Govt Regulation Agents
        </router-link>
      </div>
      <div class="space-x-6">
        <router-link
          to="/dashboard"
          class="text-gray-700 hover:text-blue-600"
          active-class="font-bold text-blue-700"
        >
          Dashboard
        </router-link>
        <router-link
          to="/upload"
          class="text-gray-700 hover:text-blue-600"
          active-class="font-bold text-blue-700"
        >
          Upload Rules
        </router-link>
        <router-link
          to="/auditing"
          class="text-gray-700 hover:text-blue-600"
          active-class="font-bold text-blue-700"
        >
          Auditing
        </router-link>
        <router-link
          to="/profile"
          class="text-gray-700 hover:text-blue-600"
          active-class="font-bold text-blue-700"
        >
          Profile
        </router-link>
        <router-link
          to="/about"
          class="text-gray-700 hover:text-blue-600"
          active-class="font-bold text-blue-700"
        >
          About Us
        </router-link>
        <!-- Show Logout button only if the user is authenticated -->
        <button
          v-if="authStore.isAuthenticated"
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
import { useAuthStore } from "../store/auth";

export default {
  name: "Navbar",
  setup() {
    const authStore = useAuthStore();
    const logout = () => {
      authStore.logout();
      // Redirect to login after logout
      // Using window.location.href here or this.$router.push('/login') if using Options API
      // For this example we'll assume Options API methods are available via the router instance.
      window.location.href = "/login";
    };
    return { authStore, logout };
  },
};
</script>
