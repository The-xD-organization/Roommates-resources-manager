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
            <div
                v-for="task in $store.state.tasksList" :key = task.id
            >
                <ShowTask
                    v-bind:task="task"
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
        };
    },
    mounted() {
        this.$store.dispatch('getTasks');
    },
};

</script>

<style scoped>

</style>
