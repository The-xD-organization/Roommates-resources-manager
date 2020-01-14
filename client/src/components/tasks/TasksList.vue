<template>
    <div>
        <b-spinner
            v-if="$store.state.getTaskStatus == 0"
            variant="info"
            label="Spinning"
        >
        </b-spinner>
        <p v-if="$store.state.getTaskStatus == -1">Błąd ładowania</p>
        <div v-else>
            <h5>Wyświetlaj:</h5>
            <label class="container">Niezrobione
                <input type="checkbox" id="notDone" value="true" v-model="notDone">
                <span class="checkmark"></span>
            </label>
            <label class="container">Zroobione
                <input type="checkbox" id="done" value="true" v-model="done">
                <span class="checkmark"></span>
            </label>
            <div
                v-for="task in $store.state.tasksList" :key = task.id
            >
                <ShowTask
                    v-bind:task="task"
                    v-if="(done == task.is_done || notDone == !task.is_done)
                        && !(notDone == false && done == false)"
                />
            </div>
        </div>
    </div>
</template>

<script>
import ShowTask from '@/components/tasks/ShowTask.vue';

export default {
    name: 'TasksList',
    components: {
        ShowTask,
    },
    data() {
        return {
            notDone: true,
            done: false,
        };
    },
    mounted() {
        this.$store.dispatch('getTasks');
    },
};

</script>

<style scoped>

</style>
