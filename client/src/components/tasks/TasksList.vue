<template>
    <div>
        <b-spinner v-if="$store.state.getTaskStatus == 0"
            variant="info"
            label="Spinning"
        >
        </b-spinner>
        <p v-if="$store.state.getTaskStatus == -1">Błąd ładowania</p>
        <b-card
            variant="info"
            class="my-2"
            border-variant="info"
            v-for="task in $store.state.tasksList" :key = task.id
        >
            <ShowTask
                v-bind:task="task"
            />
        </b-card>
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
        };
    },
    mounted() {
        this.$store.dispatch('getTasks');
    },
};

</script>

<style scoped>

</style>
