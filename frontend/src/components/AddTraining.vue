<template>
    <div v-if="visible" class="mask">
        <div class="container2">
            <form @submit.prevent="">
                <h4>Adicionar Treino</h4>
                <label for="select-exercise">Exercício</label>
                <select v-model="selectedExercise" name="select-exercise" id="select-exercise">
                    <option v-for="item in exercises" :value="item" :key="item.id">
                        {{ item.name }}
                    </option>
                </select>
                <br>
                <label for="min-reps">Mínimo de repetições</label>
                <input 
                    v-model="minReps"
                    type="number"
                    id="min-reps"
                    name="min-reps"
                />
                <br>
                <label for="max-reps">Máximo de repetições</label>
                <input
                    v-model="maxReps"
                    type="number"
                    id="max-reps"
                    name="max-reps"
                />
                <br>
                <label for="qtd-series">Quantidade de séries</label>
                <input 
                    v-model="qtdSeries"
                    type="number"
                    id="qtd-series"
                    name="qtd-series"
                    max="20"
                    @input="handleSeriesArray"
                >
                <div v-for="item in series">
                    <add-serie
                        :load="item.load"
                        :reps="item.reps"
                        :order="item.order"
                        :key="item.order"
                        @update="updateSerie"
                        @move-serie="moveSerie"
                    />
                </div>
            </form>
            <button @click="addTraining">Adicionar</button>
            <button @click="toggle">Fechar</button>
        </div>
    </div>
</template>
<script>
import AddSerie from './AddSerie.vue'
export default {
    components: { AddSerie },
    data() {
        return {
            visible: false,
            minReps: 0,
            maxReps: 0,
            qtdSeries: 0,
            series: [],
            selectedExercise: null,
            exercises: [
                {
                    id: 1,
                    name: 'Rosca Direta',
                    min: 6,
                    max: 15,
                },
                {
                    id: 2,
                    name: 'Triceps Francês',
                    min: 6,
                    max: 15,
                },
                {
                    id: 3,
                    name: 'Remada curvada',
                    min: 6,
                    max: 15,
                }
            ]
        }
    },
    methods: {
        toggle() {
            this.visible = !this.visible
        },
        handleSeriesArray() {
            if (this.qtdSeries > this.series.length) {
                for (let i=0; i < this.qtdSeries; i++) {
                    this.series.push({
                        order: this.series.length,
                        load: 0,
                        reps: 0
                    })
                }
            }
            if (this.qtdSeries < this.series.length) {
                for (let i=this.series.length; i > this.qtdSeries; i--) {
                    this.series.pop()
                }
            }
        },
        updateSerie(order, serie) {
            this.series[order] = {...serie}
        },
        moveSerie(order, direction) {
            if (
                (order <= 0 && direction === 1) ||
                (order >= this.series.length -1  && direction === -1)
            ) return

            this.series = this.series.map(serie => {
                if (serie.order === order) {
                    serie.order -= direction
                }
                else if (serie.order + direction === order) {
                    serie.order += direction
                }
                return serie
            })
            .sort((a,b) => a.order - b.order)
        },
        mountTrainingObject() {
            return {
                name: `${this.selectedExercise.name} - ${this.qtdSeries} sets de ${this.minReps} a ${this.maxReps}`,
                exercise: this.selectedExercise,
                min_reps: this.minReps,
                max_reps: this.maxReps,
                qtd_series: this.qtdSeries,
                series: this.series
            }
        },
        addTraining() {
            const training = this.mountTrainingObject()
            this.$emit('add-training', training)
            this.toggle()
        }
    },
}
</script>
<style scoped>
.mask {
    position: fixed;
    height: 100vh;
    width: 100vw;
    top: 0;
    left: 0;
    z-index: 9998;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}
.container2 {
    min-height: 600px;
    max-width: 400px;
    background-color: red;
    display: flex;
    flex-direction: column;
    padding: 50px;
}
</style>