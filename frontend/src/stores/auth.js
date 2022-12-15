import { defineStore } from 'pinia'
import { ref, computed, watch } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const user = ref({})
    
    const userInStorage = localStorage.getItem('currentUser')
    if (userInStorage) {
        user.value = JSON.parse(userInStorage)
    }

    watch(() => user, (state) => {
        localStorage.setItem('currentUser', JSON.stringify(state.value))
    }, { deep: true })

    const isAuthenticated = computed(() => !!user.value && !!user.value.authenticated)
    const getUser = async () => {
        let response = await fetch('http://localhost:8001/auth/whoami')
        user.value = await response.json()
    }
    const removeUser = async () => user.value = {}

    return { user, isAuthenticated, getUser, removeUser }
})