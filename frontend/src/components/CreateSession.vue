<template>
    <div v-if="visible" class="container">
        <form @submit.prevent="">
            <h2>Criar sessão</h2>
            <label for="session-name">Nome da sessão</label>
            <input type="text" id="session-name" name="session-name">
            <br />
            <label for="day-of-week">Dia da semana</label>
            <select name="day-of-week" id="day-of-week">
                <option value="1">Domingo</option>
                <option value="2">Segunda-feira</option>
                <option value="3">Terça-feira</option>
                <option value="4">Quarta-feira</option>
                <option value="5">Quinta-feira</option>
                <option value="6">Sexta-feira</option>
                <option value="7">Sábado</option>
            </select>
            <h3>Treinos</h3>
            <ul>
                <li v-for="(t, index) in trainings" :key="index">{{ (index + 1) + ' - ' + t.name }}</li>
            </ul>
            <button @click="showAddTrainingPopup">Adicionar treino</button>
        </form>
        <add-training ref="addTrainingPopup" />
    </div>
</template>
<script>
import AddTraining from './AddTraining.vue'
export default {
    components: { AddTraining },
    data() {
        return {
            visible: false,
            trainings: [{
                name: 'Bíceps'
            }],
        }
    },
    methods: {
        toggle() {
            this.visible = !this.visible
        },
        showAddTrainingPopup() {
            this.$refs.addTrainingPopup.toggle()
        }
    }
}
</script>
<style scoped>
.container {
    background-color: aqua;
}
</style>