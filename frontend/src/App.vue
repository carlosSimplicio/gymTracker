<template>
    <div class="navbar">
      <h1>GymTracker</h1>
      <span>
        <p>{{ currentUser?.name }}</p>
        <p>{{ currentUser?.email }}</p>
        <button v-if="authStore.isAuthenticated" @click="signOut">Logout</button>
      </span>
    </div>
    <router-view></router-view>
</template>
<script>
import { useAuthStore } from './stores/auth';
export default {
  setup() {
    const authStore = useAuthStore() 
    return { authStore }
  },
  computed: {
    currentUser() {
      return this.authStore.user
    }
  },
  methods: {
    async signOut() {
      await fetch('http://localhost:8001/auth/logout', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': this.$cookies.get('csrftoken')
        }
      })
      this.authStore.removeUser()
      this.$router.push('/login')
    }
  }
}
</script>
<style>
 .navbar {
  display: flex;
  justify-content: space-between;
  height: 10vh;
 }
</style>