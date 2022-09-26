<template>
  <h1>Criar nova sessão</h1>
  <button @click="showCreateSessionPopup">Criar</button>
  <create-session ref="createSessionPopup"/>
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
</style>