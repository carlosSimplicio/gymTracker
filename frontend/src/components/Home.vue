<template>
    <div class="main-container">
      <h1>Criar nova sessão</h1>
      <button @click="showCreateSessionPopup">Criar</button>
      <create-session ref="createSessionPopup"/>
    </div>
</template>
<script>
import CreateSession from './CreateSession.vue'
import { useAuthStore } from '../stores/auth'

export default {
  setup() {
    const authStore = useAuthStore()
    return { authStore }
  },
  components: {CreateSession},
  data() {
    return {  
    }
  },
  async mounted() {
        await this.authStore.getUser()

        if (!this.authStore.isAuthenticated) {
            this.$router.push('/login')
        }
  },
  methods: {
    showCreateSessionPopup() {
      this.$refs.createSessionPopup.toggle()
    },
  }
}
</script>
<style>
body {
 height: 100vh;
}
#app {
  height: 100vh;
}
.main-container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>