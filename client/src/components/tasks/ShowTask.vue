<template>
    <div>
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
        >
            Zrobione
        </b-button>
    </div>
</template>

<script>
export default {
    name: 'ShowTask',
    props: {
        task: Object,
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
</style>
