<template>
    <div class="main-container">
      <h1>Criar nova sessão</h1>
      <button @click="showCreateSessionPopup">Criar</button>
      <create-session ref="createSessionPopup"/>
    </div>
</template>
<script>
import CreateSession from './components/CreateSession.vue'
export default {
  components: {CreateSession},
  data() {
    return {  
    }
  },
  methods: {
    showCreateSessionPopup() {
      this.$refs.createSessionPopup.toggle()
    }
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