<template>
    <div class="login-div">
        <h2>Por favor, se indentifique</h2>
        <form @submit.prevent="signIn" class="form">
            <label for="username">Nome de usuário</label>
            <input v-model="username" type="text" id="username">
            <label for="password">Senha</label>
            <input v-model="password" type="password" id="password">
            <button>Fazer login</button>
        </form>
    </div>
</template>
<script>
import { useAuthStore } from '../stores/auth'

export default {
    setup() {
        const authStore = useAuthStore()
        return {authStore}
    },
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        async signIn() {
            if (!(this.username && this.password)) return

            let form = new FormData()
            form.append('username', this.username)
            form.append('password', this.password)
            let response = await fetch('http://localhost:8001/auth/login', {
                method: 'POST',
                body: form,
                credentials: 'include',
                headers: {
                    'X-CSRFToken': this.$cookies.get('csrftoken')
                }
            })
            if (response.status == 200) {
                await this.authStore.getUser()
                this.$router.push('/home')
            }
        }
    }
}
</script>
<style scoped>
    .login-div{
        width: 400px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        margin: auto;
        justify-content: center;
    }
    .form {
        display: flex;
        flex-direction: column;
    }
</style>