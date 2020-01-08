<template>
    <div>
        <!-- <b-spinner v-if="" variant="info"
        label="Spinning"></b-spinner> spinner
        <p>Błąd ładowania</p> -->
        <b-card
            variant="info"
            class="my-2"
            border-variant="info"
        >
            <ShowTask
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
};

</script>

<style scoped>

</style>
