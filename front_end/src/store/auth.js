// src/store/auth.js
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthenticated: localStorage.getItem("auth") === "true",
  }),
  actions: {
    login() {
      this.isAuthenticated = true;
      localStorage.setItem("auth", "true");
    },
    logout() {
      this.isAuthenticated = false;
      localStorage.removeItem("auth");
    },
  },
});
