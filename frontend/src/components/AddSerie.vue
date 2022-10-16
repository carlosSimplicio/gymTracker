<template>
    <div class="container3">
        <h4>Série {{ order+1 }}</h4>
        <label for="reps">Repetições</label>
        <input :value="reps" type="number" name="reps" id="reps" @input="updateReps">
        <br>
        <label for="load">Carga (kg)</label>
        <input :value="load" type="number" name="load" id="load" @input="updateLoad">
        <button @click="moveSerie(order, 1)">Subir</button>
        <button @click="moveSerie(order, -1)">Descer</button>
    </div>
</template>
<script>
export default {
    props: {
        load: {
            type: Number,
            default: null
        },
        reps: {
            type: Number,
            default: null
        },
        order: {
            type: Number,
            default: null
        },
    },
    data() {
        return {
            internalLoad: 0,
            internalReps: 0
        }
    },
    methods: {
        updateReps(event) {
            this.internalReps = event.target.valueAsNumber
            this.updateValues()
        },
        updateLoad(event) {
            this.internalLoad = event.target.valueAsNumber
            this.updateValues()
        },
        updateValues() {
            this.$emit(
                'update', 
                this.order,
                {
                    order: this.order,
                    load: this.internalLoad,
                    reps: this.internalReps,
                }
            )
        },
        moveSerie(order, direction) {
            this.$emit('move-serie', order, direction)
        },
    }
}
</script>
<style scoped="true">
.container3 {
    background-color: greenyellow;
}
</style>