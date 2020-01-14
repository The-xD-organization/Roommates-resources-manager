<template>
        <b-card
        variant="info"
        class="my-2"
        border-variant="info"
        :class="{done: task.is_done||doClicked}"
    >
        <h5> {{ task.description }} </h5>
        <hr>
        <p>Data utworzenia: {{ task.date_of_creation }}</p>
        <p v-if="task.assignee_name != null">Przypisana osoba: {{ task.assignee_name }} </p>
        <b-button
            v-else
            variant="btn" class="m-1"
        >
            Przypisz się
        </b-button>
        <b-button
            v-if="task.is_done == false"
            variant="btn" class="m-1"
            @click="doTask()"
        >
            Zrobione
        </b-button>
    </b-card>
</template>

<script>
export default {
    name: 'ShowTask',
    props: {
        task: Object,
    },
    data() {
        return {
            doClicked: false,
        };
    },
    methods: {
        doTask() {
            this.$store.dispatch('doTask', this.task.id);
            this.doClicked = true;
        },
    },
};

</script>

<style scoped>
.btn{
    background-color:white;
    border-color: #17a2b8;
    color:#17a2b8;
}
.btn:hover{
    background-color: #17a2b8;
    color:white;
}
.done{
    background-color:aquamarine!important;
}
</style>
