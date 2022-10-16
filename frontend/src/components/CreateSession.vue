<template>
    <div v-if="visible" class="container">
        <form @submit.prevent="" class="session-form">
            <h2>Criar sessão</h2>
            <label for="session-name">Nome da sessão</label>
            <input v-model="sessionName" type="text" id="session-name" name="session-name">
            <br />
            <label for="day-of-week">Dia da semana</label>
            <select v-model="dayOfWeek" name="day-of-week" id="day-of-week">
                <option value="1">Domingo</option>
                <option value="2">Segunda-feira</option>
                <option value="3">Terça-feira</option>
                <option value="4">Quarta-feira</option>
                <option value="5">Quinta-feira</option>
                <option value="6">Sexta-feira</option>
                <option value="7">Sábado</option>
            </select>
            <h3>Treinos</h3>
            <p v-if="!trainings.length">Nenhum treino adicionado ainda</p>
            <ul v-else>
                <li v-for="(t, index) in trainings" :key="index">{{ (index + 1) + ' - ' + t.name }}</li>
            </ul>
            <button @click="showAddTrainingPopup">Adicionar treino</button>
            <button @click="createSession">Criar</button>
            <button @click="toggle">Fechar</button>
        </form>
        <add-training ref="addTrainingPopup" @add-training="addTraining" />
    </div>
</template>
<script>
import AddTraining from './AddTraining.vue'
export default {
    components: { AddTraining },
    data() {
        return {
            visible: false,
            sessionName: '',
            dayOfWeek: null,
            trainings: [],
        }
    },
    mounted() {
        this.setToken()
    },
    methods: {
        toggle() {
            this.visible = !this.visible
        },
        showAddTrainingPopup() {
            this.$refs.addTrainingPopup.toggle()
        },
        addTraining(training) {
            this.trainings.push(training)
        },
        mountCreateSessionPayload() {
            return {
                session_name: this.sessionName,
                day_of_week: this.dayOfWeek,
                trainings: [ ...this.trainings ]
            }
        },
        async setToken() {
            await fetch('http://localhost:8001/session/token')
        },  
        async createSession() {
            const payload = this.mountCreateSessionPayload()
            let fd = new FormData()
            for (let [key, value] of Object.entries(payload)) {
                fd.append(key, value)
            }
            let response = await fetch('http://localhost:8001/session/', {
                method: 'POST',
                body: fd,
                credentials: 'include',
                headers: {
                    'X-CSRFToken': this.$cookies.get('csrftoken'),
                }
            })
        }
    }
}
</script>
<style scoped>
.container {
    background-color: aqua;
    position: fixed;
    display: flex;
    justify-content: center;
    min-height: 400px;
    width: 400px;
}
.session-form {
    min-width: 90%;
    display: flex;
    flex-direction: column;
}
</style>